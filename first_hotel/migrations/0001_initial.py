# Generated by Django 3.2.4 on 2021-06-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('categories', models.CharField(choices=[('DEL', 'DELUXE'), ('GUS', 'GUEST'), ('LUX', 'LUXURY'), ('SIG', 'SINGLE')], max_length=3)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
