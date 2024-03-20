from django.db import models

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
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='interior_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    details = models.TextField()
    image = models.ImageField(upload_to='interior_images/', null=True, blank=True)

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
    image = models.ImageField(upload_to='interior_images/', null=True, blank=True)

    def __str__(self):
        return self.name