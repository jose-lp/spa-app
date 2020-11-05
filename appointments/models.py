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
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    telephone = models.PositiveIntegerField(blank=True)
    email = models.EmailField(max_length=254)
    password =  models.CharField(max_length=10)

class Appointment(models.Model):
    client  = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.CharField(max_length=1, choices=SERVICES)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)