from django.db import models

# Create your models here.

class student ( models.Model):

    name = models.CharField(max_length=30)
    cource = models.CharField(max_length=30)
    regno = models.CharField(max_length=30)
    mid = models.CharField(max_length=30)
