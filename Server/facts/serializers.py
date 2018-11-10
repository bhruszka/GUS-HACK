from rest_framework import serializers

from facts.models import Fact


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = (
            'id',
            'goal', 'target', 'indicator', 'series', 'source',
            'data', 'min_year', 'max_year', 'oldest_year', 'newest_year',
            'unit', 'unit_parsed', 'content', 'fact_type',
        )
        ordering = ('custom_order',)
