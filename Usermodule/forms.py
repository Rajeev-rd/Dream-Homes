from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AppointmentRequest,Testimonial

class RegistrationForm(UserCreationForm):
   password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
   password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

   class Meta:
    model=User
    fields=["username","email","password1","password2"]   

    
    widgets = {
    'username': forms.TextInput(attrs={'class': 'form-control '}),
    'email': forms.EmailInput(attrs={'class': 'form-control'}),
  
    
} 

class LoginForm(forms.Form):
   username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = AppointmentRequest
        fields = ['name', 'email', 'message', 'location']
        widgets = {
            'location': forms.HiddenInput(),  # Assuming location is a required field
        }
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content']
