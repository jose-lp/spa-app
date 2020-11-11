from django import forms
from .models import Client
from .models import Appointment
from .models import Login

from django.forms import PasswordInput

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'email',
            'password',
            ]

class ClientForm(forms.ModelForm):
    re_password = forms.CharField(max_length=128, widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'gender',
            'age',
            'telephone',
            'email',
            'password',
            're_password',
        ]
        widgets = {
            'password': PasswordInput(),
            're_password': PasswordInput()
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'client_id',
            'service',
            'date',
            'time',
        ]