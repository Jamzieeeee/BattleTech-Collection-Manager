from django.contrib import admin
from django.urls import path, include
from BTCM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('', views.homepage),
]
