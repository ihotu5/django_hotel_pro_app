# Generated by Django 3.2.4 on 2021-06-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_hotel', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
