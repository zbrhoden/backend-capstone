from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from discountsapi.models import Store

class StoreView(ViewSet):
    def create(self, request):

        try:

            store = Store.objects.create(
                name=request.data["name"]
            )
            serializer = StoreSerializer(store, context={'request': request})
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
            store = Store.objects.get(pk=pk)
            
            
            # event = Event.objects.get(pk=pk)
            serializer = StoreSerializer(store, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message', 'Storet Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        try:
            store = Store.objects.get(pk=pk)
            store.delete()

            return Response({"message": "Store deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Store.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        stores = Store.objects.all()

        serializer = StoreSerializer(
            stores, many=True, context={'request': request})
        return Response(serializer.data)

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name')
        depth = 1