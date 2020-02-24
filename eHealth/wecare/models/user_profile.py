from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    GENDER = [('M', 'Male'), ('F', 'Female'),]
    
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type   = models.CharField(max_length=50, blank=False, default='user')
    gender      = models.CharField(max_length=1, choices=GENDER, default='M')
    
    def __str__(self):
        return self.user.username

