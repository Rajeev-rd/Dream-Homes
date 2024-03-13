from django.urls import path
from Adminmodule import views


urlpatterns = [
    path('index/',views.index,name="index"),
    path('AddCategory/',views.AddCategory,name="AddCategory"),
    path('AddCategoryfun/', views.AddCategoryfun, name="AddCategoryfun"),
    path('Addproperty/', views.Addproperty, name="Addproperty"),
    path('Addinteriorcategory/', views.Addinteriorcategory, name="Addinteriorcategory"),
    path('Addinterior/', views.Addinterior, name="Addinterior"),
    path('showCategory/', views.showCategory, name="showCategory"),
    path('updateCategory/<int:dataid>', views.updateCategory, name="updateCategory"),
    path('updateCategoryfun/<item>', views.updateCategoryfun, name="updateCategoryfun"),
    path('deletecategory/<dataid>', views.deletecategory, name="deletecategory"),
    path('Addpropertyfun/', views.Addpropertyfun, name="Addpropertyfun"),
    path('showproperty/', views.showproperty, name="showproperty"),
    path('updateProperty/<int:dataid>', views.updateProperty, name="updateProperty"),
    path('updatepropertyfun/<item>', views.updatepropertyfun, name="updatepropertyfun"),    
    path('deleteproperty/<dataid>', views.deleteproperty, name="deleteproperty"),
    path('Addinteriourfun', views.Addinteriourfun, name="Addinteriourfun"),
    path('Addinteriourfun2', views.Addinteriourfun2, name="Addinteriourfun2"),
    path('showinteriorcategory', views.showinteriorcategory, name="showinteriorcategory"),
    path('updateinteriorcategory/<dataid>', views.updateinteriorcategory, name="updateinteriorcategory"),
    path('updateinteriorcategoryfun/<item>', views.updateinteriorcategoryfun, name="updateinteriorcategoryfun"),  
    path('deleteinteriorcategory/<dataid>', views.deleteinteriorcategory, name="deleteinteriorcategory"),
    path('showinterior', views.showinterior, name="showinterior"),
    path('updateinterior/<dataid>', views.updateinterior, name="updateinterior"),
    path('updateinteriorfun/<item>', views.updateinteriorfun, name="updateinteriorfun"),
    path('deleteinterior/<dataid>', views.deleteinterior, name="deleteinterior"),
    path('showmembers', views.showmembers, name="showmembers"),
    path('AddStatus/', views.AddStatus, name="AddStatus"),
    path('AddStatusFun/', views.AddStatusFun, name="AddStatusFun"),


    ]