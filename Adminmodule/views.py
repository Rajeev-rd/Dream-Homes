from django.shortcuts import render, redirect
from Adminmodule.models import Category,Property,InteriorCategory,Interior,Status,Contact,Renovation,Balance
from django.core.files.storage import FileSystemStorage
from Usermodule.models import AppointmentRequest
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User



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
        category_instance = Category.objects.get(name=CategoryName)

        obj = Property(category=category_instance, name=name, price=price, description=description, floor=floor, sqft=sqft, image=IM)
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


# def updateinteriorcategory(request,dataid):
#     data=InteriorCategory.objects.filter(id=dataid)
#     return render(request, "updateinteriorcategory.html",{"data":data})

# def updateinteriorfun1(request, item):
#     if request.method=="POST":
#         name= request.POST.get("name")
#         description = request.POST.get("description")
        

#         try:
#             IM=request.FILES['image']
#             FS=FileSystemStorage()
#             file=FS.save(IM.name,IM)

#         except MultiValueDictKeyError:
#             file=InteriorCategory.objects.get(id=item).image

#         InteriorCategory.objects.filter(id=item).update(name=name,description=description,image=file)
#     return redirect(showinteriorcategory)

# def deleteinteriorcategory(request, dataid):
#     data=InteriorCategory.objects.filter(id=dataid)
#     data.delete()
#     return redirect(showinteriorcategory)




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
    return render(request, "AddStatus.html")




def AddStatusFun(request):

    if request.method == "POST":
        details = request.POST.get("details")

        IM = request.FILES["image"]
        obj = Status(details=details,image=IM)
        obj.save()
    return redirect(Addinterior)



def MessageTable(request):
    data = AppointmentRequest.objects.all()  
    return render(request, "messagestable.html",{"data":data})


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


def showmessage(request):  
    return render(request, "showmessage.html")


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
        name= request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")


        IM = request.FILES["image"]
        obj = Renovation(name=name,description=description,price=price,image=IM)
        obj.save()
    return redirect(balance)



def showRenovation(request):
    data=Renovation.objects.all()
    return render(request, "showRenovation.html",{"data":data})


def updateRenovation(request,dataid):
    datas=Category.objects.all()
    data=Renovation.objects.filter(id=dataid)
    return render(request, "updateRenovation.html",{"data":data,"datas":datas})

def updateRenovationfun(request, item):
    if request.method=="POST":
        name= request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        

        try:
            IM=request.FILES['image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=Renovation.objects.get(id=item).image

        Renovation.objects.filter(id=item).update(name=name,description=description,price=price,image=file)
    return redirect(showRenovation)

def deleteRenovation(request, dataid):
    data=Renovation.objects.filter(id=dataid)
    data.delete()
    return redirect(showRenovation)