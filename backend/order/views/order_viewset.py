from rest_framework import mixins, viewsets
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as drf_status
from library.models import LibraryEntry

class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    swagger_schema_fields = {"tags": ["Order"]}
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .order_by('-created_at')
        )

    @action(detail=True, methods=['post'], url_path='confirm')
    def confirm(self, request, pk=None):
        order = self.get_object()
        user = request.user

        if order.status != 'pending':
            return Response({'detail': 'Pedido já processado.'}, status=drf_status.HTTP_400_BAD_REQUEST)

        wallet = getattr(user, 'wallet', None)
        if wallet is None or wallet.balance < order.total:
            return Response({'detail': 'Saldo insuficiente.'}, status=drf_status.HTTP_400_BAD_REQUEST)

    
        wallet.balance -= order.total
        wallet.save()

        order.status = 'paid'
        order.save()

        for item in order.items.all():
            LibraryEntry.objects.get_or_create(user=user, product=item.product)

        return Response({'detail': 'Compra confirmada e acesso liberado.'}, status=drf_status.HTTP_200_OK)
