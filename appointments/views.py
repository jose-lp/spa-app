from django.db.models.fields import EmailField
from django.shortcuts import render, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm, LoginForm
from .forms import AppointmentForm
from .models import User
from .models import Appointment
import django_tables2 as tables


TIME = [
    ('8:00 AM', 'José López'),
    ('8:00 AM', 'Mariela Hernández'), 
    ('9:00 AM' , 'José López'),
    ('9:00 AM' , 'Mariela Hernández'),
    ('10:00 AM' , 'José López'),
    ('10:00 AM' , 'Mariela Hernández'),
    ('11:00 AM' , 'José López'),
    ('11:00 AM' , 'Mariela Hernández'),
    ('1:00 PM' , 'José López'),
    ('1:00 PM' , 'Mariela Hernández'),
    ('2:00 PM' , 'José López'),
    ('2:00 PM' , 'Mariela Hernández'),
    ('3:00 PM' , 'José López'),
    ('3:00 PM' , 'Mariela Hernández'),
    ('4:00 PM' , 'José López'),
    ('4:00 PM' , 'Mariela Hernández') ]

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

    appointments_usr  = get_appointments(request)
    appointments_list = []

    if request.method=='POST' and 'check_btn' in request.POST:
        form = AppointmentForm()
        try:
            print("check")
            request.session['date'] = request.POST['date']
            appointments_by_date = get_appointments_by_date(request)

            temp_TIME = TIME

            for i in appointments_by_date:
                if i in temp_TIME:
                    temp_TIME.remove(i)
            print(temp_TIME)

            appointments_list = []
            for i in temp_TIME:
                appointments_list.append(f'{i[0]} with {i[1]}') 
            print(appointments_list)
        
            return render(request, 'appointments.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr})
        except:

            return render(request, 'appointments.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr})

    elif request.method == 'POST' and 'reserve_btn' in request.POST:
        form = AppointmentForm()
        try:
            info = request.POST['appointments'].split(sep=' with ')
            print(request.POST)
        
            updated_request  = request.POST.copy()
            updated_request.update({
                'user_id': request.session['user'],
                'date': request.session['date'],
                'time': info[0],
                'estetician': info[1],
                'service': request.POST['service']
            })
            form = AppointmentForm(updated_request)
          
            if form.is_valid():
                print("form valido")
                form.save()
                appointments_list = get_appointments(request)
                print("adentro")
                print(appointments_list)
                del request.session['date']
            else:
                print("no valido")
                form = AppointmentForm()
                return render(request,'appointments.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr})

            return render(request, 'appointments.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr})
        except:
            
            return render(request, 'appointments.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr})

    
    elif request.method=='POST' and 'delete_btn' in request.POST:
        print("press delete")
        # Se lee el id de la cita del request
        appointment_id = request.POST['id']
        print(appointment_id)

        # Se elimina la cita utilizando el id
        Appointment.objects.filter(id=appointment_id).delete()

        # Se actualiza la tabla de citas
        appointments_list = get_appointments(request)
        
        form = AppointmentForm()
        return render(request, 'appointments.html', {'form': form ,'appointments_usr': appointments_usr})

    
    elif request.method=='POST' and 'edit_btn' in request.POST:
        print("press edit")
        form = AppointmentForm()
        return render(request, 'edit_appointment.html', {'form': form ,'appointments_usr': appointments_usr})
    
    else:
        appointments_list = get_appointments(request)
        form = AppointmentForm()
        return render(request, 'appointments.html', {'form': form ,'appointments_usr': appointments_usr})
    

def edit_appointment(request):
    return render(
        request,
        'edit_appointment.html'
    )

def get_appointments(request):
    
    appointments_user = Appointment.objects.all().filter(user_id=request.session['user'])

    appointments_list = []
    for p in appointments_user:
        appointments_list.append({'id': p.id,'estetician': p.estetician,'service': p.service, 'date': p.date, 'time': p.time})

    return appointments_list

def get_appointments_by_date(request):
    date_select = request.POST['date']
    appointments_by_date = Appointment.objects.filter(date=date_select)
    temp_list = []
    for p in appointments_by_date:
       temp_list.append((p.time, p.estetician))
    return temp_list
