from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from wallet.models import Wallet
from wallet.serializers import WalletSerializer
from wallet.models import Transaction

class WalletViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=False, methods=['post'], url_path='add-funds')
    def add_funds(self, request):
        wallet = self.get_object()
        amount = request.data.get('amount')

        try:
            amount = float(amount)
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
        wallet = self.get_object()
        amount = request.data.get('amount')

        try:
            amount = float(amount)
        except (ValueError, TypeError):
            return Response({'error': 'Valor inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        if amount <= 0 or amount > wallet.balance:
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
