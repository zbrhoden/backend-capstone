from django.db import models

class Inventory_Category(models.Model):
    inventory = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)