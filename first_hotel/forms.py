
from django import forms
# from django.forms import ModelChoiceField
from django.forms import ModelForm
# from.models import Booking
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _
from django.forms import PasswordInput
from django.core.exceptions import ValidationError
from. widgets import ShowHidePasswordWidget
from .models import Second





# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = '__all__'
       
class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password','email']
        error_messages = {
            'username': { 
                'unique': _("Please enter another username. This one is taken"),
            },
        }
        widgets = { 
           
            "password": ShowHidePasswordWidget,
            
            
        }
    


    def save(self, commit=True, *args,**kwargs):
        #m = super(UserForm, self).save(commit=False)
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()
        
        
        if commit:
            m.save()
        return m 




class SecondForm(ModelForm):
    
   
    class Meta:
        model = Second
        fields = ['username','password']
        
        widgets = { 
            #  "username": PlaceholderInput,
              #forms.TextInput(attrs={'placeholder': 'Username'}),
            "password": ShowHidePasswordWidget,
            
        }