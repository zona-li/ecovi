# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-15 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeowners', '0002_remove_homeowner_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeowner',
            name='password',
            field=models.CharField(default='null', max_length=50),
        ),
    ]