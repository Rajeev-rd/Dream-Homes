from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100,null=True)
    sqft = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    plan_image = models.ImageField(upload_to='plan_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class InteriorCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='interior_category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Interior(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='interior_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Renovation(models.Model):
    category = models.CharField(max_length=100,default='',null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='renovation_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    details = models.TextField()
    image = models.ImageField(upload_to='status_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    username = models.TextField( null=True)
    email = models.EmailField( null=True)
    message = models.TextField( null=True)
    location = models.TextField( null=True)

    def __str__(self):
        return self.username
    

class Balance(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Balance_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance_item = models.ForeignKey(Balance, on_delete=models.CASCADE)
    razorpay_payment_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender=models.TextField(max_length=100,null=True)
    receiver = models.TextField(max_length=100,null=True)
    msg=models.CharField(max_length=100)
    image = models.ImageField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class AdvancePay(models.Model):
    name = models.CharField( max_length=100)
    Category = models.CharField( null=True,max_length=100)
    AdvanceAmount = models.DecimalField(null=True, max_digits=10, decimal_places=2)  # Example for DecimalField
    
    
class FullPay(models.Model):
    name = models.CharField( null=True,max_length=100)
    Category = models.CharField( null=True,max_length=100)
    Labourcost=models.CharField( null=True,max_length=100)
    Materialcost=models.CharField( null=True,max_length=100)
    Amount = models.DecimalField(null=True, max_digits=10, decimal_places=2)  # Example for DecimalField

    def __str__(self):
        return self.name