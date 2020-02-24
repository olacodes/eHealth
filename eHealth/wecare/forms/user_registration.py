from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..models.user_profile import UserProfile

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('gender',)

