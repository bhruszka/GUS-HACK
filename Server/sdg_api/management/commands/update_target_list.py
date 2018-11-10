import logging

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        from sdg_api.api import SdgApi
        from sdg_api.models import Target
        sdg_api = SdgApi()
        target_list = sdg_api.Target_list()

        target_model_list = []

        Target.objects.all().delete()

        for i, target in enumerate(target_list):
            target_model_list.append(Target(
                goal=target['goal'],
                code=target['code'],
                title=target['title'],
                description=target['description'],
                uri=target['uri'],
            ))
            logger.debug('{}/{}'.format(i+1, len(target_list)))

        Target.objects.bulk_create(target_model_list)


