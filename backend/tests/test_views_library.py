from django.test import TestCase, Client
from django.urls import reverse
from library.models import LibraryEntry
from product.models import Product
from user.models import CustomUser

class LibraryEntryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            nickname='testuser_nick',
            email='testuser@example.com'
        )
        self.other_user = CustomUser.objects.create_user(
            username='otheruser',
            password='otherpass',
            nickname='otheruser_nick',
            email='otheruser@example.com'
        )
        self.product = Product.objects.create(title='Test Game', price=10)
        self.entry = LibraryEntry.objects.create(user=self.user, product=self.product)

    def test_library_list_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('library-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.title)

    def test_library_list_unauthenticated(self):
        url = reverse('library-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)  # Unauthorized, as the user is not logged in

    def test_library_detail_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('library-detail', args=[self.entry.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.title)

    def test_library_detail_other_user_forbidden(self):
        self.client.login(username='otheruser', password='otherpass')
        url = reverse('library-detail', args=[self.entry.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_library_force_entry_creation(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('library-list')
        data = {'user': self.user.id, 'product': self.product.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
        

    def test_library_entry_deletion(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('library-detail', args=[self.entry.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed, as deletion is not implemented in the API