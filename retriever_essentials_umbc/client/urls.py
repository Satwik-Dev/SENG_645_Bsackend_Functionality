# client/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='client_index'),
     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
]
