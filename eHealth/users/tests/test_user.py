from django.test import TestCase
from django.contrib.auth.models import User

from ..mock_data.mock_data import MockData

class UserTest(TestCase):

    def test_create_user(self):
        user = User.objects.create(**MockData.user_data())
        self.assertEqual(user.username, 'sodiq')
        self.assertEqual(user.first_name, 'ishola')
