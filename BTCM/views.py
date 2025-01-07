from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import RegistrationForm


def homepage(request):
    # return HttpResponse('Homepage')
    return render(request, 'homepage.html')

def catalogue(request):
    return render(request, 'catalogue/catalogue.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            group = Group.objects.get(name='Collectors')
            user.groups.add(group) 
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})