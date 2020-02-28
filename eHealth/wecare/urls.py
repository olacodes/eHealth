from django.urls import path
from .views import (
    dashboard,
)


urlpatterns = [
    path('dashboard/', dashboard.Dashboard.as_view(), name='dashboard'),
]