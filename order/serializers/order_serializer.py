from rest_framework import serializers

from order.models.order import Order
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.Serializer):
    product = ProductSerializer(required=True ,many=True)
    total = serializers.SerializerMethodField()
    
    def get_total(self, obj):
        total = sum([product.price for product in obj.product.all()])
        return total
    
    class Meta:
        model = Order
        fields=['product','total']
        extra_kwargs = {
            'product': {'required': False}
        }
    
    def create(self, validated_data):
        product_data = validated_data.pop('product_id')
        user_data = validated_data.pop('user')
        
        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)
        
        return order