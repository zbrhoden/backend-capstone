from django.db import models


class Order(models.Model):
    date = models.DateTimeField
    items = models.JSONField