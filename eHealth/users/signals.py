from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models.medical_information import MedicalInformation


@receiver(post_save, sender=User)
def create_med_info(sender, instance, created, **kwargs):
    if created:
        MedicalInformation.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_med_info(sender, instance, **kwargs):
    instance.medicalinformation.save()