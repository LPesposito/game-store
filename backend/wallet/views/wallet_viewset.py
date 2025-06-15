from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from wallet.models import Wallet
from wallet.serializers import WalletSerializer

class WalletViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request):
        wallet = Wallet.objects.get(user=request.user)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_funds(self, request):
        amount = request.data.get('amount')
        if not amount:
            return Response({'error': 'Amount is required'}, status=400)

        wallet = Wallet.objects.get(user=request.user)
        wallet.balance += float(amount)
        wallet.save()
        return Response({'message': 'Funds added', 'new_balance': wallet.balance}, status=200)
