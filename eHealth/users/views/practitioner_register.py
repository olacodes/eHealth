from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
import sys
from ..forms.practitioner import PractitionerRegisterForm
sys.path.append('..')
from wecare.views.medical_api import get_users


def practitioner_register(request):
    print(get_users())
    if request.method == 'POST':
        form =  PractitionerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            messages.success(request, f'Account created for {username}')
            login(request, user)
            return redirect('dashboard')

    else:
        get_users()
        form = PractitionerRegisterForm()
    return render(request, 'users/register.html', {'form': form})
