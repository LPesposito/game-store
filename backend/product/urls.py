from django.urls import path, include
from rest_framework import routers

from product import viewsets

router =  routers.SimpleRouter()
router.register(r'products', viewsets.ProductViewSet, basename='products')
router.register(r'categorys', viewsets.CategoryViewSet, basename='categorys')

urlpatterns = [
    path('', include(router.urls)),
]