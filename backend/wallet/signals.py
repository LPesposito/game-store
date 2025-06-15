from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from wallet.models import Wallet

@receiver(post_save, sender=CustomUser)
def create_wallet_for_new_user(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)