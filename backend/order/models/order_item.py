from django.db import models
from product.models import Product
from . import Order


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # preço no momento da compra

    def __str__(self):
        return f"{self.quantity}x {self.product.title}"