from django.db import models

from product.models.product import Product
from django.contrib.auth.models import User


class Oder(models.Model):
    product = models.ManyToManyField(Product,blank=False)
    user = models.ForeignKey(User, null=False)
    