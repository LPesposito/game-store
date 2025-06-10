from rest_framework import serializers
from wallet.models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance', 'updated_at']
        read_only_fields = ['updated_at']