import json 
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from tests.factories.product_factories import CategoryFactory
from product.models import Category

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
        self.assertEqual(category_data['slug'], self.category.slug)
        self.assertEqual(category_data['description'], self.category.description)
        
    def test_create_category(self):
        data = {
            'title': 'Musica',
            'slug': 'musica',
            'description': 'Categoria de música'
        }
        response = self.client.post(
            reverse('categorys-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_category = Category.objects.get(title='Musica')
        self.assertEqual(create_category.title, 'Musica')
        self.assertEqual(create_category.slug, 'musica')
        self.assertEqual(create_category.description, 'Categoria de música')
