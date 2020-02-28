from django.db import models
from django.contrib.auth.models import User

# OPTIONS FOR CHOICES FIELDS
GENDER                       = [('Male', 'Male'), ('Female', 'Female'),]
MARITAL_STATUS               = [('Single', 'Single'), ('Married', 'Married'), ('DI', 'Divorce')]
YES_OR_NO                    = [('Yes', 'YES'), ('No', 'NO')]
NO_SOMETIMES_ALWAYS          = [('No', 'NO'), ('Sometimes', 'SOMETIMES'), ('Always', 'ALWAYS')]
COMMON_DISEASES              = [('Malaria', 'MALARIA'), ('Fever', 'FEVER'), ('Tuberculosis', 'TUBERCULOSIS'), ('Cholera', 'CHOLERA'), ('Others', 'OTHERS')]

class MedicalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # personal info
    gender                       = models.CharField(max_length=50, choices=GENDER)
    address                      = models.CharField(max_length=255)
    age                          = models.IntegerField(default=0)
    marital_status               = models.CharField(max_length=50, choices=MARITAL_STATUS)
    phone_number                 = models.CharField(max_length=30)
    occupation                   = models.CharField(max_length=255)

    # General Question for doctors
    allergies                    = models.CharField(max_length=255)
    last_diagnose                = models.CharField(max_length=255)

    # Good health habit/ practice
    adequate_exercise            = models.CharField(max_length=50, choices=NO_SOMETIMES_ALWAYS)
    adequate_sleep               = models.CharField(max_length=50, choices=NO_SOMETIMES_ALWAYS)
    smoke_or_drink               = models.CharField(max_length=50, choices=NO_SOMETIMES_ALWAYS)

    # Rate of self medication questions
    last_self_medication         = models.CharField(max_length=50, choices=YES_OR_NO)
    frequent_self_medication     = models.CharField(max_length=50, choices=YES_OR_NO)
    doctor_precription           = models.CharField(max_length=50, choices=YES_OR_NO)

    # Most Common Illness
    common_illness               =  models.CharField(max_length=50, choices=COMMON_DISEASES)

    def __str__(self):
        return f'{self.user.username} MedicalInfo'

