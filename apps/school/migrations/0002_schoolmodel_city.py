# Generated by Django 4.0.6 on 2022-08-15 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolmodel',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='school.citymodel'),
            preserve_default=False,
        ),
    ]
