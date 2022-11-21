import datetime

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from rest_framework.reverse import reverse

from utils.avatar_util import AvatarUtils

UserModel = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profiles of users'
        verbose_name_plural = 'Profiles of users'
        ordering = ['name', 'surname', '-born']

    name = models.CharField(max_length=30, validators=[
        RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
    ], blank=True)
    surname = models.CharField(max_length=30, validators=[
        RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
    ], blank=True)
    born = models.DateField(default='2000-01-01', blank=True, verbose_name='Date of birth')
    avatar = models.ImageField(upload_to=AvatarUtils.upload_to, blank=True)
    phone = models.CharField(max_length=13, validators=[
        RegexValidator(r'^\+380[\d]{9}$', 'Invalid phone number ex. +380xxxxxxxxx')
    ], blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')


