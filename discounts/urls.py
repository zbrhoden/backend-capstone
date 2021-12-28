from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from discountsapi.views import register_user, login_user
from rest_framework import routers
from discountsapi.views import DiscountView, InventoryView, CategoryView, StoreView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'discount', DiscountView, 'discount')
router.register(r'inventory', InventoryView, 'inventory')
router.register(r'category', CategoryView, 'category')
router.register(r'store', StoreView, 'store')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
