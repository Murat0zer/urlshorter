# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_urlshortener_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
