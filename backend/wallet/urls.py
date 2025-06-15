from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wallet.views import WalletViewSet
from wallet.views import TransactionViewSet

router = DefaultRouter()
router.register(r'', WalletViewSet, basename='wallet')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
]
