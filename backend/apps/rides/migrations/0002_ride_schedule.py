# Generated by Django 3.1.2 on 2021-01-05 02:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='schedule',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]