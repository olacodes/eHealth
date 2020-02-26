from django.urls import path, include

from .views.user_records import (
    Users, 
    UsersMedicalRecords, 
    UserMedicalRecord
)



urlpatterns = [
    path('users/', Users.as_view(), name='users'),
    path('users/medical-records', UsersMedicalRecords.as_view(), name='medical-records'),
    path('users/medical-records/<int:user_id>', UserMedicalRecord.as_view(), name='medical-records'),
    
]