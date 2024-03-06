from django.shortcuts import render,redirect
from .models import RegistrationDb
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from Adminmodule.views import index
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout as django_logout

# Create your views here.

# function for signup
def signup(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if password and confirm_password match
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, 'signuppage.html', {'error_message': error_message})
        
        if RegistrationDb.objects.filter(email=email).exists():
            return render(request,'signuppage.html',{'error_message':'Email already exists'})
        
        try:
            # Attempt to create a new RegistrationDb instance
            RegistrationDb.objects.create(
                name=name,
                email=email,
                mobile=mobile,
                password=password
            )
            # If successful, redirect to success page or any desired page
            return redirect('indexfront')
        except ValidationError as e:
            # If validation error occurs due to uniqueness constraint, display error message
            error_message = str(e)
            return render(request, 'signuppage.html', {'error_message': error_message})
     else:
        return render(request,"signuppage.html")
#function for login
def logins(request):
    return render(request,"loginpage.html")

#function login admin and user
def loginusers(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        if RegistrationDb.objects.filter(name=username,password=password).exists():
            request.session['username']=username
            request.session['password'] = password
            request.session['is_admin'] = False
            return redirect('indexfront')
        elif User.objects.filter(username__contains=username).exists():
             user=authenticate(username=username, password=password)
             if user is not None:
                 login(request,user)
                 request.session['username'] = username
                 request.session['password'] = password
                 request.session['is_admin'] = True
                 return redirect('index')
             else:
                 messages.error(request, "Incorrect password. Please try again.")
                 return redirect('logins')
        else:
            messages.error(request, "Username is incorrect. Please try again.")
            return redirect('logins')
    else:
        return redirect('logins')
    
def myview(request):
    user_logged_in = RegistrationDb.objects.exists()
    return render(request,"frontendindexpage.html", {'user_is_logged_in':user_is_logged_in})

def check_authentication(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True})
    else:
        return JsonResponse({'authenticated': False})
    
def logout(request):
    # Log out the user using Django's logout function
    django_logout(request)
    return JsonResponse({'message': 'Logged out successfully'})

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