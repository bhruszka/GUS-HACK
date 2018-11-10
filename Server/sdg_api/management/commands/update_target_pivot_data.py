import logging

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    sexes = {
        'FEMALE': 'females',
        'MALE': 'males',
        'BOTHSEX': 'both genders',
    }

    def handle(self, *args, **kwargs):
        from sdg_api.api import SdgApi
        from sdg_api.models import TargetPivotData
        sdg_api = SdgApi()
        target_pivot_data_list = sdg_api.all_Target_pivot_data_from_files()

        target_pivot_data_model_list = []

        TargetPivotData.objects.all().delete()

        for i, pivot_data in enumerate(target_pivot_data_list):
            sex = pivot_data.get('sex')
            if sex:
                sex = self.sexes[sex]

            target_pivot_data_model_list.append(TargetPivotData(
                goal=pivot_data['goal'],
                target=pivot_data['target'],
                indicator=pivot_data['indicator'],
                source=pivot_data['source'],
                data=pivot_data['years'],
                series=pivot_data['series'],
                sex=sex,
            ))
            logger.debug('{}/{}'.format(i+1, len(target_pivot_data_list)))

        TargetPivotData.objects.bulk_create(target_pivot_data_model_list)


