# Generated by Django 4.2.5 on 2024-01-10 04:33

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muskeer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='modifiedDate',
            field=models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
