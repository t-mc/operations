# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projecten', '0006_auto_20171207_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='geschatte_omzet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='werkelijke_omzet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='verkoopkans',
            name='geschatte_omzet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='verkoopkans',
            name='werkelijke_omzet',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
