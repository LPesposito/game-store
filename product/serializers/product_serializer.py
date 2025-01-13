from rest_framework import serializers

from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)
    
    class Meta:
        model = Category
        fields = [
                'title',
                'description',
                'price',
                'active',
                'category',
            ]