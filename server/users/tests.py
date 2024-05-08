from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.user_data = {'email': 'test@example.com', 'password': 'testpassword'}

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'test@example.com')

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('user-login')
        self.user = CustomUser.objects.create(email='test@example.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.user_data = {'email': 'test@example.com', 'password': 'testpassword'}

    def test_user_login(self):
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Login successful')

    def test_invalid_user_login(self):
        self.user_data['password'] = 'wrongpassword'
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Invalid credentials')
