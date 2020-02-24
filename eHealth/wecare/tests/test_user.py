from django.test import TestCase
from django.contrib.auth.models import User

from ..models.user_profile import UserProfile
from ..mock_data.mock_data import MockData

class UserProfileTest(TestCase):

    def test_can_create_user(self):
        user = User.objects.create(**MockData.user_data())
        self.assertEqual(user.username, 'sodiq')
        self.assertEqual(user.first_name, 'ishola')

    def test_create_correct_user_type(self):
        user = User.objects.create(**MockData.user_data())
        user_profile = UserProfile.objects.create(**MockData.user_profile())
        self.assertEqual(user_profile.user_type, 'user')
        self.assertEqual(user_profile.gender, 'M')
    