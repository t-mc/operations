# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20171002_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpersoon',
            name='achternaam',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='contactpersoon',
            name='initialen',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactpersoon',
            name='voornaam',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
