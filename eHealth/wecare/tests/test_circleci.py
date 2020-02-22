from django.test import TestCase

# Create your tests here.

class SetUpTesting(TestCase):
    def test_set_up(self):
        self.assertEqual(2 + 2, 4)
