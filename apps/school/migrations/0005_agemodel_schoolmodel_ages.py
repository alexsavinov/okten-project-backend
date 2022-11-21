# Generated by Django 4.0.6 on 2022-08-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_schoolmodel_city_schoolmodel_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Ages',
                'verbose_name_plural': 'Ages',
                'db_table': 'ages',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='ages',
            field=models.ManyToManyField(related_name='ages', to='school.agemodel'),
        ),
    ]
