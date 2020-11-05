from django import forms
from .models import Client
from .models import Appointment

class LoginForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'email',
            'password'
        ]
        labels = {
            'email' = 'Email',
            'password' = 'Password'
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'gender',
            'age',
            'telephone',
            'email',
            'passw',
        ]
        labels = {
            'name'      = 'Name',
            'gender'    = 'Gender',
            'age'       = 'Age',
            'telephone' = 'Telephone',
            'email'     = 'Email'
            'password'  = 'Password',
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'client',
            'service',
            'date',
            'time',
        ]
        labels = {
            'client'   = 'Client',
            'service'  = 'Service',
            'date'     = 'Date',
            'time'     = 'Time',
        }