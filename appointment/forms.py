from django import forms
from django.db import models
from django.contrib.auth.models import User
from appointment.models import Doctor, Reason, Daytime, Appointment
import datetime

class AppointmentForm(forms.Form):
    name = forms.CharField(label='Ваше имя и фамилия ', max_length=400)
    doctor = forms.ModelChoiceField(label='К какому врачу вы хотели бы записаться ', queryset=Doctor.objects.all())
    problem = forms.ModelChoiceField(label='Причина записи       ', queryset=Reason.objects.all())
    date = forms.CharField(label='Предпочтительная дата записи ', max_length=128)
    time = forms.ModelChoiceField(label='Предпочтительное время дня     ', queryset=Daytime.objects.all()) 
    contact = forms.CharField(label='Ваш контактный телефон ', max_length=128)
    email = forms.EmailField(label='Ваш e-mail      ', max_length=128)
    cc_myself = forms.BooleanField(label='Копия себе ', required=False)
	
    
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Appointment
       
