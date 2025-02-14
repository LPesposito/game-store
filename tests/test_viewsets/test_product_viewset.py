import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse
from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)  # Autentica o usuário para os testes

        self.product = ProductFactory(
            title='pro controller',
            price=200.00,
        )

        self.product.categories.set([CategoryFactory()])

    def test_get_all_product(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        self.assertEqual(product_data[0]['title'], self.product.title)
        self.assertEqual(product_data[0]['price'], self.product.price)
        self.assertEqual(product_data[0]['active'], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        print(category)
        return
        data = {
            'title': 'notebook',
            'price': 800.00,
            'categories': [{
                'title': category.title,
                'slug': category.slug,
                'description': category.description
            }],
        }

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )

        # Adiciona uma impressão da resposta para depuração
        
        print(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_product = Product.objects.get(title='notebook')
        print(create_product.categories.all())
        self.assertEqual(create_product.title, 'notebook')
        self.assertEqual(create_product.price, 800.00)
        self.assertIn(category, create_product.categories.all())