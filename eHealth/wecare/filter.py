import sys
sys.path.append('..')
import django_filters
from users.models.medical_information import MedicalInformation, GENDER


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = MedicalInformation
        fields = ['user', 'common_illness', 'gender']
