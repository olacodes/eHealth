from django.test import TestCase
from django.contrib.auth.models import User

from ..mock_data.mock_data import MockData

class PractitionerTest(TestCase):

    def test_can_create_practitioner(self):
        user = User.objects.create(**MockData.user_data())
        self.assertEqual(user.username, 'sodiq')
        self.assertEqual(user.first_name, 'ishola')

         