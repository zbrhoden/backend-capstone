from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    category = models.ManyToManyField("Category", through="Inventory_Category")