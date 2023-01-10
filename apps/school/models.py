from django.core.validators import RegexValidator
from django.db import models

from utils.school_util import SchoolUtils
from django.utils.translation import gettext_lazy as _

# name / Назва школи
# priority / Пріоритет
# logo / Лого
# about / Про школу
# city / Місто
# homework / Перевірка ДЗ
# certificate / Сертифікат
# internship / Стажування
# site / Сайт
# facebook / Фейсбук
# instagram / Інстаграм
# telegram / Телеграм
# tiktok / Тікток
# youtube / Ютюб
# comment / Залишити коментар

class CityModel(models.Model):
    class Meta:
        db_table = 'cities'
        verbose_name = 'Cities'
        verbose_name_plural = 'Cities'
        ordering = ['name', ]

    name = models.CharField(max_length=30, validators=[
        # RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
    ], blank=False)

    def __str__(self):
        return self.name


class AgeModel(models.Model):
    class Meta:
        db_table = 'ages'
        verbose_name = 'Ages'
        verbose_name_plural = 'Ages'
        ordering = ['name', ]

    name = models.CharField(max_length=30, validators=[
        # RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
    ], blank=False)

    def __str__(self):
        return self.name

class LearnFormat(models.Model):
    class Meta:
        db_table = 'learn_formats'
        verbose_name = 'Learn formats'
        verbose_name_plural = 'Learn format'
        ordering = ['name', ]

    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class SchoolModel(models.Model):
    class Meta:
        db_table = 'school'
        verbose_name = 'Catalog of schools'
        verbose_name_plural = 'Catalog of schools'
        ordering = ['name', ]

    # class LearnFormat(models.TextChoices):
    #     ONLINE = 'ONLINE', _('Online')
    #     OFFLINE = 'OFFLINE', _('Offline')
    #
    # learn_format = models.CharField(
    #     max_length=7,
    #     choices=LearnFormat.choices,
    #     default=LearnFormat.ONLINE,
    # )


    name = models.CharField(max_length=100, validators=[
        # RegexValidator(r'^[A-Za-z][A-Za-z0-9_\s]{2,100}$')
    ], blank=False)

    about = models.CharField(max_length=300,
                             # validators=[
                             #   RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
                             # ],
                             blank=True)

    # city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name='cities')
    cities = models.ManyToManyField(CityModel, related_name='cities')
    ages = models.ManyToManyField(AgeModel, related_name='ages')
    logo = models.ImageField(upload_to=SchoolUtils.upload_to, blank=True, default="")

    learn_format = models.ManyToOneRel(max_length=100, validators=[
        # RegexValidator(r'^[A-Za-z][A-Za-z0-9_\s]{2,100}$')
    ], blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # surname = models.CharField(max_length=30, validators=[
    #     RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
    # ], blank=True)
    # born = models.DateField(default='2000-01-01', blank=True, verbose_name='Date of birth')
    # avatar = models.ImageField(upload_to=AvatarUtils.upload_to, blank=True)
    # phone = models.CharField(max_length=13, validators=[
    #     RegexValidator(r'^\+380[\d]{9}$', 'Invalid phone number ex. +380xxxxxxxxx')
    # ], blank=True)
    # user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
