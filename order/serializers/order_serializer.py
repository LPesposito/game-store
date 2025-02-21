from rest_framework import serializers
from order.models.order import Order
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = ['product', 'total', 'user']

    def get_total(self, obj):
        total = sum([product.price for product in obj.product.all()])
        return total

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        user = validated_data.pop('user')
        order = Order.objects.create(user=user, **validated_data)
        for product in product_data:
            product_instance, created = Product.objects.get_or_create(**product)
            order.product.add(product_instance)
        return order