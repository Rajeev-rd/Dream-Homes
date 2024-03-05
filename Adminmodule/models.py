from django.db import models

# Create your models here.



class Category(models.Model):
    CategoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True)


class propertydb(models.Model):
    CategoryName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sqft = models.CharField(max_length=100)
    floor = models.IntegerField()
    image = models.ImageField(null=True)


class interiorCategory(models.Model):
    RoomName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True)


class interiordb(models.Model):
    RoomName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(null=True)
