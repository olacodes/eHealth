from django.urls import path, include

from .views.user_records import (
    Users, 
    UsersMedicalRecords, 
    UserMedicalRecord
)
from .views.medical_data import (
    MostCommonIllness, 
    SelfMedication, 
    HealthHabit
    )

from .views.filter_user import (
    FilterByCholera,
    FilterByFever,
    FilterByMalaria,
    FilterByTB,
    FilterByMale,
    FilterByFemale
)

from .views.paystack import Paystack


urlpatterns = [
    path('users/', Users.as_view(), name='users-api'),
    path('paystack/', Paystack.as_view(), name='paystack'),
    path('users/medical-records', UsersMedicalRecords.as_view(), name='medical-records'),
    path('users/medical-records/<int:user_id>', UserMedicalRecord.as_view(), name='medical-records'),
    path('common-illness/', MostCommonIllness.as_view(), name='common-illness'),
    path('self-medication/', SelfMedication.as_view(), name='self-medication'),
    path('health-habit/', HealthHabit.as_view(), name='health-habit'),
    path('filter/malaria', FilterByMalaria.as_view(), name='filter-by-malaria'),
    path('filter/fever', FilterByFever.as_view(), name='filter-by-fever'),
    path('filter/tb', FilterByTB.as_view(), name='filter-by-tb'),
    path('filter/cholera', FilterByCholera.as_view(), name='filter-by-cholera'),
    path('filter/male', FilterByMale.as_view(), name='filter-by-male'),
    path('filter/female', FilterByFemale.as_view(), name='filter-by-female'),

]
