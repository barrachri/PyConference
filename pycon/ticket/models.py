"""
This is the model for the fares, tickets and invoice for the conference
"""

import datetime

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# You import settings to access the settings_conference.py
from django.conf import settings

class Fare(models.Model):
    '''
    Speaker is linked with a registered user, so every speaker must be a user
    '''
    name = models.CharField(max_length=50)
    year = models.BooleanField(default=False)
    duration = models.TextField(blank=True)
    url = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
