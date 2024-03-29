import datetime

from django.core.validators import RegexValidator
from django.db import models
# from django.utils.translation import gettext_lazy as _

from utils.school_util import SchoolUtils


class CityModel(models.Model):
    class Meta:
        db_table = 'cities'
        verbose_name = 'Cities'
        verbose_name_plural = 'Cities'
        ordering = ['name', ]

    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class SchoolModel(models.Model):
    class Meta:
        db_table = 'school'
        verbose_name = 'Schools'
        verbose_name_plural = 'Schools'
        ordering = ['name', ]

    # name / Назва школи -- string
    # priority / Пріоритет -- int
    # logo / Лого -- string
    # about / Про школу -- string
    # city / Місто -- ManyToManyField
    # homework / Перевірка ДЗ -- boolean
    # certificate / Сертифікат -- boolean
    # internship / Стажування -- boolean
    # site / Сайт -- string
    # facebook / Фейсбук -- string
    # instagram / Інстаграм -- string
    # telegram / Телеграм -- string
    # tiktok / Тікток -- string
    # youtube / Ютюб -- string
    # comment / Залишити коментар -- ManyToManyField

    name = models.CharField(max_length=100, blank=False)
    priority = models.PositiveSmallIntegerField(blank=True, default=0)
    logo = models.ImageField(upload_to=SchoolUtils.upload_to, blank=True)
    about = models.TextField(max_length=300, blank=True)
    cities = models.ManyToManyField(CityModel, related_name='cities', blank=True)
    homework = models.BooleanField(default=False)
    certificate = models.BooleanField(default=False)
    internship = models.BooleanField(default=False)
    site = models.URLField(default='')
    facebook = models.URLField(default='')
    instagram = models.URLField(default='')
    telegram = models.URLField(default='')
    tiktok = models.URLField(default='')
    youtube = models.URLField(default='')
    # comments = models.ForeignKey(CommentModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name='cities')
    # ages = models.ManyToManyField(AgeModel, related_name='ages')
    # learn_formats = models.ManyToManyField(LearnFormatModel, related_name='learn_formats')

    # class LearnFormatModel(models.TextChoices):
    #     ONLINE = 'ONLINE', _('Online')
    #     OFFLINE = 'OFFLINE', _('Offline')
    #
    # learn_format = models.CharField(
    #     max_length=7,
    #     choices=LearnFormatModel.choices,
    #     default=LearnFormatModel.ONLINE,
    # )

    # surname = models.CharField(max_length=30, validators=[
    #     RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
    # ], blank=True)
    # born = models.DateField(default='2000-01-01', blank=True, verbose_name='Date of birth')
    # avatar = models.ImageField(upload_to=AvatarUtils.upload_to, blank=True)
    # phone = models.CharField(max_length=13, validators=[
    #     RegexValidator(r'^\+380[\d]{9}$', 'Invalid phone number ex. +380xxxxxxxxx')
    # ], blank=True)
    # user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')


class CommentModel(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'
        ordering = ['created_at', ]

    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    def approve(self):
        self.approved_at = datetime.datetime.now()
        self.save()

    def __str__(self):
        return self.text

# class AgeModel(models.Model):
#     class Meta:
#         db_table = 'ages'
#         verbose_name = 'Ages'
#         verbose_name_plural = 'Ages'
#         ordering = ['name', ]
#
#     name = models.CharField(max_length=30, validators=[
#         # RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{2,30}$')
#     ], blank=False)
#
#     def __str__(self):
#         return self.name


# class LearnFormatModel(models.Model):
#     class Meta:
#         db_table = 'learn_formats'
#         verbose_name = 'Learn formats'
#         verbose_name_plural = 'Learn formats'
#         ordering = ['name', ]
#
#     name = models.CharField(max_length=30, blank=False)
#
#     def __str__(self):
#         return self.name
