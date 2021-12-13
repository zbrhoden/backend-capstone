from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from django.db.models import Count, Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from discountsapi.models import Item

class ItemView(ViewSet):
    