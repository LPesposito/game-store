import json 
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from tests.factories.product_factories import ProductFactory, CategoryFactory
from product.models import Product, Category

class CategoryViewSet(APITestCase):
    client = APIClient()
    
    def setUp(self):
        self.category = CategoryFactory(title='games')
        
    def test_get_all_category(self):
        response = self.client.get(
            reverse('categorys-list', kwargs={'version': 'v1'}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)['results'][0]
        self.assertEqual(category_data['title'], self.category.title)
        # Adicione asserts para outros campos obrigatórios do model Category, se houver
        # self.assertEqual(category_data['campo'], self.category.campo)
        
    def test_create_category(self):
        data = json.dumps({
            'title': 'Musica',
        })
        response = self.client.post(
            reverse('categorys-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_category = Category.objects.get(title='Musica')
        self.assertEqual(create_category.title, 'Musica')
        # Adicione asserts para outros campos obrigatórios do model Category, se houver
        # self.assertEqual(create_category.campo, valor_esperado)
