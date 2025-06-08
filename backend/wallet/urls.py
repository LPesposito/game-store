from rest_framework.routers import DefaultRouter
from wallet.views import WalletViewSet

router = DefaultRouter()
router.register(r'wallet', WalletViewSet, basename='wallet')
urlpatterns = router.urls