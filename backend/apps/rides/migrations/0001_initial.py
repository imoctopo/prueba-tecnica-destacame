# Generated by Django 3.1.2 on 2021-01-05 00:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routes', '0001_initial'),
        ('buses', '0001_initial'),
        ('passengers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides', to='buses.bus')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides', to='routes.route')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='passengers.passenger')),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='rides.ride')),
            ],
        ),
    ]
