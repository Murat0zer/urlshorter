# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20161028_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortener',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
