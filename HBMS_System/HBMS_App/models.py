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

#add rooms,
class rooms1(models.Model):
    room_num = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    beds = models.CharField(max_length=20)
    ac = models.CharField(max_length=20)
    flr = models.CharField(max_length=20)
    price = models.CharField(max_length=30)
    service = models.CharField(max_length=20)

#check-in-check-out,
class checkin_checkout(models.Model):
    name = models.CharField(max_length=30)
    dob = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    profe = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    id_prof = models.CharField(max_length=20)
    id_number = models.CharField(max_length=25)
    adult = models.CharField(max_length=10)
    children = models.CharField(max_length=10)
    arrival = models.CharField(max_length=20)
    depurt = models.CharField(max_length=20)
    room_id = models.CharField(max_length=20, default='')
    room_num = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    beds = models.CharField(max_length=20)
    ac = models.CharField(max_length=20)
    flr = models.CharField(max_length=20)
    price = models.CharField(max_length=30)
    service = models.CharField(max_length=20)
    tcost = models.CharField(max_length=20)
    pmod = models.CharField(max_length=20)
    dmod = models.CharField(max_length=20)
    checkby = models.CharField(max_length=20)
    


