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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='GpioR1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(default=b'type the configuration name', max_length=50)),
                ('pin', models.IntegerField(choices=[(0, 0), (1, 1), (4, 4), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (14, 14), (15, 15), (18, 18), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25)])),
                ('action', models.CharField(default=b'', max_length=30, choices=[(b'toggle light', b'toggle light')])),
            ],
        ),
        migrations.CreateModel(
            name='GpioR2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(default=b'type the configuration name  ', max_length=50)),
                ('pin', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (14, 14), (15, 15), (17, 17), (18, 18), (22, 22), (23, 23), (24, 24), (25, 25)])),
                ('action', models.CharField(default=b'', max_length=30, choices=[(b'toggle light', b'toggle light')])),
                ('rele', models.IntegerField(choices=[(1, 1), (2, 2), (4, 4), (8, 8), (16, 16), (32, 32)])),
            ],
        ),
    ]
