from django.contrib.auth.models import User
from django.db import models

class Volunteer(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        app_label = "volunteers"
