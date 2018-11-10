import logging

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        from sdg_api.api import SdgApi
        from sdg_api.models import GeoArea
        sdg_api = SdgApi()
        geo_area_list = sdg_api.GeoArea_list()

        geo_area_model_list = []

        GeoArea.objects.all().delete()

        for i, geo_area in enumerate(geo_area_list):
            geo_area_model_list.append(GeoArea(
                code=geo_area['geoAreaCode'],
                name=geo_area['geoAreaName'],
            ))
            logger.debug('{}/{}'.format(i+1, len(geo_area_list)))

        GeoArea.objects.bulk_create(geo_area_model_list)


