# Generated by Django 2.0.4 on 2019-12-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projecten', '0017_orderregel'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderregel',
            name='list_prijs',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='orderregel',
            name='selling_prijs',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
