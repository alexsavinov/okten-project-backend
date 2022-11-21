# Generated by Django 4.0.6 on 2022-08-29 18:22

from django.db import migrations, models
import utils.school_util


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_agemodel_schoolmodel_ages'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolmodel',
            name='logo',
            field=models.ImageField(blank=True, upload_to=utils.school_util.SchoolUtils.upload_to),
        ),
    ]
