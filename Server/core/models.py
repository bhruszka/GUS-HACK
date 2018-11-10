from django.contrib.auth.models import AbstractUser
from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    SEX = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    USERNAME_FIELD = 'username'

    sex = models.CharField(max_length=1, choices=SEX, null=True)
    birth_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
