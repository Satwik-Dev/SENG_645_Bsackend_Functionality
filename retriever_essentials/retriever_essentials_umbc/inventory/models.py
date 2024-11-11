from django.db import models

# inventory/models.py stores search fields in item classification
class ItemClassification(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Type of inventory item (e.g., Food, Hygiene)")
    
    def __str__(self):
        return self.name

# inventory/models.py
#classification: Links each item to an ItemClassification, helping with categorization.
#name: The name of the item (e.g., "Apple", "Soap").
#quantity: Tracks the current stock of the item.
#expiry_date: An optional field for items with an expiration date.
#barcode: Stores a unique identifier for the item, often used for scanning.
#availability: Indicates if the item is in stock or out of stock.
#Usage: This model will be the core of the inventory tracking system, allowing administrators to add, update, and track items.
class Item(models.Model):
    classification = models.ForeignKey(ItemClassification, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    expiry_date = models.DateField(null=True, blank=True)
    barcode = models.CharField(max_length=50, unique=True)
    availability = models.CharField(
        max_length=20,
        choices=[('in-stock', 'In Stock'), ('out-of-stock', 'Out of Stock')]
    )

    def __str__(self):
        return self.name
