from rest_framework import serializers
from order.models import OrderItem
from product.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_detail = serializers.StringRelatedField(source='product', read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_detail',
            'quantity',
            'price',
        ]