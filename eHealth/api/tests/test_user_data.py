from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

from django.contrib.auth.models import User
from ..mock_data import MockData

class TestUser(APITestCase):
    
    client = APIClient()

    def test_get_all_user(self):
        user = User(**MockData.user_data())
        user.save()
        url = reverse('users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        