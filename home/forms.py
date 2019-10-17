from django import forms
from django.contrib.auth.models import User
from appointment.models import ..........

class AppointmentForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Введите ваше Имя и Фамилию")
	doctor = forms.CharField(max_length=128, help_text="К какому врачу вы бы хотели записаться?")
    problem = forms.CharField(max_length=128, help_text="Причина записи")
    date = forms.CharField(max_length=128, help_text="На какую дату вы бы хотели записаться?")
    time = forms.CharField(max_length=128, help_text="Какое время дня для вас предпочтительно?")
	contact = forms.CharField(max_length=128, help_text="Как с вами лучше связаться?")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Appointment
        fields = ('name', 'doctor', 'problem', 'date', 'time')
