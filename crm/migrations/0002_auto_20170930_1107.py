# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-30 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bedrijf',
            name='adres',
        ),
        migrations.AddField(
            model_name='adres',
            name='bedrijf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Bedrijf'),
        ),
    ]