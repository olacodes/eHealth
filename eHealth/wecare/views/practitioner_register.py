from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.db import transaction
from ..forms.practioner_registration import PractionerRegistrationForm, PractitionerProfileForm 


def practitioner_register(request):
    if request.method == 'POST':
        form = PractionerRegistrationForm(request.POST)
        profile_form = PractitionerProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return render(request, 'index.html', {'user':user})
    else:
        form = PractionerRegistrationForm()
        profile_form = PractitionerProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'index.html', context)
