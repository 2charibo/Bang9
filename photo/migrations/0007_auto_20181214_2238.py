# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-14 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20181214_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='junse',
            field=models.CharField(blank=True, max_length=50, verbose_name='전세'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='bojunggum',
            field=models.CharField(blank=True, max_length=50, verbose_name='보증금/월세'),
        ),
    ]
