import glob
import json
import os

import requests
import logging

from django.conf import settings
from core.utils import async_get_data
from sdg_api.models import GeoArea

logger = logging.getLogger(__name__)


class SdgApi:
    base = 'https://unstats.un.org/SDGAPI'

    def get(self, extension, params=None):
        url = self.base + extension
        return requests.get(url, params=params).json()

    # GeoArea

    def GeoArea_list(self):
        return self.get('/v1/sdg/GeoArea/List')

    # Series

    def Series_list(self):
        return self.get('/v1/sdg/Series/List')

    # Target

    def Target_list(self):
        return self.get('/v1/sdg/Target/List')

    def all_Target_pivot_data_from_files(self):
        all_pivot_data = []

        for fname in glob.glob((os.path.join(settings.BASE_DIR, 'poland-data', 'poland-page-*.json'))):
            with open(fname, 'r') as f:
                pivot_data_page = json.loads(f.read())
                all_pivot_data += pivot_data_page['data']

        return all_pivot_data

    def all_Target_pivot_data(self):
        page_size = 500

        # def _func(page):
        #     pivot_data_page = self.get('/v1/sdg/Target/PivotData', {
        #         'page': page,
        #         'pageSize': page_size,
        #     })
        #     return pivot_data_page['data']
        #
        #
        # first_page = self.get('/v1/sdg/Target/PivotData', {
        #     'page': 1,
        #     'pageSize': page_size,
        # })
        #
        # all_pivot_data = async_get_data(_func, range(1, first_page['totalPages'] + 1))



        all_pivot_data = []

        logger.debug('Getting all Target pivot data')

        pivot_data_page = self.get('/v1/sdg/Target/PivotData', {
            'page': 1,
            'pageSize': page_size,
            'areaCode': GeoArea.Poland().code,
        })
        all_pivot_data += pivot_data_page['data']
        total_pages = pivot_data_page['totalPages']

        logger.debug('Got first page')

        for page in range(2, total_pages + 1):
            pivot_data_page = self.get('/v1/sdg/Target/PivotData', {
                'page': page,
                'pageSize': page_size,
                'areaCode': GeoArea.Poland().code,
            })
            all_pivot_data += pivot_data_page['data']
            logger.debug('all_Target_pivot_data: {}/{}'.format(page, total_pages))

        return all_pivot_data

    def Target_pivot_data(self, target, areaCode):
        assert target and areaCode, 'Both target and areaCode are required by this method.'
        return self.get('/v1/sdg/Target/PivotData', {
            'target': target,
            'areaCode': areaCode,
        })


