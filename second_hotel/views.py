from django.shortcuts import render,redirect
from .models import Room,Booking,Customerrs,Message
from.forms import AvailabilityForm,RoomForm,BookingForm,CustomerForm,MessageForm,ContactForm
from second_hotel.booking_functions.availability import check_availability
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from.decorators import unauthenticated_user,allowed_users,admin_only,verified_user
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
@verified_user
def dashboard(request):
    return render(request,"second_app/dashboard.html")    


  
@login_required(login_url='login')
@verified_user
def roombooking(request):
    return render(request,"second_app/roombooking.html")    

@login_required(login_url='login')
@verified_user
def reservation(request):
    return render(request,"second_app/reservation.html")  

@login_required(login_url='login')
@verified_user
def viewrooms(request):
    rooms = Room.objects.all()

    context = {
        "rooms": rooms,
    }
    

    return render(request,"second_app/viewrooms.html",context)    

@login_required(login_url='login')
@admin_only
@verified_user
def admindashboard(request):
    return render(request,"second_app/admindashboard.html")  

@login_required(login_url='login')
@verified_user
def rooms_list(request):
    rooms = Room.objects.all()

    context = {
        "rooms": rooms,
    }
    return render(request,"second_app/rooms_list.html",context) 


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@verified_user
def booking_list(request):
    house = Booking.objects.all()

    context = {
        "house": house,
    }
    return render(request,"second_app/booking_list.html",
                   context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@verified_user
def Add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rent')
    # context = {'form':form} 
    else:
        form = RoomForm()      
    return render(request,"second_app/addroom.html",
                   {'form': form}) 




    
class new(FormView):
    form_class = AvailabilityForm
    template_name = 'second_app/availiability.html'
    
    
    def form_valid(self,form):
        data = form.cleaned_data
        rent = Room.objects.filter(room_number=data['room_number'])
        available_rooms = []
        for room in rent:
            if check_availability(room, data['check_in'],data['check_out']):
                available_rooms.append(room)
        
        
        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                customerrs=self.request.user.customerrs,
                room=room, 
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return redirect ('book')
        else:
            return redirect("choose_room")   



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@verified_user
def room_delete(request, pk):
    rooms = Room.objects.get(id=pk)
    if request.method == "POST":
        rooms.delete()
        return redirect('rent')
    return render(request,"second_app/rooms_delete.html")    



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@verified_user

def room_edit(request, pk):
    rooms = Room.objects.get(id=pk)
    if request.method == "POST":
        form = RoomForm(request.POST,instance=rooms)
        if form.is_valid():
            form.save()
            return redirect('rent')
    else:
        form = RoomForm(instance=rooms)
    
    
    return render(request,"second_app/rooms_edit.html",{'form':form})  



@login_required(login_url='login')
@verified_user
def customer_bookings(request):
    moons = Booking.objects.filter(customerrs=request.user.customerrs)

    context = {
        "moons": moons,

    }
    return render(request,"second_app/customerbookings.html",context) 



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@verified_user
def customerrrs_list(request):
    customerslists = Customerrs.objects.all()

    context = {
        "customerslists": customerslists,
    }
    return render(request,"second_app/customerslisting.html",
                   context) 


@login_required(login_url='login')
@verified_user
def customerrrs_profile(request):
    customerslists = Customerrs.objects.all()

    context = {
        "customerslists": customerslists,
    }
    return render(request,"second_app/customersprofile.html",
                   context) 


@login_required(login_url='login')
@verified_user
def profile(request):
    customerrs = request.user.customerrs
    form = CustomerForm(instance=customerrs) 

    if request.method == "POST":
      
        
        form = CustomerForm(request.POST, request.FILES, instance=customerrs)
        if form.is_valid():
            form.save()
            customerrs.is_verfied = True
            customerrs.save()
            return redirect('login')
    
    return render(request,"second_app/profile.html",{'form': form}) 

@login_required(login_url='login')
@verified_user
def choose_room(request):
    return render(request,"second_app/bookagain.html") 


@login_required(login_url='login')
@verified_user
def book(request):
    return render(request,"second_app/keeping.html") 

@login_required(login_url='login')
@verified_user
def booking_delete(request, pk):
    house = Booking.objects.get(id=pk)
    if request.method == "POST":
        house.delete()
        return redirect('lack')
    return render(request,"second_app/booking_delete.html")    
   
    
@login_required(login_url='login')
@verified_user
def message(request):
    instance = Message.objects.filter(user=request.user).first()
    
    if request.method == "POST":
        form = MessageForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    else:
        form = MessageForm({'user': request.user})
        
    return render(request,"second_app/messages.html",{'form': form}) 
   
@login_required(login_url='login')  
@verified_user 
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message, contact_email, ['ocheesther008@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "second_app/contact.html", {'form': form})

@login_required(login_url='login')
@verified_user
def success(request):
     return render(request,"second_app/success.html") 
    
@login_required(login_url='login') 
@verified_user           
def payslip(request, pk):
    house = Booking.objects.get(id=pk)
    template_path = 'second_app/payslip.html'
    
    context = {
        "house": house,

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"' 
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

   


    










