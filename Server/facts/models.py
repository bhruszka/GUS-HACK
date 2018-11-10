# Create your models here.
import json

from core.models import CommonModel
from django.db import models

from facts.utils import find
from sdg_api.models import Target, Series


class Fact(CommonModel):
    goal = models.CharField(max_length=300)
    target = models.CharField(max_length=300)
    indicator = models.CharField(max_length=300)
    series = models.CharField(max_length=300)
    source = models.TextField()
    data = models.TextField()

    min_year = models.IntegerField(null=True)
    max_year = models.IntegerField(null=True)

    oldest_year = models.IntegerField(null=True)
    newest_year = models.IntegerField(null=True)

    unit = models.CharField(max_length=300, default='')
    unit_parsed = models.CharField(max_length=300, default='')

    @property
    def target_model(self):
        return Target.objects.get(target=self.target)

    @property
    def series_model(self):
        return Series.objects.get(code=self.series)

    @property
    def data_json(self):
        return json.loads(self.data)

    def get_year_value(self, year, data=None):
        data = data or self.data_json
        return find(data, lambda d: d['year'] == year)

    @property
    def content(self):
        content_template = 'The {fact_description} in Poland has changed from {old_value} in {old_year} to ' \
                           '{new_value} in {new_year}.'

        data = self.data_json

        oldest_data = self.get_year_value(self.oldest_year, data=data)
        newest_data = self.get_year_value(self.newest_year, data=data)

        return content_template.format(
            fact_description=self.series_model.description,

            old_value=oldest_data['value'],
            old_year=self.oldest_year,

            new_value=newest_data['value'],
            new_year=self.newest_year,
        )
