from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import ClientForm
from .forms import AppointmentForm

# Create your views here.
def home(request):
    return render(request,'home.html')

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
