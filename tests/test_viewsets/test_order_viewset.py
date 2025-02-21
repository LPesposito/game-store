import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory
from order.models import Order

class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)  # Autentica o usuário para os testes

    def test_create_order(self):
        user = UserFactory()
        category = CategoryFactory()
        product = ProductFactory(categories=[category])
        data = {
            'product': [{
                'title': product.title,
                'description': product.description,
                'price': product.price,
            }],  # Enviando os dados do produto
            'total': product.price,  # Enviando o preço total
            'user': user.id  # Enviando o ID do usuário
        }

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )

        # Adiciona uma impressão da resposta para depuração
        print(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_order = Order.objects.get(user=user)
        self.assertEqual(create_order.total, product.price)
        self.assertIn(product, create_order.product.all())