# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0005_auto_20150909_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpior2',
            name='text',
            field=models.CharField(max_length=50, default='type the configuration name  '),
        ),
    ]
