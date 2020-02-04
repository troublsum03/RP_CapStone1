# Generated by Django 3.0.2 on 2020-02-03 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenery', '0004_greenery_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greenery',
            name='image',
        ),
        migrations.AddField(
            model_name='greenery',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='greenery/'),
        ),
    ]