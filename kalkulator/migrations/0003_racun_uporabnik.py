# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 13:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kalkulator', '0002_auto_20161221_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='uporabnik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
