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
    ( 'Massage'                , 'Massage' ),
    ( 'Manicure'               , 'Manicure' ),
    ( 'Pedicure'               , 'Pedicure' ),
    ( 'Facial Cleansing'       , 'Facial Cleansing' ),
    ( 'Permanent Hair Removal' , 'Permanent Hair Removal' ),
    ( 'Cryotherapy'            , 'Cryotherapy' )
]

TIME = [
    ( '8:00 AM' , '8:00 AM' ),
    ( '9:00 AM' , '9:00 AM' ),
    ( '10:00 AM', '10:00 AM'),
    ( '11:00 AM', '11:00 AM'),
    ( '1:00 PM' , '1:00 PM'),
    ( '2:00 PM' , '2:00 PM'),
    ( '3:00 PM' , '3:00 PM'),
    ( '4:00 PM' , '4:00 PM'),
]

ESTETICIANS = [
    ( 'José López', 'José López'),
    ( 'Mariela Hernández', 'Mariela Hernández')
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