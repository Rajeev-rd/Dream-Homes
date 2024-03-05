from django.db import models

# Create your models here.



class Category(models.Model):
    Area = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    image = models.ImageField(null=True)
