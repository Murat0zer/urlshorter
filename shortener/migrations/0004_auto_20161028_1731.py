# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20161028_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortener',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default='1999-1-1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urlshortener',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
