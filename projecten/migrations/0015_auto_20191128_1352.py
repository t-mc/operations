# Generated by Django 2.0.4 on 2019-11-28 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projecten', '0014_auto_20191128_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urenpermedewerker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_dt', models.DateTimeField(auto_now=True, null=True)),
                ('jaar', models.IntegerField(choices=[(1, '2018'), (2, '2019'), (3, '2020'), (4, '2021'), (5, '2022'), (6, '2023'), (7, '2024'), (8, '2025'), (9, '2026'), (10, '2027')])),
                ('maand', models.IntegerField(choices=[(1, 'Januari'), (2, 'Februari'), (3, 'Maart'), (4, 'April'), (5, 'Mei'), (6, 'Juni'), (7, 'Juli'), (8, 'Augustus'), (9, 'September'), (10, 'Oktober'), (11, 'November'), (12, 'December')])),
                ('uren', models.PositiveSmallIntegerField()),
                ('last_modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Laatst gewijzigd door')),
                ('medewerker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Medewerker_Order', to=settings.AUTH_USER_MODEL)),
                ('projectcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Urenpermedewerker_Order', to='projecten.Verkoopkans')),
            ],
            options={
                'verbose_name_plural': 'Uren per medewerker',
                'ordering': ['medewerker', 'jaar', 'maand'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='urenpermedewerker',
            unique_together={('medewerker', 'projectcode', 'jaar', 'maand')},
        ),
    ]
