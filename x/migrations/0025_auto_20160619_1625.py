# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-19 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0024_temperature_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='GpioR1',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='sensor',
        ),
        migrations.AlterField(
            model_name='gpior2',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='x.Room'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='x.Room'),
        ),
    ]
