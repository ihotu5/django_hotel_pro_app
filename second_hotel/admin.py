from django.contrib import admin
from.models import Room,Booking,Category,Status,Customerrs,Message
from django.contrib.auth.models import Group

admin.site.site_header ='ESTACY HOTEL DASHBOARD'

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_number', 'room_category','description','reference_code','price','status',)


class BookingAdmin(admin.ModelAdmin):
    list_display = ( 'customerrs','room','check_in','check_out',)
# Register your models here.
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Customerrs)
admin.site.register(Message)
