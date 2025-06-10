import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from wallet.models import Wallet
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def user(db):
    user = User.objects.create_user(username="testuser", password="testpass")
    Wallet.objects.create(user=user, balance=100)
    return user

@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

def test_wallet_list(api_client, user):
    url = reverse('wallet-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['balance'] == '100.00'

def test_wallet_add_funds(api_client, user):
    url = reverse('wallet-add-funds')
    data = {'amount': '50.00'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['balance'] == '150.00'

def test_wallet_add_funds_negative(api_client, user):
    url = reverse('wallet-add-funds')
    data = {'amount': '-10.00'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'amount' in response.data
