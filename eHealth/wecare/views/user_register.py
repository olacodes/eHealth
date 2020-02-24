from django.shortcuts import render
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from ..forms.user_registration import UserRegistrationForm, UserProfileForm 
from django.contrib.auth.views import LoginView



class UserFormView(FormView):
    template_name = 'index.html'
    # success_url = 'register'

    def post(self, request, *args, **kwargs):
    
        form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return render(request, 'dashboard.html', {'user':user})
        else:
            return self.form_invalid(form)
            








# def user_register(request):
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


# class Register(View):
#     template_name = 'register.html'
#     form_class = UserRegistrationForm

#     # @transaction.atomic
#     def post(self, request, *args, **kwargs):

#         form = UserRegistrationForm(request.POST)
#         profile_form = UserProfileForm(request.POST)

#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()
            
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()

#             raw_password = form.cleaned_data.get('password')
#             username = form.cleaned_data.get('username')

#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return render(request, 'index.html', {'user':user})

#         else:
#             form = UserRegistrationForm()
#             profile_form = UserProfileForm()

    # def get(self, request):
        # form = UserRegistrationForm()
        # profile_form = UserProfileForm()
        # form = self.form_class()

    # context = {'form': self.form, 'profile_form': profile_form}
    # return render(request, 'register.html', context)
     