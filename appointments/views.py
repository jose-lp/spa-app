from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import ClientForm, LoginForm
from .forms import AppointmentForm
from .models import Client

# Create your views here.
def home(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("validar")
            f_email = str(form.cleaned_data['email'])
            f_passw = str(form.cleaned_data['password'])
            user    = Client.objects.raw('SELECT * FROM appointments_client WHERE email = %s', [f_email])
            if user[0] is not None:
                if user[0].password == f_passw:
                    print("iguales")
                    request.session['user'] = user[0].email
                    print(user)
                    form = AppointmentForm()
                    return render(request, 'appointments.html', {'form': form})

        return render(request, 'home.html', {'form': form})
    else:
        return render(request,'home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'register.html', {'form': form})
            
        return render(request, 'home.html', {'form': form})
    else:
        form = ClientForm()
        return render(request,'register.html', {'form': form})

def edit_client(request):
    return render(request, 'edit_client.html')

def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'appointments.html', {'form': form})
            
        return render(request, 'appointments.html', {'form': form})
    else:
        form = AppointmentForm()
        return render(request,'appointments.html', {'form': form})

def edit_appointment(request):
    return render(
        request,
        'edit_appointment.html'
    )