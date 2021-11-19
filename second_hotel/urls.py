from django.urls import path
from .views import dashboard,roombooking,reservation,admindashboard,rooms_list,booking_list,new,Add_room,viewrooms,room_delete,room_edit,customer_bookings,customerrrs_list,customerrrs_profile,profile,choose_room,book,booking_delete, message,contact,success,payslip
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
   
    path('dashboard',dashboard, name="dashboard"),
    path('roombooking',roombooking, name="roombooking"),
    path('resrvation',reservation, name="reservation"),
    path('admindashboard',admindashboard, name="admindashboard"),
    path('lack/',booking_list, name="lack"),
    path('rent/',rooms_list, name="rent"),
    path('new',new.as_view(), name="new"),
    path('Add_room',Add_room, name="Add_room"),
    path('viewrooms',viewrooms, name="loss"),
    path('room/delete/<int:pk>/', room_delete, name="admin-room-delete"),
    path('room/edit/<int:pk>/', room_edit, name="admin-room-edit"),
    path('customer/', customer_bookings, name="customer"),
    path('customerrrs_list/', customerrrs_list, name="customerrrs_list"),
    path('customerrrs_profile/', customerrrs_profile, name="customerrrs_profile"),
    path('profile/', profile, name="profile"),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('choose_room/', choose_room, name="choose_room"),
    path('book/', book, name="book"),
    path('booking/delete/<int:pk>/', booking_delete, name="admin-booking-delete"),
    path('contact/', contact, name="contact"),
    path('message/', message, name="message"),
    path('success/', success, name="success"),
    path('payslip/<int:pk>/', payslip, name="payslip"),
   
   
]
