from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com',
            first_name='Test'
        )

    def test_login_view(self):
        response = self.client.post(reverse('account:login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('movies:movies'))

    def test_register_view(self):
        response = self.client.post(reverse('account:register'), {
            'username': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'user_type': 'normal'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account:login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
