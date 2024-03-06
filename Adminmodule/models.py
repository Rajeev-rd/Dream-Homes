from django.db import models

class Category(models.Model):
<<<<<<< HEAD
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
=======
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
    category = models.ForeignKey(InteriorCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='interior_images/', null=True, blank=True)

    def __str__(self):
        return self.name
>>>>>>> 06b450213a5a4dae9f418256f73b0b519b776c3c
