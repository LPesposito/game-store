from django.urls import path, include
from rest_framework import routers

from product.views import ProductViewSet, CategoryViewSet

router =  routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categorys', CategoryViewSet, basename='categorys')

urlpatterns = [
    path('', include(router.urls)),
]