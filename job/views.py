from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from job.models import Vacancy

def job(request):

    job_list = Vacancy.objects.all()
    context_dict = {'vacancy': job_list,}
    response = render(request,'home/job.html', context_dict)
    return response