from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from core.forms import NewUserForm


def sign_up(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = NewUserForm()
    return render(request, 'registration/signup.html', {'form': form})