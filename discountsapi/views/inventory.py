from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from discountsapi.models import Inventory

class InventoryView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        inventories = Inventory.objects.all()

        serializer = InventorySerializer(
            inventories, many=True, context={'request': request})
        return Response(serializer.data)

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('id', 'name', 'price', 'store', 'categories')