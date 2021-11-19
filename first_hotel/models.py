from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import User

#Create your models here.

# class Room(models.Model):
#     ROOM_CATEGORIES=(
#         ('DEL', 'DELUXE'),
#         ('GUS', 'GUEST'),
#         ('LUX', 'LUXURY'),
#         ('SIG', 'SINGLE'),
#     )
#     room_number = models.IntegerField()
#     categories = models.CharField(max_length=3, choices= ROOM_CATEGORIES)
#     beds =  models.IntegerField()
#     capacity =  models.IntegerField()
#     is_available = models.BooleanField(default=True)

#     def __str__(self):
#         return f'  {self.room_number}.  {self.categories} with   {self.beds}   beds   for  {self.capacity} people'



# class Booking(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     check_in = models.DateTimeField()
#     check_out = models.DateTimeField()

#     def __str__(self):
#         return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'


class User(models.Model):
    username=models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,null=True)


    def __str__(self):
        return self.username


class Second(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    


    def __str__(self):
        return self.username
