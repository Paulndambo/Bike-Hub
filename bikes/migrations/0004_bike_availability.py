# Generated by Django 4.0.2 on 2022-02-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_bike_rental_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='availability',
            field=models.CharField(default='1', max_length=200),
        ),
    ]
