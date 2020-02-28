import sys
sys.path.append('..')
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from api.views.user_records import UsersMedicalRecords, UserMedicalRecord
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin


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
        user = request.user.id
        users = UsersMedicalRecords.get(self, request)
        users_data = users.data['users_medical_records']
        return render(request, self.template_name, {'users': users_data})

        

# class UserInformation(View):  
#     template_name = 'user.html',

#     def get(self, request):
#         user_id = request.user.id
#         user = UserMedicalRecord.get(self, request, user_id)
#         user_data = user.data['user_medical_record']
#         return render(request, self.template_name, {'users': user_data})
