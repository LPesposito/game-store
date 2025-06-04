from rest_framework import serializers
from shop_cart.models import CartItem
from product.serializers.product_serializer import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_detail', 'quantity', 'subtotal']
        read_only_fields = ['subtotal']

    def get_subtotal(self, obj):
        return obj.subtotal()