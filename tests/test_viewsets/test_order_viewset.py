import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory, OrderFactory
from order.models import Order

class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()  # Create a user
        self.client.force_authenticate(user=self.user)  # Authenticate the test client
        self.product = ProductFactory(categories=[CategoryFactory(title='action')])
        self.order = OrderFactory(user=self.user, products=[self.product])  # Associate the order with the user
        token = Token.objects.create(user=self.user)
        token.save()
        
        
    def test_order(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)['results']
        self.assertEqual(order_data[0]['products'][0][0], self.product.id)  
        self.assertEqual(order_data[0]['total'], str(self.product.price)+'.00')

    
    def test_create_order(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        data = {
            'user': self.user.id,  # Envia o ID do usuário
            'products': [self.product.id],  # Envia uma lista de IDs de produtos
        }

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )

        print(response.content)  # Para depuração

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_order = Order.objects.get(user=self.user)
        self.assertEqual(create_order.total, self.product.price)
        self.assertIn(self.product, create_order.product.all())
