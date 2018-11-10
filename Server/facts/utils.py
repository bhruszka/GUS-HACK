from rest_framework import pagination
from rest_framework.response import Response


class PaginationWithPageCount(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data,
        })


def unit_parser(unit):
    if unit == 'CON_10USD':
        unit_parsed = 'CON_10USD'
    elif unit == 'CON_USD':
        unit_parsed = 'Constant USD'
    elif unit == 'CUR_LCU':
        unit_parsed = 'CUR_LCU'
    elif unit == 'CU_USD':
        unit_parsed = 'CU_USD'
    elif unit == 'HA_TH':
        unit_parsed = 'HA_TH'
    elif unit == 'INDEX':
        unit_parsed = 'Index'
    elif unit == 'KG_PER_CON_USD':
        unit_parsed = 'Kilograms per Constant USD'
    elif unit == 'KMSQ':
        unit_parsed = 'KMSQ'
    elif unit == 'LTPUREAL':
        unit_parsed = 'LTPUREAL'
    elif unit == 'MJ_PER_GDP_CON_PPP_USD':
        unit_parsed = 'Megajoules per USD constant 2011 PPP GDP'
    elif unit == 'M_M3_PER_YR':
        unit_parsed = u'Million m\u00B3 per year'
    elif unit == 'NUMBER':
        unit_parsed = 'Number'
    elif unit == 'NUM_U5_M':
        unit_parsed = 'NUM_U5_M'
    elif unit == 'PERCENT':
        unit_parsed = 'Percent'
    elif unit == 'PER_1000000_POP':
        unit_parsed = 'Per million population'
    elif unit == 'PER_100000_EMP':
        unit_parsed = 'PER_100000_EMP'
    elif unit == 'PER_100000_LIVE_BIRTHS':
        unit_parsed = 'per 100000 live births'
    elif unit == 'PER_1000_LIVE_BIRTHS':
        unit_parsed = 'per 1000 live births'
    elif unit == 'PER_100000_POP':
        unit_parsed = 'Per 100,000 population'
    elif unit == 'PER_1000_POP':
        unit_parsed = 'Per 1,000 population'
    elif unit == 'PER_100_POP':
        unit_parsed = 'Per 100 population'
    elif unit == 'PER_100000_WKRS_EMP':
        unit_parsed = 'PER_100000_WKRS_EMP'
    elif unit == 'P_KM':
        unit_parsed = 'P_KM'
    elif unit == 'Ratio':
        unit_parsed = 'Ratio'
    elif unit == 'TONNES':
        unit_parsed = 'Imperial tonnes'
    elif unit == 'TONNES_M':
        unit_parsed = 'Metric tonnes'
    elif unit == 'T_KM':
        unit_parsed = 'T_KM'
    elif unit == 'T_PER_HA':
        unit_parsed = 'T_PER_HA'
    elif unit == 'mgr/m^3':
        unit_parsed = 'mgr/m^3'
    else:
        unit_parsed = unit

    return unit_parsed


def find(seq, f):
    """Return first item in sequence where f(item) == True."""
    for item in seq:
        if f(item):
            return item
