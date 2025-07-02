from rest_framework import serializers
from shop_cart.models import Cart
from .cart_item_serializer import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total', 'created_at']
        read_only_fields = ['total', 'created_at']

    def get_total(self, obj):
        return obj.total()