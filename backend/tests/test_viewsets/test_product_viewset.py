import json 
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from tests.factories.product_factories import ProductFactory, CategoryFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    client = APIClient()
    
    def setUp(self):
        self.product = ProductFactory(
            title='pro controller',
            price=200.00,
        )
        
    def test_get_all_product(self):
        response = self.client.get(
            reverse('products-list', kwargs={'version': 'v1'}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)
        self.assertEqual(product_data['results'][0]['title'], self.product.title)
        self.assertEqual(product_data['results'][0]['price'], float(self.product.price))
        self.assertEqual(product_data['results'][0]['active'], self.product.active)
        # Adicione asserts para outros campos obrigatórios do model Product, se houver
        # self.assertEqual(product_data['results'][0]['campo'], self.product.campo)
        
    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps({
            'title': 'notebook',
            'price': 800.00,
            'categories': [{'title': category.title}],
        })
        response = self.client.post(
            reverse('products-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_product = Product.objects.get(title='notebook')
        self.assertEqual(create_product.title, 'notebook')
        self.assertEqual(create_product.price, 800.00)
        # Adicione asserts para outros campos obrigatórios do model Product, se houver
        # self.assertEqual(create_product.campo, valor_esperado)