from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from news.models import New
from django.http import HttpResponseNotFound

def news(request):

    news_list = New.objects.all()
    context_dict = {'news': news_list,}
    response = render(request,'news/news.html', context_dict)
    return response
	
def detail(request, news_id):

    try:
        news = New.objects.get(link=news_id) #линк как связь с атрибутами конкретного объекта модели (бд)
    except New.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами новость не найдена")
    return render(request, 'news/generic.html', {'news': news})
	

