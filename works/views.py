from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from works.models import Work, WorkImage
from django.http import HttpResponseNotFound

def works(request):
    works_list = Work.objects.all()
    context_dict = {'works': works_list}
    response = render(request, 'home/works.html', context_dict)
    return response
	
def detail(request, work_id):
    try:
        work = Work.objects.get(link=work_id)
        images = WorkImage.objects.filter(work_number=work_id)
    except Work.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами работа не найдена")  
    return render(request, 'works/generic.html', {'work': work, 'images': images})