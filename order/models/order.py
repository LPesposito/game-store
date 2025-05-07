from django.db import models

from product.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    products = models.ManyToManyField(Product,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first to get an ID
        self.total = sum(product.price for product in self.products.all())  # Calculate total price
        super().save(update_fields=['total'])  # Save the updated total
