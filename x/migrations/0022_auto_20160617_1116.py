# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0021_auto_20160616_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
