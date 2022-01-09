from django.db import models


class Order(models.Model):
    date = models.DateTimeField
    total_price = models.DecimalField(max_digits=4, decimal_places=2)
    total_quantity = models.IntegerField
    items = models.JSONField