from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


# OPTIONS FOR CHOICES FIELDS
GENDER                       = [('Male', 'Male'), ('Female', 'Female'),]
MARITAL_STATUS               = [('Single', 'Single'), ('Married', 'Married'), ('Divorce', 'Divorce')]
YES_OR_NO                    = [('Yes', 'Yes'), ('No', 'No')]
NO_SOMETIMES_ALWAYS          = [('No', 'No'), ('Sometimes', 'Sometimes'), ('Always', 'Always')]
COMMON_DISEASES              = [('Malaria', 'Malaria'), ('Fever', 'Fever'), ('Tuberculosis', 'Tuberculosis'), ('Cholera', 'Cholera'), ('Others', 'Others')]

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




@receiver(post_save, sender=User)
def create_med_info(sender, instance, created, **kwargs):
    if created:
        MedicalInformation.objects.create(user=instance).save()


@receiver(post_save, sender=User)
def save_med_info(sender, instance, **kwargs):
    try:
        instance.medicalinformation.save()
    except ObjectDoesNotExist:
        MedicalInformation.objects.create(user=instance)
        
