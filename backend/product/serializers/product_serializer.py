from rest_framework import serializers
from product.models import Product, Category
from .category_serializer import CategorySerializer
from .product_image_serializer import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # Puxa as imagens via related_name
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True
    )
    categories_detail = CategorySerializer(
        source='categories',
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'active',
            'categories',         # IDs para escrita
            'categories_detail',  # Dados completos para leitura
            'images'              # Lista de imagens do produto
        ]