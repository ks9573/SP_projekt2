# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 15:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0009_vnos_datum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vnos',
            name='datum',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
