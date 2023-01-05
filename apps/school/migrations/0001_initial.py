# Generated by Django 4.0.6 on 2022-08-15 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[A-Za-z][A-Za-z0-9_]{2,30}$')])),
            ],
            options={
                'verbose_name': 'Cities',
                'verbose_name_plural': 'Cities',
                'db_table': 'cities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Catalog of schools',
                'verbose_name_plural': 'Catalog of schools',
                'db_table': 'school',
                'ordering': ['name'],
            },
        ),
    ]