from operator import attrgetter
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError, JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.views.generic import View, FormView
from .forms import AppointmentRequestForm,TestimonialForm
from .models import AppointmentRequest, Testimonial,Order_Address
from django.contrib.auth.decorators import login_required
from Adminmodule.models import AdvancePay, Balance,Category, FullPay, Message,Payment, Property,Renovation,Interior, Status
import razorpay
import logging
from django.http import HttpResponse
from django.db.models import Max

# Create your views here.

logger = logging.getLogger(__name__)

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
    try:
        # Attempt to fetch data from the database
        datas = Balance.objects.all()
        cate = Category.objects.all()
        Pro = Property.objects.all()
        Int = Interior.objects.all()
        Reno = Renovation.objects.all()
        testimonials = Testimonial.objects.all()

        # Render the template with the fetched data
        return render(request, "frontendindexpage.html", {'testimonials': testimonials, 'datas': datas, 'cate': cate,'Pro':Pro,"Int":Int,"Reno":Reno})
    except Exception as e:
        # Log the error for debugging purposes
        logger.error(f"An error occurred while fetching data: {e}")
        # Check if the user is authenticated and is_staff (admin)
        if request.user.is_authenticated and request.user.is_staff:
            # If the user is authenticated and is_staff, return the error response
            return HttpResponseServerError("An error occurred. Please try again later.")
        else:
            # If the user is not authenticated or is not an admin, return a forbidden response
            return HttpResponseForbidden("You are not authorized to view this page.")
    
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
    cate = Category.objects.all()
    Pro = Property.objects.all()
    Int = Interior.objects.all()
    Reno = Renovation.objects.all()
    return render(request,"projects.html",{'cate':cate,'Pro':Pro,"Int":Int,"Reno":Reno})

#function for contact page
def contact(request):
    cate = Category.objects.all()
    Pro = Property.objects.all()
    Int = Interior.objects.all()
    Reno = Renovation.objects.all()
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

# def status(request):
#     return render(request,'status.html')

def status(request):
    latest_updates = Status.objects.values('details').annotate(latest_id=Max('id'))
    data = []
    for update in latest_updates:
        latest_update = Status.objects.filter(details=update['details'], id=update['latest_id']).first()
        data.append(latest_update)
    return render(request, "status.html", {"data": data})



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
                return JsonResponse({'success': False, 'message': 'Invalid balance_item_id'})
            
            # Process payment using Razorpay
            # For simplicity, let's assume the payment is successful
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_IzIBFTmzd3zzKk', 'mMvIdZd7a4EU1pMd9tSQEbE0'))
            payment = client.order.create({'amount': int(balance_item.price * 100), 'currency': "INR", 'payment_capture': '1'})
            
            # Return success response
            return JsonResponse({'success': True, 'message': 'Payment successful'})
        else:
            return JsonResponse({'success': False, 'message': 'balance_item_id is required'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    

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

def message_user(request, dataid):
    current_user = request.user
    msg = AppointmentRequest.objects.filter(name=dataid)

    data = Message.objects.all()

    all_msgs = sorted(
        data,
        key=attrgetter('timestamp'),
        reverse=True
    )
    return render(request, 'message_user.html', {"data": data, "all_msgs": all_msgs, "msg": msg})


#function for construction single page
def bltcntsingle(request, property_id):
    # Retrieve the specific property from the database
    property = get_object_or_404(Property, pk=property_id)

    # Pass the property to the template
    return render(request, "bldcnst_single.html", {'property': property})

def initiate_payment(request, property_id):
    if request.method == "POST":
        property = get_object_or_404(Property, pk=property_id)
        amount = 100000  # Set the amount to 1000 INR (100,000 paisa)
        client = razorpay.Client(auth=("rzp_test_IzIBFTmzd3zzKk", "mMvIdZd7a4EU1pMd9tSQEbE0"))  # Replace with your Razorpay keys
        payment_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'receipt#1',
            'payment_capture': 1  # Auto capture
        }
        payment = client.order.create(data=payment_data)
        return JsonResponse({'property_id': property_id, 'amount': amount, 'id': payment.get('id')})

def download_plan(request, property_id):
    # Retrieve the specific property from the database
    property = get_object_or_404(Property, pk=property_id)
    
    # Check if the user has made the payment
    if user_has_paid(request.user, property_id):  # Check if user has paid
        # Check if the property has a plan image
        if property.plan_image:
            # Open the plan image file
            with open(property.plan_image.path, 'rb') as f:
                # Create a response to serve the image as a file download
                response = HttpResponse(f.read(), content_type='image/jpeg')
                response['Content-Disposition'] = 'attachment; filename="plan_image.jpg"'
                return response
    else:
        # Redirect user to payment page if not paid
        return redirect('initiate_payment', property_id=property_id)

def user_has_paid(user, property_id):
    # Implement logic to check if user has paid for the property plan
    # This could involve querying your database for payment status
    return True  # Example implementation, replace with actual logic
def bltcntafterpayment(request, property_id):
    # Retrieve the specific property from the database
    property = get_object_or_404(Property, pk=property_id)

    # Pass the property to the template
    return render(request, "bldcnst_afterpayment.html", {'property': property})

#function for Interior single page
def Interiorsingle(request, Interior_id):
    # Retrieve the specific property from the database
    Interiors = get_object_or_404(Interior, pk=Interior_id)

    # Pass the property to the template
    return render(request, "interior_single.html", {'Interior': Interiors})

#function for Renovation single page
def Renovationsingle(request, Reno_id):
    # Retrieve the specific property from the database
    Renovations = get_object_or_404(Renovation, pk=Reno_id)

    # Pass the property to the template
    return render(request, "reno_single.html", {'Renovation': Renovations})



def advance_payment_page(request):
    data=AdvancePay.objects.all()
    return render(request, "Advance_payment_page.html",{"data":data})

def advance_payment(request):
    if request.method == 'POST':
        adv_amount_id = request.POST.get('adv_amount_id')

        # if adv_amount_id:
        #     try:
        #         advance_bill = AdvancePay.objects.get(id=adv_amount_id)
        #     except AdvancePay.DoesNotExist:
        #         return JsonResponse({'success': False, 'message': 'Invalid advance bill ID'})
        if adv_amount_id:
            advance_bill = AdvancePay.objects.get(id=adv_amount_id)
            client = razorpay.Client(auth=('rzp_test_IzIBFTmzd3zzKk', 'mMvIdZd7a4EU1pMd9tSQEbE0'))
            amount_in_paise = int(advance_bill.AdvanceAmount * 100)
            payment = client.order.create({'amount': amount_in_paise, 'currency': 'INR', 'payment_capture': '1'})

          # Delete the bill from the database
            advance_bill.delete()

            # Assuming you want to redirect to a payment page after creating the order
            return redirect('advance_payment_page')  
        else:
            return JsonResponse({'success': False, 'message': 'adv_amount_id is required'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def full_payment_page(request):
    data=FullPay.objects.all()
    return render(request, 'full_payment_page.html', {"data":data})

def full_payment(request):
    if request.method == 'POST':
        full_amount_id = request.POST.get('full_amount_id')

        if full_amount_id:
            try:
                advance_bill = FullPay.objects.get(id=full_amount_id)
            except FullPay.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Invalid advance bill ID'})

            client = razorpay.Client(auth=('rzp_test_IzIBFTmzd3zzKk', 'mMvIdZd7a4EU1pMd9tSQEbE0'))
            amount_in_paise = int(advance_bill.Amount * 100)
            payment = client.order.create({'amount': amount_in_paise, 'currency': 'INR', 'payment_capture': '1'})

            # Assuming you want to redirect to a payment page after creating the order
            return redirect('full_payment_page')  
        else:
            return JsonResponse({'success': False, 'message': 'adv_amount_id is required'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

