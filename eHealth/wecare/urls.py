from django.urls import path
from .views import (
    user_register, 
    practitioner_register,
    index,
    med_info_view,
    dashboard,    
)

urlpatterns = [
    path('', index.Index.as_view(), name='index'),
    path('dashboard/', dashboard.Dashboard.as_view(), name='dashboard'),
    path('register/', user_register.UserFormView.as_view(), name='register'),
    path('medical-information', med_info_view.med_info_view, name='medical-information'),
    path('practitioner/register', practitioner_register.practitioner_register, name='practitioner-register'),
]