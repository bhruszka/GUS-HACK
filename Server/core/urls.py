from django.urls import path

from . import views

urlpatterns = [
    path('accounts/signup', views.sign_up, name='signup'),
]
