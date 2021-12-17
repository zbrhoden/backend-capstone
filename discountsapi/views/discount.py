from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from discountsapi.models import Discount, Manager, Category

class DiscountView(ViewSet):
    def create(self, request):
 

        category = Category.objects.get(pk=request.data["CategoriesId"])

        try:

            discount = Discount.objects.create(
                item=request.data["item"],
                store=request.data["store"],
                start_date=request.data["start_date"],
                end_date=request.data["end_date"],
                category=category
            )
            serializer = DiscountSerializer(discount, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        manager = Manager.objects.get(user=request.auth.user)

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        discount = Discount.objects.get(pk=pk)
        


        discount.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
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
        fields = ('id', 'item', 'store', 'category', 'start_date', 'end_date')
        depth = 1