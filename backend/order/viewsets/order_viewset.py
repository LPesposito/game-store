from rest_framework import mixins, viewsets
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .order_by('-created_at')
        )