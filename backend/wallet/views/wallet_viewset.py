from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from wallet.models import Wallet
from wallet.serializers import WalletSerializer
from wallet.models import Transaction
from decimal import Decimal

class WalletViewSet(viewsets.GenericViewSet):
    swagger_schema_fields = {
        "tags": ["wallet"]
    }
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=False, methods=['post'], url_path='add-funds')
    def add_funds(self, request):
        wallet = Wallet.objects.get(user=request.user)
        amount = request.data.get('amount')

        try:
            amount = Decimal(amount)
        except (ValueError, TypeError):
            return Response({'error': 'Valor inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        if amount <= 0:
            return Response({'error': 'O valor deve ser positivo.'}, status=status.HTTP_400_BAD_REQUEST)

        wallet.balance += amount
        wallet.save()

        
        Transaction.objects.create(
            wallet=wallet,
            transaction_type='deposit',
            amount=amount,
            note='Adição de fundos'
        )

        return Response({'message': 'Fundos adicionados com sucesso.', 'balance': wallet.balance})


    @action(detail=False, methods=['post'], url_path='withdraw')
    def withdraw(self, request):
        wallet = Wallet.objects.get(user=request.user)
        amount = request.data.get('amount')

        try:
            amount = Decimal(str(amount))
        except (ValueError, TypeError):
            return Response({'error': 'Valor inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        if amount <= Decimal(0) or amount > wallet.balance:
            return Response({'error': 'Valor inválido ou saldo insuficiente.'}, status=status.HTTP_400_BAD_REQUEST)

        wallet.balance -= amount
        wallet.save()

       
        Transaction.objects.create(
            wallet=wallet,
            transaction_type='withdraw',
            amount=amount,
            note='Retirada de fundos'
        )

        return Response({'message': 'Fundos retirados com sucesso.', 'balance': wallet.balance})
    
    @action(detail=False, methods=['get'], url_path='balance')
    def balance(self, request):
        wallet = Wallet.objects.get(user=request.user)
        serializer = WalletSerializer(wallet)
        return Response({'balance': serializer.data['balance']}, status=status.HTTP_200_OK)
