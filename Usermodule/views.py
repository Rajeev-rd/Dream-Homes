from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.views.generic import View, FormView
from .forms import AppointmentRequestForm,TestimonialForm
from .models import Testimonial,Order_Address
from django.contrib.auth.decorators import login_required
from Adminmodule.models import Balance,Category,Payment
import razorpay
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
    datas = Balance.objects.all()
    cate = Category.objects.all()
    testimonials = Testimonial.objects.all()  # Fetch all testimonials from the database
    return render(request, "frontendindexpage.html", {'testimonials': testimonials,'datas':datas,'cate':cate})

#function for about page
def about(request):
    cate = Category.objects.all()
    return render(request,"about.html",{'cate':cate})

#function for service page
def service(request):
    cate = Category.objects.all()
    testimonials = Testimonial.objects.all()  # Fetch all testimonials from the database
    return render(request,"service.html",{'testimonials': testimonials,'cate':cate})

#function for projects page
def projects(request):
    return render(request,"projects.html")

#function for contact page
def contact(request):
    cate = Category.objects.all()
    return render(request,"contact.html",{'cate':cate})

#function for testimonial
def testimonial(request):
    return render(request,"testimonial.html")

#function to send the request to message
def submit_request(request):
    category_id = request.GET.get('category_id')
    category = None
    if category_id:
        category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            appointment_request = form.save(commit=False)
            if category:
                appointment_request.service = category
            appointment_request.save()
            return redirect('indexfront')
    else:
        form = AppointmentRequestForm()
    
    return render(request, 'frontendindexpage.html', {'form': form, 'category': category})


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

#function of payment
@login_required
def checkout(request, balance_item_id):
    balance_item = Balance.objects.get(id=balance_item_id)
    amount_in_paise = balance_item.price * 100
    return render(request, 'payment.html', {'balance_item': balance_item, 'amount_in_paise': amount_in_paise})

@login_required
def make_payment(request):
    if request.method == 'POST':
        # Retrieve balance_item_id from the POST data
        balance_item_id = request.POST.get('balance_item_id')
        
        if balance_item_id:
            # Get the Balance object using the balance_item_id
            try:
                balance_item = Balance.objects.get(id=balance_item_id)
            except Balance.DoesNotExist:
                # Handle case where Balance object does not exist for the given ID
                return HttpResponseBadRequest("Invalid balance_item_id")
            
            # Process payment using Razorpay
            # For simplicity, let's assume the payment is successful
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_IzIBFTmzd3zzKk', 'mMvIdZd7a4EU1pMd9tSQEbE0'))
            payment = client.order.create({'amount': int(balance_item.price * 100), 'currency': "INR", 'payment_capture': '1'})
            
            # Return payment details
            return JsonResponse({'payment': payment})
        else:
            return HttpResponseBadRequest("balance_item_id is required")
    else:
        return redirect('indexfront')

    

def checkout_Address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        
        # Create and save the Address object
        address_obj = Order_Address.objects.create(
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
        )
        address_obj.save()
        
        # return redirect('indexfront')  # Redirect to a success page
    return render(request, 'payment.html')
