# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0018_auto_20160505_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpior2',
            name='image',
        ),
        migrations.RemoveField(
            model_name='gpior2',
            name='version',
        ),
        migrations.AlterField(
            model_name='gpior1',
            name='action',
            field=models.CharField(choices=[(b'toggle light', b'toggle light'), (b'temperature', b'temperature'), (b'lock', b'lock'), (b'camera', b'camera')], default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='gpior2',
            name='action',
            field=models.CharField(choices=[(b'toggle light', b'toggle light'), (b'temperature', b'temperature'), (b'lock', b'lock'), (b'camera', b'camera')], default=b'', max_length=30),
        ),
        migrations.DeleteModel(
            name='Icon',
        ),
    ]
