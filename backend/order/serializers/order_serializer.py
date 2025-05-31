from rest_framework import serializers
from order.models import Order, OrderItem
from .order_item_serializer import OrderItemSerializer  # se estiver separado
from django.db import transaction


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'created_at',
            'total',
            'items',
        ]
        read_only_fields = ['total', 'id', 'created_at']

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total = 0
        for item_data in items_data:
            price = item_data['price']
            quantity = item_data['quantity']
            total += price * quantity
            OrderItem.objects.create(order=order, **item_data)

        order.total = total
        order.save()

        return order