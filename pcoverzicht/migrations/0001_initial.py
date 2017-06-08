# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-06 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=40, unique=True)),
                ('gebruiker', models.CharField(max_length=80)),
                ('merkentype', models.CharField(max_length=80, verbose_name='Merk en Type')),
                ('kenmerken', models.TextField()),
                ('aanschafdatum', models.DateField()),
                ('serienummer', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Computers',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(max_length=80)),
                ('versienummer', models.CharField(max_length=20)),
                ('productkey', models.CharField(blank=True, max_length=40)),
                ('naam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcoverzicht.Computer', verbose_name='PC Naam')),
            ],
            options={
                'verbose_name_plural': 'Software',
            },
        ),
    ]