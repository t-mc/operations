# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projecten', '0003_auto_20171006_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='omschrijving',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='verkoopkans',
            name='omschrijving',
            field=models.CharField(max_length=160),
        ),
    ]
