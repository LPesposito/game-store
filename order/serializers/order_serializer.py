from rest_framework import serializers
from order.models.order import Order
from product.models.product import Product
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = ['products', 'total', 'user']

    def create(self, validated_data):
        products_data = validated_data.pop('product')  # IDs dos produtos
        user = validated_data.pop('user')
        order = Order.objects.create(user=user, **validated_data)
        order.product.set(products_data)  # Associa os produtos ao pedido
        return order