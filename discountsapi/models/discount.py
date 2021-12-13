from django.db import models

class Discount(models.Model):
    item = models.ForeignKey("Item", null=True, blank=True, on_delete=models.CASCADE)
    store = models.ForeignKey ("Store", on_delete=models.CASCADE)
    category = models.ForeignKey ("Category", null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()