# Generated by Django 3.1.2 on 2021-01-05 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('starting_address', models.CharField(max_length=100)),
                ('ending_address', models.CharField(max_length=100)),
            ],
        ),
    ]
