from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from product.models import Product, Category

class ProductViewTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title="cat", slug="cat")

    def test_product_list(self):
        Product.objects.create(title="prod", price=10, active=True)
        url = reverse('products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        url = reverse('products-list')
        data = {
            "title": "prod2",
            "price": 20,
            "categories": [self.category.id],
            "description": "desc"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "prod2")
