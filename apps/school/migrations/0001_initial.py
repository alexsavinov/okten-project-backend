# Generated by Django 4.0.6 on 2023-01-17 21:08

from django.db import migrations, models
import django.db.models.deletion
import utils.school_util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
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
                ('priority', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('logo', models.ImageField(blank=True, default='', upload_to=utils.school_util.SchoolUtils.upload_to)),
                ('about', models.TextField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cities', models.ManyToManyField(related_name='cities', to='school.citymodel')),
            ],
            options={
                'verbose_name': 'Schools',
                'verbose_name_plural': 'Schools',
                'db_table': 'school',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.schoolmodel')),
            ],
            options={
                'verbose_name': 'Comments',
                'verbose_name_plural': 'Comments',
                'db_table': 'comments',
                'ordering': ['created_at'],
            },
        ),
    ]
