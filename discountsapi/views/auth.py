from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import logging

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    logging.info("password")
    username = request.data['username']
    password = request.data['password']

    logging.warning(request.data)
    # logging.warning(authenticated_user)
    authenticated_user = authenticate(username=username, password=password)
    logging.warning(authenticated_user)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)
        

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):

    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password']
    )

    token = Token.objects.create(user=new_user)

    data = { 'token': token.key }
    return Response(data)
