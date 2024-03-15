from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.views.generic import View, FormView
from .forms import AppointmentRequestForm
# Create your views here.

# function for signup
class RegistrationView(FormView):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'signuppage.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration successfully")
            return redirect('login')
        messages.error(request,"Please enter correct details")
        return render(request, 'signuppage.html', {"form": form})

#function for login
class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'loginpage.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    # Redirect superusers to admin page
                    return redirect('index')  # Replace 'admin_page' with your admin page URL name
                else:
                    return redirect('indexfront')  # Redirect regular users to index page
            else:
                messages.error(request, "Invalid credentials")
        return render(request, 'loginpage.html', {"form": form})



def signout_view(request,*args, **kwargs):
    logout(request)
    return redirect("login")

#function for index of user view
def indexfront(request):
    return render(request,"frontendindexpage.html")

#function for about page

def about(request):
    return render(request,"about.html")

#function for service page
def service(request):
    return render(request,"service.html")

#function for projects page
def projects(request):
    return render(request,"projects.html")

#function for contact page
def contact(request):
    return render(request,"contact.html")

#function to send the request to message
def submit_request(request):
    if request.method == 'POST':
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            # Create a new AppointmentRequest object but don't save it yet
            appointment_request = form.save(commit=False)
            # Optionally, you can modify or add more data to the appointment_request object here
            
            # Now save the form data to the database
            appointment_request.save()
            
            # Redirect to a success page
            return redirect('indexfront')
    else:
        form = AppointmentRequestForm()
    
    return render(request, 'frontendindexpage.html', {'form': form})