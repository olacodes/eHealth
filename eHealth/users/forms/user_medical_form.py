from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..models.medical_information import MedicalInformation

class UserMedicalForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'email',)

class UserMedicalFormUpdate(forms.ModelForm):
    class Meta:
        model = MedicalInformation
        fields = '__all__'
        exclude = ['user']
        

