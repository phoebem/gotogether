# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-18 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotogether', '0004_auto_20161218_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='distance',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='options',
            name='points',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='options',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
