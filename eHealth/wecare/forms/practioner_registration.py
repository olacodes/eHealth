from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..models.practitioner import Practitioner

class PractionerRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')

class PractitionerProfileForm(forms.ModelForm):

    class Meta:
        model = Practitioner
        fields = ('department',)