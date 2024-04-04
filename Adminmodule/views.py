from datetime import timezone
from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from Adminmodule.models import Category,Property,InteriorCategory,Interior,Status,Contact,Renovation,Balance
from django.core.files.storage import FileSystemStorage
from Usermodule.models import AppointmentRequest
from Usermodule.views import SignInView
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login,logout
from Adminmodule.models import Message
from django.contrib.auth.models import User
from itertools import chain
from operator import attrgetter



# Create your views here.

def index(request):
    return render(request, "Adminindex.html")
def AddCategory(request):
    return render(request, "AddCategory.html")


def AddCategoryfun(request):

    if request.method == "POST":
        CategoryName = request.POST.get("CategoryName")
        description = request.POST.get("description")


        IM = request.FILES["image"]
        obj = Category(name=CategoryName, description=description,image=IM)
        obj.save()
    return redirect(AddCategory)

def showCategory(request):
    data=Category.objects.all()
    return render(request, "showCategory.html",{"data":data})


def updateCategory(request,dataid):
    data=Category.objects.filter(id=dataid)
    return render(request, "updateCategory.html",{"data":data})



def updateCategoryfun(request, item):
    if request.method=="POST":
        CategoryName = request.POST.get("CategoryName")
        description = request.POST.get("description")

        try:
            IM=request.FILES['image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=Category.objects.get(id=item).image

        Category.objects.filter(id=item).update(name=CategoryName,description=description,image=file)
    return redirect(showCategory)



def deletecategory(request, dataid):
    data=Category.objects.filter(id=dataid)
    data.delete()
    return redirect(showCategory)

def Addproperty(request):
    data=Category.objects.all()
    return render(request, "Addproperty.html",{"data":data})


def Addpropertyfun(request):

    if request.method == "POST":
        CategoryName = request.POST.get("CategoryName")
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        sqft = request.POST.get("sqft")
        floor = request.POST.get("floor")


        IM = request.FILES["image"]
        plan_image_file = request.FILES["plan_image"]
        category_instance = Category.objects.get(name=CategoryName)

        obj = Property(category=category_instance, name=name, price=price, description=description, floor=floor, sqft=sqft, image=IM,plan_image=plan_image_file)
        obj.save()
    return redirect(showproperty)





def showproperty(request):
    data=Property.objects.all()
    return render(request, "showproperty.html",{"data":data})

def updateProperty(request,dataid):
    data=Property.objects.filter(id=dataid)
    datas=Category.objects.all()
    return render(request, "updateproperty.html",{"data":data,"datas":datas})




def updatepropertyfun(request, item):
    if request.method=="POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        sqft = request.POST.get("sqft")
        floor = request.POST.get("floor")
        

        try:
            IM=request.FILES['image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=Property.objects.get(id=item).image

        Property.objects.filter(id=item).update(name=name,description=description,price=price,sqft=sqft,floor=floor,image=file)
    return redirect(showproperty)




def deleteproperty(request, dataid):
    data=Property.objects.filter(id=dataid)
    data.delete()
    return redirect(showproperty)

# def Addinteriorcategory(request):
#     return render(request, "Addinteriorcategory.html")


# def Addinteriourfun(request):

#     if request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")


#         IM = request.FILES["image"]
#         obj = InteriorCategory(name=name, description=description,image=IM)
#         obj.save()
#     return redirect(AddCategory)

def Addinterior(request):
    data=Category.objects.all()
    return render(request, "Addinterior.html",{"data":data})


# def showinteriorcategory(request):
#     data=InteriorCategory.objects.all()
#     return render(request, "showinteriorcategory.html",{"data":data})

def Addinteriourfun2(request):

    if request.method == "POST":
        category= request.POST.get("category")
        description = request.POST.get("description")
        price = request.POST.get("price")


        IM = request.FILES["image"]
        obj = Interior(category=category,description=description,price=price,image=IM)
        obj.save()
    return redirect(Addinterior)



def showinterior(request):
    data=Interior.objects.all()
    return render(request, "showinterior.html",{"data":data})






def updateinterior(request,dataid):
    data=Interior.objects.filter(id=dataid)
    datas=Interior.objects.all()
    return render(request, "updateinterior.html",{"data":data,"datas":datas})


def updateinteriorfun(request, item):
    if request.method=="POST":
        price = request.POST.get("price")
        description = request.POST.get("description")
        

        try:
            IM=request.FILES['image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=Interior.objects.get(id=item).image

        Interior.objects.filter(id=item).update(description=description,price=price,image=file)
    return redirect(showinterior)


def deleteinterior(request, dataid):
    data=Interior.objects.filter(id=dataid)
    data.delete()
    return redirect(showinterior)


def showmembers(request):
    data=User.objects.all()
    return render(request, "showmembers.html",{"data":data})



def AddStatus(request):
    data=User.objects.all()
    return render(request, "AddStatus.html",{"data":data})


def AddStatusFun(request):

    if request.method == "POST":
        CustomerName = request.POST.get("CustomerName")
        details = request.POST.get("details")
        IM = request.FILES["image"]
        obj = Status(CustomerName=CustomerName,details=details,image=IM)
        obj.save()
        messages.success(request, "Add Status Successfully")
    return redirect(AddStatus)

def Message(request):
    return render(request, "messagestable.html")



def message(request):

    if request.method == "POST":
        username= request.POST.get("username")
        email = request.POST.get("email")
        location = request.POST.get("location")
        message = request.POST.get("message")


        
        obj = Contact(username=username,email=email,location=location,message=message)
        obj.save()
    return redirect(Addinterior)


def balance(request):  
    return render(request, "balance.html")
def balanceadd(request):

    if request.method == "POST":
        name= request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")


        IM = request.FILES["image"]
        obj = Balance(name=name,description=description,price=price,image=IM)
        obj.save()
    return redirect(balance)



def showBalance(request):
    data=Balance.objects.all()
    return render(request, "showBalance.html",{"data":data})


def updateBalance(request,dataid):
    data=Balance.objects.filter(id=dataid)
    return render(request, "updateBalance.html",{"data":data})

def updateBalancefun(request, item):
    if request.method=="POST":
        name= request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        

        try:
            IM=request.FILES['image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=Balance.objects.get(id=item).image

        Balance.objects.filter(id=item).update(name=name,description=description,price=price,image=file)
    return redirect(showBalance)

def deleteBalance(request, dataid):
    data=Balance.objects.filter(id=dataid)
    data.delete()
    return redirect(showBalance)




def Renovations(request):  
    data=Category.objects.all()
    return render(request, "Renovations.html",{"data":data})
def addRenovation(request):

    if request.method == "POST":
        CategoryName = request.POST.get("CategoryName")
        description = request.POST.get("description")
        price = request.POST.get("price")


        IM = request.FILES["image"]
        obj = Renovation(category=CategoryName,description=description,price=price,image=IM)
        obj.save()
    return redirect(Renovations)



def showRenovation(request):
    data=Renovation.objects.all()
    return render(request, "showRenovation.html",{"data":data})


def updateRenovation(request,dataid):
    datas=Category.objects.all()
    data=Renovation.objects.filter(id=dataid)
    return render(request, "updateRenovation.html",{"data":data,"datas":datas})

def updateRenovationfun(request, item):
    if request.method=="POST":
        description = request.POST.get("description")
        price = request.POST.get("price")
        

        try:
            IM=request.FILES['image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=Renovation.objects.get(id=item).image

        Renovation.objects.filter(id=item).update(description=description,price=price,image=file)
    return redirect(showRenovation)

def deleteRenovation(request, dataid):
    data=Renovation.objects.filter(id=dataid)
    data.delete()
    return redirect(showRenovation)

def MessageTable(request):
    data = AppointmentRequest.objects.all()  
    return render(request, "messagestable.html",{"data":data})




from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import AdvancePay, FullPay, Message


from django.shortcuts import redirect, HttpResponse
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import redirect


from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.utils import timezone



def add_message(request):
    alert = False

    if request.method == "POST":
        receiver = request.POST.get("receiver")
        sender = request.POST.get("sender")
        msg = request.POST.get("msg")

        # Use get method with a default value for 'image' to avoid MultiValueDictKeyError
        image = request.FILES.get("image", None)

        obj = Message(receiver=receiver, sender=sender, msg=msg, image=image)
        obj.save()
        if sender == "admin":
            
            return redirect('showmessage',dataid=receiver)
        else:
            
            return redirect('message_user', dataid=receiver)

    return render(request, 'web.html', {'alert': alert})


from django.shortcuts import render
from django.db.models import Q
from operator import attrgetter
from itertools import chain
from .models import Message

def showmessage(request, dataid):
    current_user = request.user
    msg = AppointmentRequest.objects.filter(name=dataid)

    data = Message.objects.filter(Q(sender=dataid) | Q(receiver=dataid))

    all_msgs = sorted(
        data,
        key=attrgetter('timestamp'),
        reverse=True
    )

    return render(request, 'showmessage.html', {"data": data, "all_msgs": all_msgs, "msg": msg})

from django.shortcuts import render, redirect
from .models import AdvancePay, FullPay, Category, User
from django.contrib import messages

def Advance(request):
    data = Category.objects.all()  
    datas = User.objects.all() 
    return render(request, "Advance.html",{"data":data,"datas":datas})

def AdvancePays(request):
    if request.method == "POST":
        name= request.POST.get("name")
        category = request.POST.get("category")
        advance_amount = request.POST.get("advance_amount")
        obj = AdvancePay(name=name, Category=category, AdvanceAmount=advance_amount)
        obj.save()
    return redirect('balance')  # Assuming you have a URL named 'balance' defined in your URLs

def FullPays(request):
    datas = User.objects.all()
    data = Category.objects.all()  
    return render(request, "FullPay.html",{"data":data,"datas":datas})

def FullAmound(request):
    if request.method == "POST":
        username= request.POST.get("username")
        category = request.POST.get("category")
        labour_cost = request.POST.get("labour_cost")
        material_cost = request.POST.get("material_cost")
        total_amount = request.POST.get("total_amount")
        obj = FullPay(username=username, Category=category, Labourcost=labour_cost, Materialcost=material_cost, Amount=total_amount)
        obj.save()
        messages.success(request, "Successfully")
    return redirect('full_pays')  # Assuming you have a URL named 'full_pays' defined in your URLs




def signout_admin(request,*args, **kwargs):
    logout(request)
    return redirect("indexfront")