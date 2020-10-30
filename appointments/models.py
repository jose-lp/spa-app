from django.db import models

# Create your models here.

GENDERS =[
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

SERVICES =[
    ('0', 'Massage'),
    ('1', 'Manicure'),
    ('2', 'Pedicure'),
    ('3', 'Facial Cleansing'),
    ('4', 'Permanent Hair Removal'),
    ('5', 'Cryotherapy')
]

class Client(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    telephone = models.PositiveIntegerField(blank=True, max_length=8, min_length=8)
    email = models.EmailField(max_length=254)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    telephone = models.PositiveIntegerField(blank=True, max_length=8, min_length=8)
    email = models.EmailField(max_length=254)

class Appointment(models.Model):
    client  = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.CharField(max_length=1, choices=SERVICES)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)