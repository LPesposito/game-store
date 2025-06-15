from rest_framework import serializers
from wallet.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'wallet',
            'transaction_type',
            'amount',
            'timestamp',
            'note'
        ]
        read_only_fields = ['id', 'timestamp', 'wallet']
