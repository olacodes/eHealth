from django.contrib.auth.models import User


class MockData:
    @classmethod
    def user_data(cls):
        return {
        'id': 1,
        'first_name': 'ishola',
        'username': 'sodiq',
        'email': 'olatundesodiq@gmail.com',
        'password': 'olatunde123',
    }

    @classmethod
    def create_user(cls):
        user = User(**MockData.user_data())
        return user

    @classmethod
    def user_profile(cls):
        user = MockData.create_user()
        return {
            'user_id': user.id,
            'gender': 'M'
        }

    @classmethod
    def practitioner_profile(cls):
        user = MockData.create_user()
        return {
            'user_id': user.id,
            'department': 'surgical'
        }