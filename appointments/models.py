from django.db import models

# Create your models here.

GENDERS =[
    ( 'Male'   , 'M'),
    ( 'Female' , 'F'),
    ( 'Other'  , 'O')
]

SERVICES =[
    ( 'Massage'                , '0' ),
    ( 'Manicure'               , '1' ),
    ( 'Pedicure'               , '2' ),
    ( 'Facial Cleansing'       , '3' ),
    ( 'Permanent Hair Removal' , '4' ),
    ( 'Cryotherapy'            , '5' )
]

TIME = [
    ( '8:00 AM' , '8:00' ),
    ( '9:00 AM' , '9:00' ),
    ( '10:00 AM', '10:00'),
    ( '11:00 AM', '11:00'),
    ( '1:00 PM' , '13:00'),
    ( '2:00 PM' , '14:00'),
    ( '3:00 PM' , '15:00'),
    ( '4:00 PM' , '16:00'),
]

class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    telephone = models.PositiveIntegerField(blank=True)
    email = models.EmailField(max_length=254)
    password =  models.CharField(max_length=10)
    re_password =  models.CharField(max_length=10)

class Appointment(models.Model):
    client  = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.CharField(max_length=25, choices=SERVICES)
    date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME)