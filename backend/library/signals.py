from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order
from library.models import LibraryEntry

@receiver(post_save, sender=Order)
def create_library_entry(sender, instance, created, **kwargs):
    if created:
        for item in instance.items.all():
            LibraryEntry.objects.get_or_create(
                user=instance.user,
                product=item.product,
                defaults={'access_key': None}  # access_key will be generated in the LibraryEntry model's save method
            )