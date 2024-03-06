from django.urls import path
from Usermodule import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='indexfront', permanent=False)),
    path('indexfront',views.indexfront,name="indexfront"),
    path('signup',views.signup,name="signup"),
    path('logins',views.logins,name="logins"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('projects',views.projects,name="projects"),
    path('contact',views.contact,name="contact"),
    path('loginusers',views.loginusers,name="loginusers"),
    path('myview',views.myview,name="myview"),
    path('logout', views.logout, name="logout"),



    path('check-authentication/', views.check_authentication, name="check_authentication"),

]