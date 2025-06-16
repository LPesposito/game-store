from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import CustomUser

# User registration and listing tests

class UserViewTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {
            "username": "testuser",
            "nickname": "nick",
            "email": "test@example.com",
            "password": "testpass123",
            "password2": "testpass123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username="testuser").exists())

    def test_user_list_authenticated(self):
        user = CustomUser.objects.create_user(username="user1", password="pass")
        self.client.force_authenticate(user=user)
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print(response.data)
        self.assertTrue(any(u['username'] == "user1" for u in response.data['results']))
