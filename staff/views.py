from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from staff.models import Staff

def people(request):
    staff_list = Staff.objects.all()
    context_dict = {'staff': staff_list,}
    response = render(request, 'home/people.html', context_dict)
    return response
	
def detail(request, person_id):
    
    staff = Staff.objects.get(link=person_id)
    return render(request, 'staff/generic.html', {'staff': staff})