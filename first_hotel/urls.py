from django.urls import path
from .views import index, register,login_request,logout_request
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',index, name = 'index'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('register',register, name = 'register'),
    # path('rooms',rooms, name = 'rooms'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="first_app/password_reset.html"), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="first_app/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="first_app/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="first_app/password_reset_done.html"), name="password_reset_complete"),
]