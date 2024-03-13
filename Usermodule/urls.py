from django.urls import path
from Usermodule import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='indexfront', permanent=False)),
    path('indexfront',views.indexfront,name="indexfront"),
    path('signup',views.RegistrationView.as_view(),name="signup"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('projects',views.projects,name="projects"),
    path('contact',views.contact,name="contact"),
    path('login',views.SignInView.as_view(),name="login"),
    path('logout',views.signout_view,name="logout")
    

]