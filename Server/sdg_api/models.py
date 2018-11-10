from django.db import models

# Create your models here.
from core.models import CommonModel


class GeoArea(CommonModel):
    code = models.CharField(max_length=300)
    name = models.CharField(max_length=300)

    @staticmethod
    def Poland():
        return GeoArea.objects.get(name='Poland')


class Series(CommonModel):
    goal = models.CharField(max_length=300)
    target = models.CharField(max_length=300)
    indicator = models.CharField(max_length=300)
    code = models.CharField(max_length=300)
    description = models.TextField()
    uri = models.CharField(max_length=300)


class Target(CommonModel):
    goal = models.CharField(max_length=300)
    code = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.TextField()
    uri = models.CharField(max_length=300)


class TargetPivotData(CommonModel):
    goal = models.CharField(max_length=300)
    target = models.CharField(max_length=300)
    indicator = models.CharField(max_length=300)
    series = models.CharField(max_length=300)
    source = models.TextField()
    data = models.TextField()
    sex = models.CharField(max_length=10, null=True)
