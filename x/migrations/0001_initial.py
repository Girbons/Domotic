# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gpio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GpioR1',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('pin', models.IntegerField(choices=[(0, 0), (1, 1), (4, 4), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (14, 14), (15, 15), (18, 18), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25)])),
                ('command', models.CharField(max_length='30', choices=[('gpio.setmode', 'setmode'), ('gpio.setup', 'setup'), ('gpio.input', 'input'), ('gpio.output', 'output')])),
                ('param', models.CharField(max_length='30', choices=[('gpio.HIGH', 'HIGH'), ('gpio.LOW', 'LOW')])),
            ],
        ),
        migrations.CreateModel(
            name='GpioR2',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('pin', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (14, 14), (15, 15), (17, 17), (18, 18), (22, 22), (23, 23), (24, 24), (25, 25)])),
                ('command', models.CharField(max_length='30', choices=[('gpio.setmode', 'setmode'), ('gpio.setup', 'setup'), ('gpio.input', 'input'), ('gpio.output', 'output')])),
                ('param', models.CharField(max_length='30', choices=[('gpio.HIGH', 'HIGH'), ('gpio.LOW', 'LOW')])),
            ],
        ),
    ]
