from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models.medical_information import MedicalInformation
from django.core.exceptions import ObjectDoesNotExist


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
        