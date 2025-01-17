from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import *
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.contrib import messages

from catalogue.models import Catalogue, Collection
from .forms import (RegistrationForm, CatalogueForm, AddCollectionForm,
UpdateCollectionForm)


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
            # Add all new users to the 'Collectors' group
            group = Group.objects.get(name='Collectors')
            user.groups.add(group)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})


# CATALOGUE
def create_catalogue(request):
    context = {}

    form = CatalogueForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item added to catalogue')

    context['form'] = form
    return render(request, "catalogue/create_catalogue.html", context)


def list_catalogue(request):
    context = {}

    # Sort by baseid as a string, not ideal
    catalogue_list = Catalogue.objects.all().order_by('baseid')
    paginator = Paginator(catalogue_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "catalogue/list_catalogue.html",
                  {"page_obj": page_obj})


def detail_catalogue(request, id):
    context = {}

    context["data"] = Catalogue.objects.get(id=id)

    return render(request, "catalogue/detail_catalogue.html", context)


def update_catalogue(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Catalogue, id=id)

    # pass the object as instance in form
    form = CatalogueForm(request.POST or None, request.FILES or None,
                         instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Item updated in catalogue')
        return redirect(detail_catalogue, id=id)
    # add form dictionary to context
    context["form"] = form

    return render(request, "catalogue/update_catalogue.html", context)


def delete_catalogue(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Catalogue, id=id)
    context['object'] = obj

    if request.method == "POST":
        # delete object
        obj.delete()
        messages.success(request, 'Item deleted from catalogue')
        # after deleting redirect to
        # home page
        return redirect(list_catalogue)

    return render(request, "catalogue/delete_catalogue.html", context)


# COLLECTION
def create_collection(request):
    context = {}

    # Form contains ID of Catalogue entry as hidden field
    form = AddCollectionForm(request.POST or None)
    if form.is_valid():
        collection = form.save(commit=False)
        # Add to current user's collection
        collection.owner = request.user
        collection.save()
        messages.success(request, 'Item added to collection')
        # Take user to update page to add notes etc
        return redirect(update_collection, collection.id)

    context['form'] = form
    return render(request, "collection/create_collection.html", context)


def list_collection(request):
    context = {}

    # Only show current user's collection items
    collection_list = Collection.objects.filter(owner=request.user.id)
    paginator = Paginator(collection_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "collection/list_collection.html",
                  {"page_obj": page_obj})


def detail_collection(request, id):
    context = {}

    context["data"] = Collection.objects.get(id=id)

    return render(request, "collection/detail_collection.html", context)


def update_collection(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Collection, id=id)

    # pass the object as instance in form
    form = UpdateCollectionForm(request.POST or None, request.FILES or None,
                                instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Item modified in collection')
        return redirect(detail_collection, id=id)
    # add form dictionary to context
    context["form"] = form

    return render(request, "collection/update_collection.html", context)


def delete_collection(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Collection, id=id)
    context['object'] = obj

    if request.method == "POST":
        # delete object
        obj.delete()
        messages.success(request, 'Item deleted from collection')
        # after deleting redirect to
        # home page
        return redirect(list_collection)

    return render(request, "collection/delete_collection.html", context)
