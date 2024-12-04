# inventory/admin.py
from django.contrib import admin
from .models import ItemClassification, Item

admin.site.register(ItemClassification)
admin.site.register(Item)
