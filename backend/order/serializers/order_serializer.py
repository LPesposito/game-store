from rest_framework import serializers
from order.models import Order, OrderItem
from .order_item_serializer import OrderItemSerializer
from django.db import transaction


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'created_at',
            'total',
            'items',
            'user',
            'status',  
        ]
        read_only_fields = ['total', 'id', 'created_at', 'user', 'status']

    @transaction.atomic
    def create(self, validated_data):
        request = self.context['request']
        user = request.user  

        items_data = validated_data.pop('items')
        order = Order.objects.create(user=user, **validated_data)

        total = 0
        for item_data in items_data:
            price = item_data['price']
            quantity = item_data['quantity']
            total += price * quantity
            OrderItem.objects.create(order=order, **item_data)

        order.total = total
        order.save()

        return order