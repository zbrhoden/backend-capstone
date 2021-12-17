from django.contrib import admin
from discountsapi.models import Category, Discount, Inventory_Category, Inventory, Manager, Store

# Register your models here.
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Inventory_Category)
admin.site.register(Inventory)
admin.site.register(Manager)
admin.site.register(Store)