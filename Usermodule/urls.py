from django.urls import path
from Usermodule import views

urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('logins',views.logins,name="logins"),
    path('indexfront',views.indexfront,name="indexfront"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('projects',views.projects,name="projects"),
    path('contact',views.contact,name="contact"),
    path('loginusers',views.loginusers,name="loginusers"),
    path('myview',views.myview,name="myview"),
]