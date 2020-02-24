from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from ..forms.user_registration import UserRegistrationForm, UserProfileForm 
from django import forms


class Index(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(self.request.GET or None)
        user_profile_form = UserProfileForm(self.request.GET or None)

        context = self.get_context_data(**kwargs)
        context['form'] = user_form
        context['profile_form'] = user_profile_form
        return self.render_to_response(context)


        



    # def user_register(self,request):
    #     if request.method == 'POST':
    #         form = UserRegistrationForm(request.POST)
    #         profile_form = UserProfileForm(request.POST)

    #         if form.is_valid() and profile_form.is_valid():
    #             user = form.save()
                
    #             profile = profile_form.save(commit=False)
    #             profile.user = user
    #             profile.save()

    #             username = form.cleaned_data.get('username')
    #             raw_password = form.cleaned_data.get('password1')

    #             user = authenticate(username=username, password=raw_password)
    #             login(request, user)

    #             return render(request, 'dashboard.html', {'user':user})
    #     else:
    #         form = UserRegistrationForm()
    #         profile_form = UserProfileForm()

    #     context = {'form': form, 'profile_form': profile_form}
    #     return render(request, 'index.html', context)



    # def practitioner_register(self, request):
    #     if request.method == 'POST':
    #         form = PractionerRegistrationForm(request.POST)
    #         profile_form = PractitionerProfileForm(request.POST)

    #     if form.is_valid() and profile_form.is_valid():
    #         user = form.save()
            
    #         profile = profile_form.save(commit=False)
    #         profile.user = user
    #         profile.save()

    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')

    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)

    #         return render(request, 'index.html', {'user':user})
    #     else:
    #         form = PractionerRegistrationForm()
    #         profile_form = PractitionerProfileForm()

    #     context = {'form': form, 'profile_form': profile_form}
    #     return render(request, 'index.html', context)

     