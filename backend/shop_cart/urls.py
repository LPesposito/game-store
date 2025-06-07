from rest_framework.routers import DefaultRouter
from shop_cart.viewsets import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls