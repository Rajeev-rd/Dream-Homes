from django.shortcuts import render, redirect
from Adminmodule.models import Category,Property
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

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
    return redirect(AddCategory)





def showproperty(request):
    data=Property.objects.all()
    return render(request, "showproperty.html",{"data":data})

def updateProperty(request,dataid):
    data=Property.objects.filter(id=dataid)
    datas=Category.objects.all()
    return render(request, "updateproperty.html",{"data":data,"datas":datas})




def updatepropertyfun(request, item):
    if request.method=="POST":
        CategoryName = request.POST.get("CategoryName")
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

        Property.objects.filter(id=item).update(CategoryName=CategoryName,description=description,price=price,sqft=sqft,floor=floor,image=file)
    return redirect(showproperty)




def deleteproperty(request, dataid):
    data=Property.objects.filter(id=dataid)
    data.delete()
    return redirect(showproperty)

def Addinteriorcategory(request):
    return render(request, "Addinteriorcategory.html")


def Addinteriourfun(request):

    if request.method == "POST":
        CategoryName = request.POST.get("CategoryName")
        description = request.POST.get("description")


        IM = request.FILES["image"]
        obj = Category(name=CategoryName, description=description,image=IM)
        obj.save()
    return redirect(AddCategory)

def Addinterior(request):
    return render(request, "Addinterior.html")