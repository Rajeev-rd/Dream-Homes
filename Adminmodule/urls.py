from django.urls import path
from Adminmodule import views


urlpatterns = [
    path('index/',views.index,name="index"),
    path('AddCategory/',views.AddCategory,name="AddCategory"),
    path('AddCategoryfun/', views.AddCategoryfun, name="AddCategoryfun"),

    ]