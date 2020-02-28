from django.urls import path
from .views import (
    dashboard,
    home,
    user_information 
)

urlpatterns = [
    path('', home.Home.as_view(), name='home'),
    path('dashboard/', dashboard.Dashboard.as_view(), name='dashboard'),
    path('users/', user_information.UsersInformation.as_view(), name='users'),
]