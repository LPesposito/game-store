from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self): #type: ignore
        return Product.objects.all().order_by('id')
    
    class Meta:
        ordering = ['id']
    
    swagger_schema_fields = {
        "tags": ["product"]
    }