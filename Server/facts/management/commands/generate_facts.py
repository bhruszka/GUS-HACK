import json
import logging
import random

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


def pivot_data_get_value(p):
    return p['value']


def pivot_data_get_year(data):
    return int(json.loads(data['year'])[0])


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        from sdg_api.models import TargetPivotData
        from facts.models import Fact
        from facts.utils import unit_parser

        units = set()

        Fact.objects.all().delete()

        fact_model_list = []

        order = random.sample(range(1, TargetPivotData.objects.count() + 1), TargetPivotData.objects.count())

        for i, target_pivot_data in enumerate(TargetPivotData.objects.all()):
            # target = Target.objects.
            data = json.loads(target_pivot_data.data)
            data_with_value = [d for d in data if pivot_data_get_value(d) != '']

            for year_data in data_with_value:
                year_data['year'] = pivot_data_get_year(year_data)

            min_val = min(data_with_value, key=pivot_data_get_value)
            max_val = max(data_with_value, key=pivot_data_get_value)
            oldest_val = data_with_value[0]
            newest_val = data_with_value[-1]

            # print("Min: {}, Max: {}, Newest: {}".format(min_val, max_val, newest_val))
            unit = newest_val['Units']
            units.add(unit)

            fact_type = ''
            if oldest_val != newest_val:
                fact_type = 'new_old'
            else:
                fact_type = 'one_point'

            fact_model_list.append(Fact(
                goal=target_pivot_data.goal,
                target=target_pivot_data.target,
                indicator=target_pivot_data.indicator,
                series=target_pivot_data.series,
                source=target_pivot_data.source,
                data=json.dumps(data_with_value),
                sex=target_pivot_data.sex,

                min_year=min_val['year'],
                max_year=max_val['year'],

                oldest_year=oldest_val['year'],
                newest_year=newest_val['year'],

                unit=unit,
                unit_parsed=unit_parser(unit),

                fact_type=fact_type,
                custom_order=order[i],

                love=random.randint(0, 1000),
                sad=random.randint(0, 1000),
                alert=random.randint(0, 1000),
                edu=random.randint(0, 1000),
            ))

        Fact.objects.bulk_create(fact_model_list)

        # print(unit_dict.keys())
        print(len(units))
        for unit in sorted(units):
            print(unit)
