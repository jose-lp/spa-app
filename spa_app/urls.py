"""spa_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from appointments import views
import appointments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('appointments/', views.appointments, name='appointments'),
    path('edit_appointment/', views.edit_appointment, name='edit_appointment'),
    path('appointments_admin/', views.appointments_admin, name='appointments_admin'),
    path('edit_appointment_admin/', views.edit_appointment_admin, name='edit_appointment_admin'),
]
