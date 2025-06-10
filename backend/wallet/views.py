from rest_framework import generics, permissions
from wallet.models import Wallet
from wallet.serializers import WalletSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from decimal import Decimal

class WalletDetailView(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.wallet


class WalletAddFundsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        amount = request.data.get("amount")
        if not amount:
            return Response({"error": "Amount is required"}, status=400)
        
        try:
            amount = Decimal(amount)
            if amount <= 0:
                raise ValueError
        except:
            return Response({"error": "Invalid amount"}, status=400)

        wallet = request.user.wallet
        wallet.balance += amount
        wallet.save()

        return Response({"message": "Funds added successfully", "balance": wallet.balance})