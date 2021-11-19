from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Room(models.Model):
    ROOM_NUMBERS=(
        ('001', '001'),
        ('002', '002'),
        ('003', '003'),
        ('004', '004'),
        ('005', '005'),
        ('006', '006'),
        ('007', '007'),
        ('008', '008'),
        ('009', '009'),
        ('010', '010'),
        ('011', '011'),
        ('012', '012'),
        ('013', '013'),
        ('014', '014'),
        ('015', '015'),
        ('016', '016'),
        ('017', '017'),
        ('018', '018'),
        ('019', '019'),
        ('020', '020'),
    )
    # STATUS=[
    #     ('pending', 'pending'),
    #     ('available', 'available'),
    #     ('unavailable', 'unavailable'),
    #     ('comfirmed', 'confirmed'),
    
    # ]
    # ROOM_CATEGORIES=[
    #     ('DELUXE', 'DELUXE'),
    #     ('GUEST', 'GUEST'),
    #     ('LUXURY', 'LUXURY'),
    #     ('SIGLE', 'SINGLE'),
    # ]
    room_id = models.IntegerField() 
    room_number = models.CharField(max_length=15,choices= ROOM_NUMBERS)
    room_category = models.ForeignKey('Category', on_delete=models.CASCADE,default=False )
    description =  models.TextField()
    reference_code =  models.IntegerField()
    price = models.IntegerField()
    status = models.ForeignKey('Status',on_delete=models.CASCADE,default=False )


    class Meta:
        verbose_name_plural = 'Rooms'


    def __str__(self):
        return f' Room {self.room_number}.{self.room_category} Price {self.price}'



class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='moons')
    customerrs = models.ForeignKey('Customerrs', null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Room Booking'

    

    def __str__(self):
        return f'{self.user}.{self.customerrs} has booked {self.room} from {self.check_in} to {self.check_out} '


class Status(models.Model):
    STATUS=(
        ('pending', 'pending'),
        ('available', 'available'),
        ('unavailable', 'unavailable'),
        ('comfirmed', 'confirmed'),
    )
    status = models.CharField(max_length=20, choices= STATUS)

    class Meta:
        verbose_name_plural = 'Room Status'


    def __str__(self):
        return self.status





class Category(models.Model):
    ROOM_CATEGORIES=(
        ('DELUXE', 'DELUXE'),
        ('GUEST', 'GUEST'),
        ('LUXURY', 'LUXURY'),
        ('SINGLE', 'SINGLE'),
    )
    categories = models.CharField(max_length=10,choices= ROOM_CATEGORIES)

    class Meta:
        verbose_name_plural = ' Room Category'

    def __str__(self):
        return self.categories

class Customerrs(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone_no = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    nationality = models.CharField(max_length=200,null=True)
    is_verfied = models.BooleanField(default= False)

    def __str__(self):
        return self.name or ''

class Message(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    message = models.TextField()


    def __str__(self):
        return f'{self.user}.{self.message}'
    

   



# class Room(models.Model):
# ROOM_CATEGORIES=(
#         ('DEL', 'DELUXE'),
#         ('GUS', 'GUEST'),
#         ('LUX', 'LUXURY'),
#         ('SIG', 'SINGLE'),
#     )
#     room_id = models.IntegerField() 
#     room_number = models.IntegerField()
#     categories = models.CharField(max_length=3, choices= ROOM_CATEGORIES)
#     description =  models.CharField()
#     reference_code =  models.IntegerField()
#     price = models.IntegerField()
#     status = models.CharField(max_length=3, choices= STATUS)











