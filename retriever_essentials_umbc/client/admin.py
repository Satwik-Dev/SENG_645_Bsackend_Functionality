# client/admin.py
from django.contrib import admin
from .models import AdminProfile, StudentProfile

admin.site.register(AdminProfile)
admin.site.register(StudentProfile)
