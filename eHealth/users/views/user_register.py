from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from ..forms.user_register import UserRegistraterForm


def user_register(request):
    if request.method == 'POST':
        form =  UserRegistraterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            messages.success(request, f'Account created for {username}')
            login(request, user)
            return redirect('dashboard')

    else:
        form = UserRegistraterForm()
    return render(request, 'users/register.html', {'form': form})