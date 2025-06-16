from django.db import models
from user.models import CustomUser as User
from product.models import Product
from django.utils import timezone


class LibraryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="library")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="in_libraries")
    acquired_at = models.DateTimeField(default=timezone.now)
    access_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ['user', 'product']  # Evita jogos duplicados na biblioteca

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
