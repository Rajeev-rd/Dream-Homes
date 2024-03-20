from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.views.generic import View, FormView
from .forms import AppointmentRequestForm,TestimonialForm
from .models import Testimonial
from django.contrib.auth.decorators import login_required
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
    return redirect("indexfront")

#function for index of user view
def indexfront(request):
    testimonials = Testimonial.objects.all()  # Fetch all testimonials from the database
    return render(request, "frontendindexpage.html", {'testimonials': testimonials})

#function for about page

def about(request):
    return render(request,"about.html")

#function for service page
def service(request):
    testimonials = Testimonial.objects.all()  # Fetch all testimonials from the database
    return render(request,"service.html", {'testimonials': testimonials})

#function for projects page
def projects(request):
    return render(request,"projects.html")

#function for contact page
def contact(request):
    return render(request,"contact.html")

#function for testimonial
def testimonial(request):
    return render(request,"testimonial.html")

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

def updatestatus(request):
    return render(request,"status.html")

#function for testimonial
def testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            # Assuming you want to associate the testimonial with the currently logged-in user
            if request.user.is_authenticated:
                form.instance.user = request.user
            else:
                # Set a default user or None if no user is logged in
                form.instance.user = None

            form.save()
            return redirect('testimonial')
    else:
        form = TestimonialForm()

    testimonials = Testimonial.objects.all()
    context = {'testimonials': testimonials, 'form': form}
    return render(request, 'testimonial.html', context)


@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            # Assuming you want to associate the testimonial with the currently logged-in user
            if request.user.is_authenticated:
                form.instance.user = request.user
            else:
                # Set a default user or None if no user is logged in
                form.instance.user = None

            form.save()
            return redirect('testimonial')
    else:
        form = TestimonialForm()
    return render(request, 'add_testimonial.html', {'form': form})

def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    if request.method == 'POST' and request.user == testimonial.user:
        testimonial.delete()
    return redirect('testimonial')

def status(request):
    return render(request,'status.html')

