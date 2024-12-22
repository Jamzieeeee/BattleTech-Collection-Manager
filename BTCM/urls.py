from django.contrib import admin
from django.urls import path, include
from BTCM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogue/', include('catalogue.urls')),
    path('', views.homepage),
]
