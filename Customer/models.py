from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=255)
  phone = models.CharField(max_length=15)
  address = models.TextField()