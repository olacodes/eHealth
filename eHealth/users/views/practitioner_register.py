from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from ..forms.practitioner import PractitionerRegisterForm


def practitioner_register(request):
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
        form = PractitionerRegisterForm()
    return render(request, 'practitioner/register.html', {'form': form})
