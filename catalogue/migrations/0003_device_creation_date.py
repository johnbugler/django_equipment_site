# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-12 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_device_researcher'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
