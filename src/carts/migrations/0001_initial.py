# Generated by Django 3.0.2 on 2020-02-05 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('greenery', '0013_greenery_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('greenery', models.ManyToManyField(blank=True, to='greenery.Greenery')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]