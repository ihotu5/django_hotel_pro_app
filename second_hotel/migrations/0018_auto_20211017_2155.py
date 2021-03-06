# Generated by Django 3.2.4 on 2021-10-17 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('second_hotel', '0017_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrs',
            name='is_updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moons', to='auth.user'),
        ),
    ]
