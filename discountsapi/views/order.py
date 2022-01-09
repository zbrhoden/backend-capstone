from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from discountsapi.models import Order
from rest_framework import status

class OrderView(ViewSet):

    def create(self, request):
        try:

            order = Order.objects.create(
                date= request.data["day_of_week"],
                total_price= request.data["total_price"],
                total_quantity= request.data["total_quantity"],
                items= request.data["items"]
            )
            serializer = OrderSerializer(order, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

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