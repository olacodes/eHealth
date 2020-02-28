from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

class Dashboard(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs) 

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        return render(request, 'dashboard.html')
        