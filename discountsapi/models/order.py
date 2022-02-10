from django.db import models


class Order(models.Model):
    order_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_quantity = models.IntegerField(blank=True, null=True)