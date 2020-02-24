from django.contrib.auth.models import User
from django.db import models

class Practitioner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, default='practitioner', null=False)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
