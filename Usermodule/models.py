from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class contactbd(models.Model):
    name = models.CharField(max_length=100)