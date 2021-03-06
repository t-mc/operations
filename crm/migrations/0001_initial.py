# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 14:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_dt', models.DateTimeField(auto_now=True, null=True)),
                ('adrestype', models.CharField(choices=[('P', 'Postadres'), ('B', 'Bezoekadres')], max_length=1)),
                ('adresregel_1', models.CharField(max_length=80, null=True)),
                ('adresregel_2', models.CharField(blank=True, max_length=80, null=True)),
                ('postcode', models.CharField(max_length=7, null=True)),
                ('plaats', models.CharField(max_length=80, null=True)),
                ('Land', models.CharField(max_length=80, null=True)),
                ('last_modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Laatst gewijzigd door')),
            ],
            options={
                'verbose_name_plural': 'Adressen',
            },
        ),
        migrations.CreateModel(
            name='Bedrijf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_dt', models.DateTimeField(auto_now=True, null=True)),
                ('bedrijfsnaam', models.CharField(max_length=120, unique=True)),
                ('telefoonnummer', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=75, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('kvk_nummer', models.CharField(blank=True, max_length=20, null=True)),
                ('onenote', models.URLField(blank=True, max_length=400, null=True)),
                ('actief', models.BooleanField(default=True)),
                ('adres', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Adres')),
            ],
            options={
                'verbose_name_plural': 'Bedrijven',
                'ordering': ['bedrijfsnaam'],
            },
        ),
        migrations.CreateModel(
            name='Branche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_dt', models.DateTimeField(auto_now=True, null=True)),
                ('branch', models.CharField(max_length=80, unique=True)),
                ('last_modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Laatst gewijzigd door')),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Contactpersoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_dt', models.DateTimeField(auto_now=True, null=True)),
                ('volledige_naam', models.CharField(max_length=120)),
                ('initialen', models.CharField(max_length=20)),
                ('voornaam', models.CharField(max_length=120)),
                ('tussenvoegsel', models.CharField(blank=True, max_length=120, null=True)),
                ('achternaam', models.CharField(max_length=120)),
                ('telefoonnummer', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('mobielnummer', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('functie', models.CharField(blank=True, max_length=120, null=True)),
                ('afdeling', models.CharField(blank=True, max_length=120, null=True)),
                ('assistent', models.CharField(blank=True, max_length=120, null=True)),
                ('manager', models.CharField(blank=True, max_length=120, null=True)),
                ('overige_contactgegevens', models.CharField(blank=True, max_length=120, null=True)),
                ('actief', models.BooleanField(default=True)),
                ('sexe', models.CharField(choices=[('M', 'Man'), ('V', 'Vrouw'), ('O', 'Onbekend')], default='O', max_length=1, verbose_name='geslacht')),
                ('bedrijf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Bedrijf')),
                ('last_modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Laatst gewijzigd door')),
                ('standplaats', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Adres')),
            ],
            options={
                'verbose_name_plural': 'Contactpersonen',
                'ordering': ['volledige_naam'],
            },
        ),
        migrations.AddField(
            model_name='bedrijf',
            name='branche',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Branche'),
        ),
        migrations.AddField(
            model_name='bedrijf',
            name='klantpartner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Klantpartner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bedrijf',
            name='last_modified_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Laatst gewijzigd door'),
        ),
    ]
