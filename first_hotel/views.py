from django.shortcuts import render,redirect
# from .models import Room, Booking
# from django.forms import modelform_factory
from .forms import UserForm,SecondForm
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from second_hotel.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.decorators import login_required
from second_hotel.models import Customerrs
from second_hotel.signals import create_profile  
from django.contrib.auth.models import Group
# # Create your views here.



def index(request):
    return render(request,"first_app/index.html")


@unauthenticated_user
def login_request(request):
    form = SecondForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
           
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("admindashboard")
            else:
                
                form = SecondForm()
                messages.info(request, 'Username or Password is incorrect')
                
    return render(request, 'first_app/login.html', {'form': form})
         
def logout_request(request):
    logout(request)
    return redirect('index')

@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
           user= form.save()
           username = form.cleaned_data.get('username')
           
           
           

           

            
           
           messages.success(request,'Account was created for ' + username)
           
           
           login(request, user)
           return redirect('/profile/')
    else:
        form = UserForm()    
    return render(request, 'first_app/register.html',{'form': form})

    

# BookingForm = modelform_factory(Booking, exclude=[])

# def rooms(request):

#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     else:
#         form = BookingForm()
#     return render(request,"first_app/rooms.html",{"form": form})
