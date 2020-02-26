from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
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
        labels = {
            'allergies': _('I am allergic to ?'),
            'last_diagnose': _('I was recently diagnose of?'),
            'adequate_exercise': _('I participate in sports or physical exercise daily for at least 20 minutes ?'),
            'adequate_sleep': _('I get an adequate amount of sleep daily for at least 6 hours'),
            'smoke_or_drink': _('I smoke or drink or both'),
            'frequent_self_medication': _('I indulge in self-medication eveytime I notice any symptoms of disease'),
            'last_self_medication': _('Have you taken self-medication in the last 12 months?'),
            'doctor_precription': _('I buy and use drugs without doctor\'s prescription'),
            'common_illness': _('For which condition have you been diagnose, treated or monitored (most recent)')
        }
        

