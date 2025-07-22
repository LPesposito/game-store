from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.product_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    
    serializer_class = CategorySerializer
    
    def get_queryset(self): # type: ignore
        return Category.objects.all().order_by('title')
    
    swagger_schema_fields = {
        "tags": ["product"]
    }