import datetime

from django.contrib.auth import get_user_model
from django.forms import ModelForm, DateField, widgets

from core.models import CustomUser


class NewUserForm(ModelForm):
    birth_date = DateField(widget=widgets.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)

    class Meta:
        model = get_user_model()
        fields = '__all__'
