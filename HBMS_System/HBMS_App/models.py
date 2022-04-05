import email
from operator import mod
from turtle import mode
from django.db import models
from matplotlib.pyplot import cla

# Create your models here.
#admin database model
class admin1(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

#employee table
class employee1(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=100)