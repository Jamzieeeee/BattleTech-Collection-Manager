from django.urls import path, include
from BTCM import views

urlpatterns = [
    path('', views.catalogue),
]
