from django.db import models
from django.contrib.auth.models import User

# OPTIONS FOR CHOICES FIELDS
GENDER                       = [('M', 'Male'), ('F', 'Female'),]
MARITAL_STATUS               = [('SI', 'Single'), ('MA', 'Married'), ('DI', 'Divorce')]
YES_OR_NO                    = [('Y', 'YES'), ('N', 'NO')]
NO_SOMETIMES_ALWAYS          = [('NO', 'NO'), ('SMT', 'SOMETIMES'), ('AWS', 'ALWAYS')]
COMMON_DISEASES              = [('MAL', 'MALARIA'), ('FEV', 'FEVER'), ('TUB', 'TUBERCULOSIS'), ('CHOL', 'CHOLERA'), ('OTHERS', 'OTHERS')]

class MedicalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # personal info
    gender                       = models.CharField(max_length=1, choices=GENDER)
    address                      = models.CharField(max_length=255)
    age                          = models.IntegerField(default=0)
    marital_status               = models.CharField(max_length=2, choices=MARITAL_STATUS)
    phone_number                 = models.CharField(max_length=30)
    occupation                   = models.CharField(max_length=255)

    # General Question for doctors
    allergies                    = models.CharField(max_length=255)
    last_diagnose                = models.CharField(max_length=255)

    # Good health habit/ practice
    adequate_exercise            = models.CharField(max_length=3, choices=NO_SOMETIMES_ALWAYS)
    adequate_sleep               = models.CharField(max_length=3, choices=NO_SOMETIMES_ALWAYS)
    smoke_or_drink               = models.CharField(max_length=3, choices=NO_SOMETIMES_ALWAYS)

    # Rate of self medication questions
    last_self_medication         = models.CharField(max_length=3, choices=YES_OR_NO)
    frequent_self_medication     = models.CharField(max_length=3, choices=YES_OR_NO)
    doctor_precription           = models.CharField(max_length=3, choices=YES_OR_NO)

    # Most Common Illness
    common_illness               =  models.CharField(max_length=7, choices=COMMON_DISEASES)

    def __str__(self):
        return f'{self.user.username} MedicalInfo'

