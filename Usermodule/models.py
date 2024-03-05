from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class RegistrationDb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if RegistrationDb.objects.filter(email=self.email).exists():
            raise ValidationError("Email already exists.")

        # If not, proceed with saving
        super().save(*args, **kwargs)



class contactbd(models.Model):
    name = models.CharField(max_length=100)