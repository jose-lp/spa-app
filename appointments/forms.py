from django import forms
from .models import User
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

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
    class Meta:
        model = User
        fields = [
            'type_user',
            'first_name',
            'last_name',
            'gender',
            'age',
            'telephone',
            'email',
            'password',
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'user_id',
            'estetician',
            'service',
            'date',
            'time',
        ]