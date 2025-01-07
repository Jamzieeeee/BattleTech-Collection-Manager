from django.urls import path, include
from BTCM import views

urlpatterns = [
    path('catalogue/create/', views.create_catalogue),
    path('catalogue/list/', views.list_catalogue),
    path('catalogue/detail/<id>', views.detail_catalogue),
    path('catalogue/update/<id>', views.update_catalogue),
    path('catalogue/delete/<id>', views.delete_catalogue),

]
