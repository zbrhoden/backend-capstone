from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from discountsapi.models import Discount, Category, Inventory, Store

class DiscountView(ViewSet):
    def create(self, request):

        category = Category.objects.get(pk=request.data["category"])
        inventory = Inventory.objects.get(pk=request.data["inventory"])
        store = Store.objects.get(pk=request.data["store"])

        try:

            discount = Discount.objects.create(
                inventory=inventory,
                store=store, 
                day_of_week=request.data["day_of_week"],
                quantity=request.data["quantity"],
                discount_percentage=request.data["discount_percentage"],
                category=category
            )
            serializer = DiscountSerializer(discount, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as ex:
            return HttpResponseServerError(ex)


    def retrieve(self, request, pk=None):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/events/2
            #
            # The `2` at the end of the route becomes `pk`
            discount = Discount.objects.get(pk=pk)
            
            
            # event = Event.objects.get(pk=pk)
            serializer = DiscountSerializer(discount, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message', 'Discount Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        category = Category.objects.get(pk=request.data["category"])
        inventory = Inventory.objects.get(pk=request.data["inventory"])
        store = Store.objects.get(pk=request.data["store"])

        discount = Discount.objects.get(pk=pk)
        
        discount.inventory = inventory
        discount.store = store
        discount.category = category
        discount.day_of_week = request.data["day_of_week"]
        discount.quantity = request.data["quantity"]
        discount.discount_percentage = request.data["discount_percentage"]

        discount.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)



    def destroy(self, request, pk=None):

        try:
            discount = Discount.objects.get(pk=pk)
            discount.delete()

            return Response({"message": "Discount deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Discount.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        discounts = Discount.objects.all()

        serializer = DiscountSerializer(
            discounts, many=True, context={'request': request})
        return Response(serializer.data)

class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'inventory', 'store', 'category', 'day_of_week', 'quantity', 'discount_percentage')
        depth = 1