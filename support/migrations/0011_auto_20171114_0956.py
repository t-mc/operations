# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0010_auto_20170929_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cases',
            name='bedrijf',
        ),
        migrations.RemoveField(
            model_name='cases',
            name='contact',
        ),
    ]
