from django.db import models
from wallet.models import Wallet

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Depósito'),
        ('withdraw', 'Saque'),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type.title()} de R${self.amount} em {self.timestamp.strftime('%d/%m/%Y %H:%M')}"
