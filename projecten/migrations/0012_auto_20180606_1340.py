# Generated by Django 2.0.4 on 2018-06-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projecten', '0011_omzetpermaand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='omzetpermaand',
            options={'ordering': ['jaar', 'maand'], 'verbose_name_plural': 'Omzetten per maand'},
        ),
        migrations.AlterField(
            model_name='omzetpermaand',
            name='maand',
            field=models.IntegerField(choices=[(1, 'Januari'), (2, 'Februari'), (3, 'Maart'), (4, 'April'), (5, 'Mei'), (6, 'Juni'), (7, 'Juli'), (8, 'Augustus'), (9, 'September'), (10, 'Oktober'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='omzetpermaand',
            name='omzet',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Omzet in euro's"),
        ),
        migrations.AlterUniqueTogether(
            name='omzetpermaand',
            unique_together={('projectcode', 'jaar', 'maand')},
        ),
    ]
