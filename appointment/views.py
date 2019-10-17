from django.shortcuts import render
from appointment.forms import AppointmentForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext


def appointment_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppointmentForm(request.POST)
	
        if form.is_valid():
            
            name = str(form.cleaned_data['name'])
            doctor = str(form.cleaned_data['doctor'])
            problem = str(form.cleaned_data['problem'])
            date = str(form.cleaned_data['date'])
            time = str(form.cleaned_data['time'])
            contact = str(form.cleaned_data['contact'])
            email = str(form.cleaned_data['email'])
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['paracartoon@gmail.com', 'doctor@dentstudio.ru']
            if cc_myself:
                recipients.append(email)
            send_mail('Dent Studio APPOINTMENT REQUEST', '\nИмя пациента: '+name+'\nЗапись к врачу: '+doctor+'\nПричина записи: '+problem+'\nПредпочтительная дата приема: '+date+'\nПредпочтительное время приема: '+time+'\nКонтактный телефон: '+contact+'\nЭлектронная почта: '+email, 'noreply@dentstudio.ru', recipients)
            return render(request, 'appointment/sent_ok.html')
        else:
            return render(request, 'appointment/appointment.html', {'form': form})
    else:
        form = AppointmentForm()

        return render(request, 'appointment/appointment.html', {'form': form})


def sent_ok(request):
    return render(request, 'appointment/sent_ok.html')
