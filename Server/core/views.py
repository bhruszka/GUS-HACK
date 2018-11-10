import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.forms import NewUserForm
from core.serializers import UserSerializer


def sign_up(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['date_joined'] = datetime.date.today()
        data['last_login'] = datetime.datetime.now()
        # data['password'] = data['password1']
        form = NewUserForm(data)
        print("ERRORS")
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = NewUserForm()
    return render(request, 'registration/signup.html', {'form': form})


@api_view()
@login_required
def me(request):
    serializer = UserSerializer(request.user)
    print(serializer.data)
    return Response(serializer.data)
