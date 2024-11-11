# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),  # List and filter items
    path('index/', views.index, name='inventory_index'),
    path('update/<int:item_id>/', views.update_inventory, name='update_inventory'),  # Update item
]

