from django.urls import path
from .views import WalletDetailView, WalletAddFundsView

urlpatterns = [
    path('', WalletDetailView.as_view(), name='wallet-detail'),
    path('add/', WalletAddFundsView.as_view(), name='wallet-add-funds'),
]