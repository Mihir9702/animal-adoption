from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Animal

class AnimalViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.animal = Animal.objects.create(name='Fido', species='Dog', age=3, description='Friendly dog')

    def test_list_animals(self):
        url = reverse('animal-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_animal(self):
        url = reverse('animal-detail', kwargs={'pk': self.animal.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Fido')

    def test_update_animal(self):
        url = reverse('animal-detail', kwargs={'pk': self.animal.pk})
        data = {'name': 'Max', 'species': 'Cat', 'age': 2, 'description': 'Playful cat'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Max')

    def test_adopt_animal(self):
        url = reverse('animal-adopt', kwargs={'pk': self.animal.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['adopted'])
        self.assertEqual(response.data['adopted_by'], self.user.id)
