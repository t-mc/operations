# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projecten', '0008_auto_20180322_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='verkoopkans',
            name='geschatte_omzet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='verkoopkans',
            name='werkelijke_omzet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
