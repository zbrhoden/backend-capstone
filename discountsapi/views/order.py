from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from discountsapi.models import Order
from rest_framework import status
import logging


class OrderView(ViewSet):

    def create(self, request):
        try:
            logging.info('I told you so')
            order = Order.objects.create(
                order_date= request.data["order_date"],
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
        fields = ('id', 'order_date', 'items')