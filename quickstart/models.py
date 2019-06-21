from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    talkid = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    borndate = models.DateField()
    password = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

