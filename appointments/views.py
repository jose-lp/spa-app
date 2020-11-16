from django.db.models.fields import EmailField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm, LoginForm
from .forms import AppointmentForm
from .models import User
from .models import Appointment

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


# Create your views here.
def home(request):
    form = LoginForm()
    error = {}
    client_list = get_appointment_clients()
    appointments_list = []
    request.session.flush()
    if request.method == 'POST':
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                f_email = str(form.cleaned_data['email'])
                f_passw = str(form.cleaned_data['password'])
                user    = User.objects.raw('SELECT * FROM appointments_user WHERE email = %s', [f_email])
                if user[0] is not None:

                    if user[0].password == f_passw:
                        request.session['user'] = user[0].id
                        form = AppointmentForm()
                        if user[0].type_user == 'Admin':
                            appointments_usr  = get_appointments_admin(request)
                            return HttpResponseRedirect("../appointments_admin/")
                            
                        else:
                            appointments_usr  = get_appointments(request)
                            return HttpResponseRedirect("../appointments/")
                    else:
                        error['password'] = "Incorrect password"
                else:
                    error['email'] = "Email doesn't exist"
            else:
                error['password'] = "Some field is missing"
            return render(request, 'home.html', {'form': form, 'error': error})
        except:
            form = LoginForm()
            print("except")
            error['email'] = "Email doesn't exist"
            return render(request, 'home.html', {'form': form, 'error': error})
    else:
        return render(request,'home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'form': form})
        else:
            return render(request,'register.html', {'form': form})
    else:
        form = UserForm()
        return render(request,'register.html', {'form': form})

def appointments(request):

    appointments_usr  = get_appointments(request)
    appointments_list = []
    error = {}
    if request.method=='POST' and 'check_btn' in request.POST:
        form = AppointmentForm()
        try:
            request.session['date'] = request.POST['date']
            appointments_by_date = get_appointments_by_date_and_user(request)

            temp_TIME = TIME.copy()

            for i in appointments_by_date:
                if i in temp_TIME:
                    temp_TIME.remove(i)

            appointments_list = []
            for i in temp_TIME:
                appointments_list.append(f'{i[0]} with {i[1]}') 
        
            return render(request, 'appointments.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr})
        except:

            return render(request, 'appointments.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr})

    elif request.method == 'POST' and 'reserve_btn' in request.POST:
        form = AppointmentForm()
        try:
            info = request.POST['appointments'].split(sep=' with ')
        
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
                form.save()
                appointments_list = get_appointments(request)
                appointments_usr = get_appointments(request)
                del request.session['date']
                return render(request, 'appointments.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr})
            else:
                form = AppointmentForm()
                return render(request,'appointments.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr})
        except:
            error['date'] = "Please select a date"
            return render(request, 'appointments.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr, 'error':error})

    
    elif request.method=='POST' and 'delete_btn' in request.POST:
        # Se lee el id de la cita del request
        appointment_id = request.POST['appointment_id']

        # Se elimina la cita utilizando el id
        Appointment.objects.filter(id=appointment_id).delete()

        # Se actualiza la tabla de citas
        appointments_list = get_appointments(request)
        
        appointments_usr = get_appointments(request)

        form = AppointmentForm()
        return render(request, 'appointments.html', {'form': form ,'appointments_usr': appointments_usr})

    
    elif request.method=='POST' and 'edit_btn' in request.POST:
        form = AppointmentForm()
        request.session['appointment_id'] = request.POST['appointment_id']
        return HttpResponseRedirect("../edit_appointment/")
    
    else:
        appointments_list = get_appointments(request)
        form = AppointmentForm()
        return render(request, 'appointments.html', {'form': form ,'appointments_usr': appointments_usr})
    

def appointments_admin(request):
    client_list = get_appointment_clients()
    appointments_usr  = get_appointments_admin(request)
    appointments_list = []
    error = {}

    if request.method=='POST' and 'check_btn' in request.POST:
        form = AppointmentForm()
        try:
            request.session['date'] = request.POST['date']
            appointments_by_date = get_appointments_by_date(request)

            temp_TIME = TIME.copy()

            for i in appointments_by_date:
                if i in temp_TIME:
                    temp_TIME.remove(i)

            appointments_list = []
            for i in temp_TIME:
                appointments_list.append(f'{i[0]} with {i[1]}') 

            return render(request, 'appointments_admin.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr, 'client_list': client_list})
        except:

            return render(request, 'appointments_admin.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr, 'client_list': client_list})

    elif request.method == 'POST' and 'reserve_btn' in request.POST:
        form = AppointmentForm()
        try:
            info = request.POST['appointments'].split(sep=' with ')
            info_client = request.POST['user_sel'].split(sep=': ')
            id_client = int(info_client[0])
            
            updated_request  = request.POST.copy()
            updated_request.update({
                'user_id': id_client,
                'date': request.session['date'],
                'time': info[0],
                'estetician': info[1],
                'service': request.POST['service']
            })
            form = AppointmentForm(updated_request)
          
            if form.is_valid():
                form.save()
                appointments_usr = get_appointments_admin(request)
                del request.session['date']
                return render(request, 'appointments_admin.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr, 'client_list': client_list})
            else:
                form = AppointmentForm()
                return render(request,'appointments_admin.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr, 'client_list': client_list})
        except:
            error['date'] = "Please select a date"
            return render(request, 'appointments_admin.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr, 'client_list': client_list, 'error': error})

    
    elif request.method=='POST' and 'delete_btn' in request.POST:
        # Se lee el id de la cita del request
        appointment_id = request.POST['appointment_id']

        # Se elimina la cita utilizando el id
        Appointment.objects.filter(id=appointment_id).delete()

        # Se actualiza la tabla de citas
        appointments_list = get_appointments_admin(request)
        
        appointments_usr = get_appointments_admin(request)
        
        form = AppointmentForm()
        return render(request, 'appointments_admin.html', {'form': form ,'appointments_usr': appointments_usr, 'client_list': client_list})
    
    elif request.method=='POST' and 'edit_btn' in request.POST:
        form = AppointmentForm()
        request.session['appointment_id'] = request.POST['appointment_id']
        return HttpResponseRedirect("../edit_appointment_admin/")
    
    else:
        appointments_list = get_appointments_admin(request)
        form = AppointmentForm()
        return render(request, 'appointments_admin.html', {'form': form ,'appointments_usr': appointments_usr, 'client_list': client_list})

def edit_appointment(request):
    appointments_usr  = get_appointments(request)
    appointments_list = []
    form = AppointmentForm()
    error = {}
    if request.method=='POST' and 'check_btn' in request.POST:
        form = AppointmentForm()
        try:
            request.session['date'] = request.POST['date']
            appointments_by_date = get_edit_appointments_by_date_and_user(request)

            temp_TIME = TIME.copy()

            for i in appointments_by_date:
                if i in temp_TIME:
                    temp_TIME.remove(i)

            appointments_list = []
            for i in temp_TIME:
                appointments_list.append(f'{i[0]} with {i[1]}') 
            
            return render(request, 'edit_appointment.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr})
        except:

            return render(request, 'edit_appointment.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr})
    elif request.method == 'POST' and 'update_btn' in request.POST:
        form = AppointmentForm()
        try:
            info = request.POST['appointments'].split(sep=' with ')
            appointment = Appointment.objects.get(id=request.session['appointment_id'])
            appointment.date = request.session['date']
            appointment.time = info[0]
            appointment.estetician = info[1]
            appointment.service = request.POST['service']
            appointment.save()
            appointments_usr = get_appointments(request)
            return render(request, 'appointments.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr})
        except:
            error['date'] = "Please select a date"
            return render(request, 'edit_appointment.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr,'error':error})  
    return render(request, 'edit_appointment.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr})   

def edit_appointment_admin(request):
    appointments_usr  = get_appointments_admin(request)
    client_list = get_appointment_clients()
    appointments_list = []
    form = AppointmentForm()
    error = {}

    if request.method=='POST' and 'check_btn' in request.POST:
        form = AppointmentForm()
        try:
            request.session['date'] = request.POST['date']
            appointments_by_date = get_appointments_by_date(request)

            temp_TIME = TIME.copy()

            for i in appointments_by_date:
                if i in temp_TIME:
                    temp_TIME.remove(i)

            appointments_list = []
            for i in temp_TIME:
                appointments_list.append(f'{i[0]} with {i[1]}') 
        
            return render(request, 'edit_appointment_admin.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr, 'client_list': client_list})
        except:

            return render(request, 'edit_appointment_admin.html', {'form': form ,'appointment_list': appointments_list,  'appointments_usr': appointments_usr, 'client_list': client_list})
    elif request.method == 'POST' and 'update_btn' in request.POST:
        form = AppointmentForm()
        try:
            info = request.POST['appointments'].split(sep=' with ')
            info_client = request.POST['user_sel'].split(sep=': ')
            id_client = int(info_client[0])
            id_client = User.objects.get(id=id_client)

            appointment = Appointment.objects.get(id=request.session['appointment_id'])
            appointment.user_id = id_client
            appointment.date = request.session['date']
            appointment.time = info[0]
            appointment.estetician = info[1]
            appointment.service = request.POST['service']
            appointment.save()
            
            appointments_usr  = get_appointments_admin(request)
            return render(request, 'appointments_admin.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr, 'client_list': client_list})
        except:
            error['date'] = "Please select a date"
            return render(request, 'edit_appointment_admin.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr, 'client_list': client_list, 'error':error})    
    
    return render(request, 'edit_appointment_admin.html', {'form': form ,'appointments_list': appointments_list, 'appointments_usr': appointments_usr, 'client_list': client_list})   


def get_appointments(request):
    appointments_user = Appointment.objects.all().filter(user_id=request.session['user'])

    appointments_list = []
    for p in appointments_user:
        appointments_list.append({'id': p.id,'estetician': p.estetician,'service': p.service, 'date': p.date, 'time': p.time})

    return appointments_list

def get_appointments_admin(request):
    appointments = Appointment.objects.all()
    appointments_list = []
    for p in appointments:
        appointments_list.append({'id': p.id,'estetician': p.estetician,'service': p.service, 'date': p.date, 'time': p.time, 'name': f'{p.user_id.first_name} {p.user_id.last_name}' })

    return appointments_list

def get_appointments_by_date(request):
    date_select = request.POST['date']
    appointments_by_date = Appointment.objects.filter(date=date_select)
    temp_list = []
    for p in appointments_by_date:
       temp_list.append((p.time, p.estetician))
    return temp_list

def get_appointments_by_date_and_user(request):
    date_select = request.POST['date']
    appointments_by_date = Appointment.objects.filter(date=date_select)
    temp_list = []
    for p in appointments_by_date:
        if p.user_id.id == request.session["user"]:
            temp_list.append((p.time, "José López"))
            temp_list.append((p.time, "Mariela Hernández"))
        else:
            temp_list.append((p.time, p.estetician))
    return temp_list

def get_edit_appointments_by_date_and_user(request):
    date_select = request.POST['date']
    appointments_by_date = Appointment.objects.filter(date=date_select)
    temp_list = []
    for p in appointments_by_date:
        if p.id == int(request.session["appointment_id"]):
            pass
        
        elif p.user_id.id == request.session["user"] :
            temp_list.append((p.time, "José López"))
            temp_list.append((p.time, "Mariela Hernández"))
        else:
            temp_list.append((p.time, p.estetician))
    return temp_list

def get_appointment_clients():
    users = User.objects.all()
    client_list = []
    for p in users:
        client = f'{p.id}: {p.first_name} {p.last_name}'
        if client not in client_list:
            client_list.append(client)

    return client_list
