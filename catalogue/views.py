from django.shortcuts import render

# Create your views here.
def catalogue(request):
    return render(request, 'catalogue/catalogue.html')