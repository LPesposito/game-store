from django.db import models
from user.models import CustomUser
from product.models import Product
import secrets

class LibraryEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='library_entries')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    acquired_at = models.DateTimeField(auto_now_add=True)
    access_key = models.CharField(max_length=64, unique=True, blank=True)

    class Meta:
        unique_together = ('user', 'product')

    def save(self, *args, **kwargs):
        if not self.access_key:
            self.access_key = secrets.token_hex(32)
        super().save(*args, **kwargs)
