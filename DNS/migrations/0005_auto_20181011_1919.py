# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-11 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNS', '0004_zone_create_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='\u57df\u540d'),
        ),
    ]
