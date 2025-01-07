from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import *
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import RegistrationForm, CatalogueForm
from catalogue.models import Catalogue


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

def create_catalogue(request):
    context = {}

    # add the dictionary during initialization
    form = CatalogueForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "catalogue/create_catalogue.html", context)

def list_catalogue(request):
    context ={}

    # add the dictionary during initialization
    context["dataset"] = Catalogue.objects.all()
        
    return render(request, "catalogue/list_catalogue.html", context)

def detail_catalogue(request, id):
    context ={}

    # add the dictionary during initialization
    context["data"] = Catalogue.objects.get(id = id)
        
    return render(request, "catalogue/detail_catalogue.html", context)

def update_catalogue(request, id):
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Catalogue, id = id)

    # pass the object as instance in form
    form = CatalogueForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect(detail_catalogue, id = id)
    # add form dictionary to context
    context["form"] = form

    return render(request, "catalogue/update_catalogue.html", context)

def delete_catalogue(request, id):
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Catalogue, id = id)


    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return redirect(list_catalogue)

    return render(request, "catalogue/delete_catalogue.html", context)