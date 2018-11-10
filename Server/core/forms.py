import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, DateField, widgets, CharField, PasswordInput

from core.models import CustomUser


class NewUserForm(UserCreationForm):
    birth_date = DateField(widget=widgets.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)

    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2", "birth_date", "sex")