from rest_framework import serializers
from order.models.order import Order
from product.models.product import Product
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = ['products', 'total', 'user','id']
        read_only_fields = ['total', 'id']  
        

    def create(self, validated_data) -> Order:
        products_data = validated_data.pop('products')
        user = validated_data.pop('user')
        order = Order.objects.create(user=user, **validated_data)
        order.products.set(products_data)  # Associate products with the order
        order.save()  # The total will be calculated in the model's save method
        return order