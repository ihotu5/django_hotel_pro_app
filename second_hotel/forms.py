from django import forms
from .models import Room,Booking,Customerrs,Message
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminSplitDateTime

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class AvailabilityForm(forms.Form):
    ROOM_NUMBERS = (
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
    
    room_number = forms.ChoiceField(choices=ROOM_NUMBERS, required= True)
    # check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])
    # check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])
    
    check_in = forms.SplitDateTimeField(widget=AdminSplitDateTime)
    check_out = forms.SplitDateTimeField(widget=AdminSplitDateTime)



class CustomerForm(ModelForm):
    class Meta:
        model = Customerrs
        fields = '__all__'
        exclude = ['user']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields =  '__all__'
       
        
class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Contact Name', max_length=255)
    contact_email = forms.CharField(label='Contact Email',max_length=255)
    contact_message = forms.CharField(widget=forms.Textarea,required=True)
        
       




















    # class Meta:
    #     model = Booking
    #     fields =['room','check_out','check_in']

    # def form_valid(self,form):
    #     data = form.clean_data
    #     rent = Room.objects.filter(category=data['room_number'])
    #     available_rooms = []
    #     for room in rent:
    #         if check_availability(room, data['check_in'],data['check_out']):
    #             available_rooms.append(room)
        
        
    #     if len(available_rooms) > 0:
    #         room = available_rooms[0]
    #         booking = Booking.objects.create(
    #             user= self.request.user,
    #             room=room,
    #             check_in=data['check_out'],
    #             check_out=data['check_out']
    #         )
    #         booking.save()
    #         return HttpResponse(booking)
    #     else:
    #         return HttpResponse('all this room has been booked')   


        
        
        


    