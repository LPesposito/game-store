from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import CustomUser
from order.models import Order
from product.models import Product, Category
from library.models import LibraryEntry

class OrderViewTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="orderuser", password="pass")
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(title="cat", slug="cat")
        self.product = Product.objects.create(title="prod", price=10, active=True)
        self.product.categories.add(self.category)

    def test_order_list(self):
        Order.objects.create(user=self.user)
        url = reverse('orders-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        url = reverse('orders-list')
        data = {
            "items": [
                {"product": self.product.id, "quantity": 2, "price": 10}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['items'][0]['product'], self.product.id)

        self.assertEqual(LibraryEntry.objects.count(), 0)
