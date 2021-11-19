from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customerrs



def create_profile(sender, instance,created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customerrs.objects.create(
            user=instance,
            name =instance.username,
           )
        print('Profile Created')
post_save.connect(create_profile, sender=User)

    