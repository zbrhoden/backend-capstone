from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=8, decimal_places=2)