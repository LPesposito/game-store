from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from wallet.models import Wallet
from wallet.serializers import WalletSerializer, WalletDepositSerializer


class WalletViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        wallet = request.user.wallet
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def deposit(self, request):
        serializer = WalletDepositSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            wallet = request.user.wallet
            wallet.balance += amount
            wallet.save()
            return Response(WalletSerializer(wallet).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)