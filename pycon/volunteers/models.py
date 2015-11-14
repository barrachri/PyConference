from django.contrib.auth.models import User
from django.db import models

class Volunteer(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=128)
    
    class Meta:
        app_label = "volunteers"
