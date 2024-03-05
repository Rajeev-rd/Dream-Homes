from django.shortcuts import render, redirect
from Adminmodule.models import Category

# Create your views here.

def index(request):
    return render(request, "Adminindex.html")
def AddCategory(request):
    return render(request, "AddCategory.html")


def AddCategoryfun(request):

    if request.method == "POST":
        Floor = request.POST.get("Floor")
        sqrt = request.POST.get("sqrt")


        IM = request.FILES["image"]
        obj = Category(Floor=Floor, Dsqrt=sqrt,image=IM)
        obj.save()
    return redirect(AddCategoryfun)