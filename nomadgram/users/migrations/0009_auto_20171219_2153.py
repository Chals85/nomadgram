# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-19 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20171219_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('not-specified', 'Not spacified')], max_length=80, null=True),
        ),
    ]
