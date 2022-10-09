from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class patient(models.Model):
    name = models.CharField(max_length=100)
    wardno = models.CharField(max_length=10)
    details = models.TextField()
    saline = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)

    def __str__(self):
        return self.name

   