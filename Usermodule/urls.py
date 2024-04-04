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
    path('testimonial/',views.testimonial,name="testimonial"),
    path('status/',views.status,name="status"),
    # path('updatestatus/',views.updatestatus,name="updatestatus"),
    path('login/',views.SignInView.as_view(),name="login"),
    path('logout/',views.signout_view,name="logout"),

    path('submit/', views.submit_request, name='submit_request'),

    path('testimonial/',views.testimonial, name='testimonial'),
    path('add_testimonial/',views.add_testimonial, name='add_testimonial'),
    path('delete_testimonial/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
    path('checkout/<int:balance_item_id>/', views.checkout, name='checkout'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('message_user/<dataid>',views.message_user, name='message_user'),

    path('bltcntsingle/<int:property_id>/', views.bltcntsingle, name='bltcntsingle'),
    path('initiate_payment/<int:property_id>/', views.initiate_payment, name='initiate_payment'),
    path('download_plan/<int:property_id>/', views.download_plan, name='download_plan'),
    path('bltcntafterpayment/<int:property_id>/', views.bltcntafterpayment, name='bltcntafterpayment'),

    path('Interiorsingle/<int:Interior_id>/', views.Interiorsingle, name='Interiorsingle'),
    path('Renovationsingle/<int:Reno_id>/', views.Renovationsingle, name='Renovationsingle'),

    path('advance_payments/', views.advance_payment_page, name='advance_payment_page'),
    path('full_payments/', views.full_payment_page, name='full_payment_page'),

]