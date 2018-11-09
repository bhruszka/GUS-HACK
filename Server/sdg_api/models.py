from django.db import models

# Create your models here.
from core.models import CommonModel


class Series(CommonModel):
    goal = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    indicator = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.TextField()
    uri = models.CharField(max_length=50)

