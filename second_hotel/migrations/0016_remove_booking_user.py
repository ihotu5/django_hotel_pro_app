# Generated by Django 3.2.4 on 2021-10-11 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_hotel', '0015_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
