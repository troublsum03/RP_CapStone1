# Generated by Django 3.0.2 on 2020-01-31 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenery',
            name='price',
            field=models.DecimalField(decimal_places=2, default=30.0, max_digits=20),
        ),
    ]
