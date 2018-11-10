# Create your models here.
import json

from core.models import CommonModel
from django.db import models

from facts.utils import find, lowerize_first_word
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

    custom_order = models.IntegerField(null=True)

    FACT_TYPES = (('new_old', 'new_old'), ('one_point', 'one_point'),)

    fact_type = models.CharField(max_length=10, choices=FACT_TYPES, default='one_point')

    @property
    def target_model(self):
        return Target.objects.get(code=self.target)

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
        data = self.data_json

        oldest_data = self.get_year_value(self.oldest_year, data=data)
        newest_data = self.get_year_value(self.newest_year, data=data)

        content = ''

        if self.fact_type == 'new_old':
            new_old_content_template = 'The {fact_description} in Poland has changed from {old_value} in {old_year}' \
                                       'to {new_value} in {new_year}.'

            content = new_old_content_template.format(
                fact_description=lowerize_first_word(self.series_model.description),

                old_value=oldest_data['value'], old_year=self.oldest_year,

                new_value=newest_data['value'], new_year=self.newest_year, )
        else:
            one_point_content_template = 'The UN aims to {target}. In {year}, Poland has achieved {value} ({series}).'

            content = one_point_content_template.format(target=lowerize_first_word(self.target_model.title),
                year=self.newest_year, value=newest_data['value'],
                series=lowerize_first_word(self.series_model.description), )

        return content

    class Meta:
        ordering = ('custom_order',)
