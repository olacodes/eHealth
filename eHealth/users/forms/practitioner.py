from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PractitionerRegisterForm(UserCreationForm):
    email       = forms.EmailField()
    is_staff    = forms.BooleanField(initial=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')
        