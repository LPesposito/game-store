from rest_framework import serializers

from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.Serializer):
    product = ProductSerializer(required=True ,many=True)
    total = serializers.SerializerMethodField()
    
    def get_total(self, obj):
        total = sum([product.price for product in obj.product.all()])
        return total
    
    class Meta:
        model = Product
        fields=['product','total']