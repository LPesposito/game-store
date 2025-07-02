from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import CustomUser
from shop_cart.models import Cart, CartItem
from product.models import Product, Category

class ShopCartViewTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="cartuser", password="pass")
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(title="cat", slug="cat")
        self.product = Product.objects.create(title="prod", price=10, active=True)
        self.product.categories.add(self.category)

    def test_cart_mine(self):
        url = reverse('cart-mine')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.user.id)

    def test_add_cart_item(self):
        url = reverse('cart-items-list')
        data = {"product": self.product.id, "quantity": 2}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['quantity'], 2)
