from django.db import models

class Discount(models.Model):
    inventory = models.ForeignKey("Inventory", null=True, blank=True, on_delete=models.CASCADE)
    store = models.ForeignKey ("Store", on_delete=models.CASCADE)
    #category could be i.e. fruit or candy
    category = models.ForeignKey ("Category", null=True, blank=True, on_delete=models.CASCADE)
    day_of_week = models.IntegerField (null=True, blank=True)
    quantity = models.IntegerField( null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=8, decimal_places=8)