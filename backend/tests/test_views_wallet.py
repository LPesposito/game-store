from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import CustomUser
from wallet.models import Wallet

class WalletViewTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="walletuser", password="pass")
        self.wallet = Wallet.objects.create(user=self.user, balance=100)
        self.client.force_authenticate(user=self.user)

    def test_wallet_retrieve(self):
        url = reverse('wallet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['balance']), 100)

    def test_wallet_add_funds(self):
        url = reverse('wallet-add-funds')
        response = self.client.post(url, {'amount': 50})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(float(self.wallet.balance), 150)

    def test_wallet_withdraw(self):
        url = reverse('wallet-withdraw')
        response = self.client.post(url, {'amount': 30})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(float(self.wallet.balance), 70)
