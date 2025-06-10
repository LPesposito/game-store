import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from shop_cart.models import Cart

User = get_user_model()

@pytest.fixture
def user(db):
    user = User.objects.create_user(username="cartuser", password="cartpass")
    return user

@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

def test_cart_mine(api_client, user):
    url = reverse('cart-mine')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['user'] == user.id

def test_cart_mine_creates_cart_if_not_exists(api_client, user):
    Cart.objects.filter(user=user).delete()
    url = reverse('cart-mine')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['user'] == user.id
