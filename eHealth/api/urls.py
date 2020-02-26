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


urlpatterns = [
    path('users/', Users.as_view(), name='users'),
    path('users/medical-records', UsersMedicalRecords.as_view(), name='medical-records'),
    path('users/medical-records/<int:user_id>', UserMedicalRecord.as_view(), name='medical-records'),
    path('common-illness/', MostCommonIllness.as_view(), name='common-illness'),
    path('self-medication/', SelfMedication.as_view(), name='self-medication'),
    path('health-habit/', HealthHabit.as_view(), name='health-habit'),
]