from django.db.models.fields import EmailField
from django.shortcuts import render, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm, LoginForm
from .forms import AppointmentForm
from .models import User
from .models import Appointment
import django_tables2 as tables


class AppointmentsTable(tables.Table):

    class Meta:
        model = Appointment
        template_name = "django_tables2/bootstrap.html"

# Create your views here.
def home(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.data)
        if form.is_valid():
            print("formulario válido")
            f_email = str(form.cleaned_data['email'])
            f_passw = str(form.cleaned_data['password'])
            user    = User.objects.raw('SELECT * FROM appointments_user WHERE email = %s', [f_email])
            if user[0] is not None:
                print("email existe")
                if user[0].password == f_passw:
                    print("passw correcto")
                    request.session['user'] = user[0].id
                    print(user[0].id)
                    form = AppointmentForm()
                    return render(request, 'appointments.html', {'form': form})
                else:
                    print("passw incorrecto")
            else:
                print("email no existe")
        else:
            print("formulario INVALIDO")
        return render(request, 'home.html', {'form': form})
    else:
        return render(request,'home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("form valido")
            form.save()
            return render(request, 'home.html', {'form': form})
        else:
            print("form no valido")
            return render(request,'register.html', {'form': form})
    else:
        form = UserForm()
        return render(request,'register.html', {'form': form})

def edit_user(request):
    return render(request, 'edit_user.html')

def appointments(request):
    appointments_user = Appointment.objects.all().filter(user_id=request.session['user'])

    appointments_list = []
    for p in appointments_user:
        appointments_list.append({'estetician': p.estetician,'service': p.service, 'date': p.date, 'time': p.time})

    print(appointments_list)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print("form valido")
            form.save()
        else:
            return render(request,'appointments.html', {'form': form ,'appointments_usr': appointments_list})
            
        return render(request, 'appointments.html', {'form': form ,'appointments_usr': appointments_list})
    else:
        form = AppointmentForm()
        return render(request,'appointments.html', {'form': form ,'appointments_usr': appointments_list})

def edit_appointment(request):
    return render(
        request,
        'edit_appointment.html'
    )

