from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from discountsapi.models import Order

class OrderView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        orders = Order.objects.all()

        serializer = OrderSerializer(
            orders, many=True, context={'request': request})
        return Response(serializer.data)

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'date', 'total_price', 'total_quantity', 'items')