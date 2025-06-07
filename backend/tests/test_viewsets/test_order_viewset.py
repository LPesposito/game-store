import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from tests.factories.product_factories import ProductFactory, CategoryFactory
from tests.factories.order_factories import UserFactory
from order.models import Order, OrderItem

class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.product = ProductFactory(categories=[CategoryFactory(title='action')], price=100)
        self.product2 = ProductFactory(categories=[CategoryFactory(title='adventure')], price=200)
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.order = Order.objects.create(user=self.user)
        OrderItem.objects.create(order=self.order, product=self.product, quantity=1, price=self.product.price)
        OrderItem.objects.create(order=self.order, product=self.product2, quantity=2, price=self.product2.price)
        self.order.total = self.product.price * 1 + self.product2.price * 2
        self.order.save()

    def test_order(self):
        response = self.client.get(
            reverse('orders-list', kwargs={'version': 'v1'}),
        )
        if response.status_code != status.HTTP_200_OK:
            print("test_order response:", response.status_code, response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)['results'][0]
        self.assertEqual(order_data['id'], self.order.id)
        # total é string decimal no serializer
        self.assertEqual(str(order_data['total']), f"{self.order.total:.2f}")
        items = order_data['items']
        self.assertEqual(len(items), 2)
        ids = [item['product'] for item in items]
        self.assertIn(self.product.id, ids)
        self.assertIn(self.product2.id, ids)
        for item in items:
            if item['product'] == self.product.id:
                self.assertEqual(item['quantity'], 1)
                self.assertEqual(float(item['price']), float(self.product.price))
            if item['product'] == self.product2.id:
                self.assertEqual(item['quantity'], 2)
                self.assertEqual(float(item['price']), float(self.product2.price))

    def test_create_order(self):
        data = {
            'items': [
                {'product': self.product.id, 'quantity': 1, 'price': float(self.product.price)},
                {'product': self.product2.id, 'quantity': 2, 'price': float(self.product2.price)}
            ]
        }
        # Garante que user não está no payload
        self.assertNotIn('user', data)
        response = self.client.post(
            reverse('orders-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_order response:", response.status_code, response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.latest('id')
        self.assertEqual(created_order.user, self.user)
        self.assertEqual(float(created_order.total), self.product.price * 1 + self.product2.price * 2)
        items = created_order.items.all()
        self.assertEqual(items.count(), 2)
        products = [item.product for item in items]
        self.assertIn(self.product, products)
        self.assertIn(self.product2, products)

    def test_order_list_pagination(self):
        # Create multiple orders for pagination
        for i in range(10):
            order = Order.objects.create(user=self.user)
            OrderItem.objects.create(order=order, product=self.product, quantity=1, price=self.product.price)
            order.total = self.product.price
            order.save()
        response = self.client.get(
            reverse('orders-list', kwargs={'version': 'v1'}),
            {'page': 1, 'page_size': 5}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertIn('results', data)
        self.assertLessEqual(len(data['results']), 5)

    def test_order_list_only_user_orders(self):
        # Create an order for another user
        other_user = UserFactory()
        other_order = Order.objects.create(user=other_user)
        OrderItem.objects.create(order=other_order, product=self.product, quantity=1, price=self.product.price)
        response = self.client.get(
            reverse('orders-list', kwargs={'version': 'v1'}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        for order in data['results']:
            print(order)
            self.assertEqual(order['user'], self.user.id)

    def test_retrieve_order(self):
        response = self.client.get(
            reverse('orders-detail', kwargs={'version': 'v1', 'pk': self.order.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data['id'], self.order.id)
        self.assertEqual(str(data['total']), f"{self.order.total:.2f}")

    def test_cannot_retrieve_other_users_order(self):
        other_user = UserFactory()
        other_order = Order.objects.create(user=other_user)
        OrderItem.objects.create(order=other_order, product=self.product, quantity=1, price=self.product.price)
        response = self.client.get(
            reverse('orders-detail', kwargs={'version': 'v1', 'pk': other_order.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        def test_create_order_missing_user(self):
            # Explicitly include 'user' in payload, should be ignored or cause error
            data = {
                'user': 9999,
                'items': [
                    {'product': self.product.id, 'quantity': 1, 'price': float(self.product.price)}
                ]
            }
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            # Should ignore 'user' field and create order for authenticated user
            self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

        def test_create_order_empty_items(self):
            # Items is empty list
            data = {'items': []}
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_create_order_negative_quantity(self):
            # Negative quantity
            data = {
                'items': [
                    {'product': self.product.id, 'quantity': -1, 'price': float(self.product.price)}
                ]
            }
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_create_order_zero_quantity(self):
            # Zero quantity
            data = {
                'items': [
                    {'product': self.product.id, 'quantity': 0, 'price': float(self.product.price)}
                ]
            }
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_create_order_missing_product(self):
            # Missing product field in item
            data = {
                'items': [
                    {'quantity': 1, 'price': float(self.product.price)}
                ]
            }
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_create_order_missing_quantity(self):
            # Missing quantity field in item
            data = {
                'items': [
                    {'product': self.product.id, 'price': float(self.product.price)}
                ]
            }
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_create_order_missing_price(self):
            # Missing price field in item
            data = {
                'items': [
                    {'product': self.product.id, 'quantity': 1}
                ]
            }
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_create_order_invalid_price_type(self):
            # Price is a string instead of a float
            data = {
                'items': [
                    {'product': self.product.id, 'quantity': 1, 'price': "not_a_number"}
                ]
            }
            response = self.client.post(
                reverse('orders-list', kwargs={'version': 'v1'}),
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
