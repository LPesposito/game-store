from rest_framework import status 
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet

from order import models, serializers

class OrderViewSet(ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()