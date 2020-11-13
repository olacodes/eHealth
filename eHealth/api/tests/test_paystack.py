from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase 
    
class TestAddAccount(APITestCase):

  def setUp(self):
    self.correct_data = {
        "account_number": "0221618652",
        "bank_code": "058",
        "bank_name": "GTB Bank"
    }
    
  def test_add_valid_account(self):
      url = reverse('paystack')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)