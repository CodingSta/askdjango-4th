import re
from django.conf import settings
from django.forms import ValidationError
from django.db import models


def phonenumber_validator(value):
    if re.match(r'^01[016789][1-9]\d{6,7}$', value) is None:
        raise ValidationError('휴대폰 번호를 입력해주세요.')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True, validators=[phonenumber_validator])
