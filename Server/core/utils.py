import time
import traceback
from threading import Lock, currentThread, Thread
import logging


logger = logging.getLogger(__name__)

MAX_THREADS = 200


def async_get_data(func, data, mapping=False):
    """
    This is used to asynchronously get records.

    :param func: The function that receives a single element of data as its first parameter
    :param data: A set of data
    :param mapping: Whether or not the result should contain a mapping of data -> result
    :return: A list of results from calling func on each data element or a list of dicts in the format {'key': element, 'value': func_result}
    """
    ret = []
    ret_lock = Lock()

    def _func(_chunk):
        counter = 0
        for element in _chunk:
            # call func and append result to list
            # in case of exception try again
            recovered = False
            for i in range(5):  # try to recover only 5 times
                try:
                    if mapping:
                        data_to_append = {'key': element, 'value': func(element)}
                    else:
                        data_to_append = func(element)

                    ret_lock.acquire()
                    # enter critical section
                    ret.append(data_to_append)
                    # exit critical section
                    ret_lock.release()

                    counter += 1
                    if recovered:
                        logger.info('%s: %d/%d RECOVERED FROM EXCEPTION', currentThread().name, counter, len(_chunk))
                    else:
                        logger.info('%s: %d/%d', currentThread().name, counter, len(_chunk))
                    break
                except Exception:
                    logger.info('%s: %s', currentThread().name, traceback.format_exc())
                    recovered = True
        logger.info('%s finished', currentThread().name)

    partitioned_data = partition(data, MAX_THREADS)
    thread_pool = []
    start = time.time()
    logger.info('Initializing %d threads...', len(partitioned_data))
    for chunk in partitioned_data:
        t = Thread(target=_func, args=(chunk,))
        t.daemon = False
        t.start()
        thread_pool.append(t)
    logger.info('Initialization finished. Waiting for threads to exit...')
    for t in thread_pool:
        t.join()
    end = time.time()
    logger.info('async_get_data finished in %s seconds', end - start)
    return ret


def partition(lst, n):
    q, r = divmod(len(lst), n)
    indices = [q*i + min(i, r) for i in range(n+1)]
    return [lst[indices[i]:indices[i+1]] for i in range(min(len(lst), n))]
