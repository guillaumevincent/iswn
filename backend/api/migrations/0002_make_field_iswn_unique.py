# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iswn',
            name='iswn',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
