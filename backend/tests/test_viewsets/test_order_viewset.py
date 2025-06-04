import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.urls import reverse

from tests.factories.product_factories import ProductFactory, CategoryFactory
from tests.factories.order_factories import UserFactory, OrderFactory
from order.models import Order

class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()  
        self.client.force_authenticate(user=self.user)  
        self.product = ProductFactory(categories=[CategoryFactory(title='action')])
        self.product2 = ProductFactory(categories=[CategoryFactory(title='adventure')])  
        self.order = OrderFactory(user=self.user)  
        self.order.products.set([self.product, self.product2])  
        self.order.save()  
        token = Token.objects.create(user=self.user)
        token.save()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        
    def test_order(self):
        response = self.client.get(
            reverse('orders-list', kwargs={'version': 'v1'}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)['results']
        self.assertEqual(order_data[0]['products'][0], self.product.id)
        self.assertEqual(order_data[0]['products'][1], self.product2.id)
        self.assertEqual(order_data[0]['total'], str(self.product.price + self.product2.price) + '.00')

    
    def test_create_order(self):
        data = {
            'user': self.user.id,  
            'products': [self.product.id, self.product2.id],  
        }

        response = self.client.post(
            reverse('orders-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_order = Order.objects.filter(user=self.user, products__in=[self.product, self.product2]).distinct().first()
        self.assertEqual(create_order.total, self.product.price + self.product2.price)
        self.assertIn(self.product, create_order.products.all())
        self.assertIn(self.product2, create_order.products.all())
        
    def test_get_all_orders(self):
        response = self.client.get(
            reverse('orders-list', kwargs={'version': 'v1'}),
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)
        #import pdb; pdb.set_trace()
        self.assertEqual(order_data['results'][0]['id'], self.order.id)
        
    def test_create_order_with_status(self) -> None:
        product1 = ProductFactory(categories=[CategoryFactory(title='action')])
        product2 = ProductFactory(categories=[CategoryFactory(title='adventure')])
        total = product1.price + product2.price
        data = json.dumps({
    
            'user': self.user.id,
            'products': [product1.id, product2.id],
        })
        
        response = self.client.post(
            reverse('orders-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_order = Order.objects.get(total=total)
        self.assertEqual(create_order.total, total)
