# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0006_auto_20170504_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activiteiten',
            name='tijdsduur',
        ),
        migrations.DeleteModel(
            name='Tijdsduur',
        ),
    ]
