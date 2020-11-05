from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(
        request,
        'home.html'
    )

def register(request):
    return render(
        request,
        'register.html'
    )

def edit_client(request):
    return render(
        request,
        'edit_client.html'
    )

def appointments(request):
    return render(
        request,
        'appointments.html'
    )

def edit_appointment(request):
    return render(
        request,
        'edit_appointment.html'
    )
