# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-28 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20171228_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('not-specified', 'Not spacified'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]
