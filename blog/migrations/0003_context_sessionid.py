# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-22 18:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170122_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='sessionid',
            field=models.TextField(default=datetime.datetime(2017, 1, 22, 18, 2, 9, 201998), max_length=32),
            preserve_default=False,
        ),
    ]
