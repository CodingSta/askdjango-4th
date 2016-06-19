from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
