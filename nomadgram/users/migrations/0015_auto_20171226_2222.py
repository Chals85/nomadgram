# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-26 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20171226_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('not-specified', 'Not spacified'), ('male', 'Male')], max_length=80, null=True),
        ),
    ]
