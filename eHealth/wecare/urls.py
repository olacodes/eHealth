from django.urls import path
from .views import (
    dashboard,
    home 
)

urlpatterns = [
    path('', home.Home.as_view(), name='home'),
    path('dashboard/', dashboard.Dashboard.as_view(), name='dashboard'),
]