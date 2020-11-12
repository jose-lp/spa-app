from django.db import models

# Create your models here.

GENDERS =[
    ( 'Male'   , 'M'),
    ( 'Female' , 'F'),
    ( 'Other'  , 'O')
]

TYPE_USER =[
    ( 'Admin'  , 'A'),
    ( 'Normal' , 'N')
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

ESTETICIANS = [
    ( 'José López', 'JL'),
    ( 'Mariela Hernández', 'MH')
]

class User(models.Model):
    id = models.AutoField(primary_key=True)
    type_user =  models.CharField(max_length=7, choices=TYPE_USER)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    telephone = models.PositiveIntegerField(blank=True)
    email = models.EmailField(max_length=254, unique=True)
    password =  models.CharField(max_length=10)

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estetician = models.CharField(max_length=25, choices=ESTETICIANS)
    service = models.CharField(max_length=25, choices=SERVICES)
    date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME)

class Login(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=10)