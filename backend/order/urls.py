from rest_framework.routers import DefaultRouter
from order.viewsets import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls