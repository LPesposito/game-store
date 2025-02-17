from rest_framework import serializers
from product.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
        ]
        extra_kwargs = {'slug':{'required':False}}  