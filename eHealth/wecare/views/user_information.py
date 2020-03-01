import sys
sys.path.append('..')
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from api.views.user_records import UsersMedicalRecords, UserMedicalRecord
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models.medical_information import MedicalInformation
from ..filter import UserFilter


class TestIsStaff(UserPassesTestMixin):
        def test_func(self):
            return self.request.user.is_staff


class UsersInformation(TestIsStaff, View):  
    template_name = 'users.html',

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs) 


    @method_decorator(login_required)
    def get(self, request):
        users = MedicalInformation.objects.select_related('user')
        f = UserFilter(request.GET, queryset=users)
        context = {'filter': f}
        users = f.qs
        return render(request, self.template_name,  context)
