from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from order import models, serializers

class OrderViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]    

    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all().order_by('id')