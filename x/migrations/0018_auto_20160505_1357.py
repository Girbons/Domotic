# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-05 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0017_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='id_icon',
            field=models.CharField(default=b'', max_length=5, unique=True),
        ),
    ]
