# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0003_auto_20150908_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpior2',
            name='action',
            field=models.CharField(default='', max_length=30, choices=[('toggle light', 'toggle light')]),
        ),
        migrations.AlterField(
            model_name='gpior1',
            name='command',
            field=models.CharField(max_length=30, choices=[('gpio.input', 'input'), ('gpio.output', 'output')]),
        ),
        migrations.AlterField(
            model_name='gpior2',
            name='command',
            field=models.CharField(max_length=30, choices=[('gpio.input', 'input'), ('gpio.output', 'output')]),
        ),
    ]
