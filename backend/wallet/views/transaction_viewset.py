from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from wallet.models import Transaction
from wallet.serializers.transaction_serializer import TransactionSerializer

class TransactionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Pega as transações da carteira do usuário logado
        return Transaction.objects.filter(wallet__user=self.request.user).order_by('-timestamp')

    def perform_create(self, serializer):
        wallet = self.request.user.wallet
        serializer.save(wallet=wallet)

