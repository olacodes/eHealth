from django.test import TestCase
from django.contrib.auth.models import User

from ..models.practitioner import Practitioner
from ..mock_data.mock_data import MockData

class PractitionerTest(TestCase):

    def test_can_create_practitioner(self):
        user = User.objects.create(**MockData.user_data())
        self.assertEqual(user.username, 'sodiq')
        self.assertEqual(user.first_name, 'ishola')

    def test_create_correct_user_type(self):
        user = User.objects.create(**MockData.user_data())
        user_profile = Practitioner.objects.create(**MockData.practitioner_profile())
        self.assertEqual(user_profile.user_type, 'practitioner')
        self.assertEqual(user_profile.department, 'surgical')
         