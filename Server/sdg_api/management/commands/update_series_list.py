import logging

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        from sdg_api.api import SdgApi
        from sdg_api.models import Series
        sdg_api = SdgApi()
        series_list = sdg_api.Series_list()

        series_model_list = []

        Series.objects.all().delete()

        for i, series in enumerate(series_list):
            logger.debug('{}/{}'.format(i+1, len(series_list)))
            series_model_list.append(Series(
                goal=series['goal'][0],
                target=series['target'][0],
                indicator=series['indicator'][0],
                code=series['code'],
                description=series['description'],
                uri=series['uri'],
            ))

        Series.objects.bulk_create(series_model_list)


