from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'gender',
            'age',
            'telephone',
            'email',
        ]
        labels = {
            'name'      = 'Name',
            'gender'    = 'Gender',
            'age'       = 'Age',
            'telephone' = 'Telephone',
            'email'     = 'Email'
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'client',
            'service',
            'employee',
            'date',
            'time',
        ]
        labels = {
            'client'   = 'Client',
            'service'  = 'Service',
            'employee' = 'Employee',
            'date'     = 'Date',
            'time'     = 'Time',
        }