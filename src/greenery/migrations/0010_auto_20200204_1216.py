# Generated by Django 3.0.2 on 2020-02-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenery', '0009_greenery_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='greenery',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='greenery',
            name='slug',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
    ]
