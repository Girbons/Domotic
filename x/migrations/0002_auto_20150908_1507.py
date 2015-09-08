# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpior1',
            name='text',
            field=models.CharField(default='configuration name', max_length=50),
        ),
        migrations.AddField(
            model_name='gpior2',
            name='text',
            field=models.CharField(default='configuration name', max_length=50),
        ),
        migrations.AlterField(
            model_name='gpior1',
            name='command',
            field=models.CharField(choices=[('gpio.setmode', 'setmode_BOARD'), ('gpio.setmode', 'setmode_BCM'), ('gpio.setup', 'setup'), ('gpio.input', 'input'), ('gpio.output', 'output')], max_length=30),
        ),
        migrations.AlterField(
            model_name='gpior1',
            name='param',
            field=models.CharField(choices=[('gpio.HIGH', 'HIGH'), ('gpio.LOW', 'LOW')], max_length=30),
        ),
        migrations.AlterField(
            model_name='gpior2',
            name='command',
            field=models.CharField(choices=[('gpio.setmode', 'setmode_BOARD'), ('gpio.setmode', 'setmode_BCM'), ('gpio.setup', 'setup'), ('gpio.input', 'input'), ('gpio.output', 'output')], max_length=30),
        ),
        migrations.AlterField(
            model_name='gpior2',
            name='param',
            field=models.CharField(choices=[('gpio.HIGH', 'HIGH'), ('gpio.LOW', 'LOW')], max_length=30),
        ),
    ]
