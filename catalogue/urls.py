from django.urls import path, include
from BTCM import views

urlpatterns = [
    path('catalogue/create/', views.create_catalogue),
    path('catalogue/list/', views.list_catalogue, name='list_catalogue'),
    path('catalogue/detail/<id>', views.detail_catalogue),
    path('catalogue/update/<id>', views.update_catalogue),
    path('catalogue/delete/<id>', views.delete_catalogue),
    path('collection/create/', views.create_collection),
    path('collection/list/', views.list_collection, name='list_collection'),
    path('collection/detail/<id>', views.detail_collection),
    path('collection/update/<id>', views.update_collection),
    path('collection/delete/<id>', views.delete_collection),
]
