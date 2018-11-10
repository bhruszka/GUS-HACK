import json
import logging

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


def getValue(p):
    return p['value']


def getYear(p):
    return p['year']

def unitParser(u):
    if u == "PERCENT":
        return "%"
    elif u == "NUMBER":
        return ""
    elif u == "PER_100000_LIVE_BIRTHS":
        return "per 100000 live births"
    elif u == "PER_1000_LIVE_BIRTHS":
        return "per 1000 live births"

    return u


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        from sdg_api.models import TargetPivotData, Target

        unit_dict = {}

        for e in TargetPivotData.objects.all():
            # target = Target.objects.
            data = json.loads(e.data)
            data_with_value = [d for d in data if getValue(d) != '']
            min_val = min(data_with_value, key=getValue)
            max_val = max(data_with_value, key=getValue)
            newest_val = data_with_value[-1]
            # print("Min: {}, Max: {}, Newest: {}".format(min_val, max_val, newest_val))
            unit_dict[min_val['Units']] = 1
            unit_dict[max_val['Units']] = 1
            unit_dict[newest_val['Units']] = 1

        # print(unit_dict.keys())
        print(len(unit_dict.keys()))
        for k in unit_dict.keys():
            print(k)
