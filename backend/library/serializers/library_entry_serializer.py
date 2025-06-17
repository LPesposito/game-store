from rest_framework import serializers
from library.models import LibraryEntry
from product.models import Product
from product.serializers import ProductSerializer  

class LibraryEntrySerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = LibraryEntry
        fields = [
            'id',
            'product',
            'product_detail',
            'acquired_at',
            'access_key',
        ]
        read_only_fields = ['acquired_at', 'access_key']  
