# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0004_auto_20150909_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpior1',
            name='command',
        ),
        migrations.RemoveField(
            model_name='gpior2',
            name='command',
        ),
        migrations.AddField(
            model_name='gpior1',
            name='action',
            field=models.CharField(default='', max_length=30, choices=[('toggle light', 'toggle light')]),
        ),
        migrations.AlterField(
            model_name='gpior1',
            name='text',
            field=models.CharField(default='type the configuration name', max_length=50),
        ),
    ]
