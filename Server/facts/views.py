from django.shortcuts import render

# Create your views here.

import django_filters.rest_framework

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from facts.models import Fact
from facts.serializers import FactSerializer


class FactViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    permission_classes = (permissions.AllowAny,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('goal', 'fact_type')
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def random_facts(request, count):
    facts = Fact.objects.order_by('?')[:count]
    serializer = FactSerializer(facts, many=True)
    return Response(serializer.data)
