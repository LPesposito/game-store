import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from tests.factories.product_factories import ProductFactory, CategoryFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(
            title='pro controller',
            price=200,
            categories=[self.category]
        )

    def test_get_all_product(self):
        response = self.client.get(
            reverse('products-list', kwargs={'version': 'v1'}),
        )
        if response.status_code != status.HTTP_200_OK:
            print("test_get_all_product response:", response.status_code, response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)
        result = product_data['results'][0]
        self.assertEqual(result['title'], self.product.title)
        self.assertEqual(result['price'], self.product.price)
        self.assertEqual(result['active'], self.product.active)
        # O campo de leitura é categories_detail
        categories_detail = result['categories_detail']
        self.assertTrue(any(cat['title'] == self.category.title for cat in categories_detail))
        self.assertEqual(result['description'], self.product.description)
        self.assertIn('images', result)

    def test_create_product(self):
        category = CategoryFactory()
        data = {
            'title': 'notebook',
            'price': 800,
            'categories': [category.id],
            'description': 'desc test'
        }
        response = self.client.post(
            reverse('products-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_product response:", response.status_code, response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_product = Product.objects.get(title='notebook')
        self.assertEqual(create_product.title, 'notebook')
        self.assertEqual(create_product.price, 800)
        self.assertIn(category, create_product.categories.all())
        self.assertEqual(create_product.description, 'desc test')
        self.assertTrue(create_product.active)