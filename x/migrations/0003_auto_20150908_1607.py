# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0002_auto_20150908_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpior1',
            name='param',
        ),
        migrations.RemoveField(
            model_name='gpior2',
            name='param',
        ),
        migrations.AlterField(
            model_name='gpior2',
            name='text',
            field=models.CharField(default='configuration name  ', max_length=50),
        ),
    ]
