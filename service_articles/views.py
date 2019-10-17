from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from service_articles.models import Cosmetology, Gnatology, Terapy, Ortoped, Ortodont, Hygiene, Implant, Parodontology
from django.http import HttpResponseNotFound

def cosmetology(request):

    articles_list = Cosmetology.objects.order_by('-date')[:50]
    mainx = Cosmetology.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/cosmetology.html', context_dict)
    return response

def detail_cosmetology(request,article_id):
    try:
        article = Cosmetology.objects.get(link=article_id)
    except Cosmetology.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_cosmetology.html', {'article': article})
	
def detail_gnatology(request,article_id):
    try:
        article = Gnatology.objects.get(link=article_id)
    except Gnatology.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_gnatology.html', {'article': article})
	
def gnatology(request):

    articles_list = Gnatology.objects.all()
    mainx = Gnatology.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/gnatology.html', context_dict)
    return response

def parodontology(request):

    articles_list = Parodontology.objects.order_by('-date')[:50]
    mainx = Parodontology.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/parodont.html', context_dict)
    return response

def detail_parodontology(request,article_id):
    try:
        article = Parodontology.objects.get(link=article_id)
    except Parodontology.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_parodontology.html', {'article': article})
	
def terapy(request):

    articles_list = Terapy.objects.order_by('-date')[:50]
    mainx = Terapy.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/terapy.html', context_dict)
    return response

def detail_terapy(request,article_id):
    try:
        article = Terapy.objects.get(link=article_id)
    except Terapy.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_terapy.html', {'article': article})
	
def ortoped(request):

    articles_list = Ortoped.objects.order_by('-date')[:50]
    mainx = Ortoped.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/ortoped.html', context_dict)
    return response
	
def detail_ortoped(request,article_id):
    try:
        article = Ortoped.objects.get(link=article_id)
    except Ortoped.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_ortoped.html', {'article': article})
	
def implant(request):

    articles_list = Implant.objects.order_by('-date')[:50]
    mainx = Implant.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/implant.html', context_dict)
    return response	
	
def detail_implant(request,article_id):
    try:
        article = Implant.objects.get(link=article_id)
    except Implant.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_implant.html', {'article': article})
	
def ortodont(request):

    articles_list = Ortodont.objects.order_by('-date')[:50]
    mainx = Ortodont.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/ortodont.html', context_dict)
    return response
	
def detail_ortodont(request,article_id):
    try:
        article = Ortodont.objects.get(link=article_id)
    except Ortodont.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_ortodont.html', {'article': article})
	
def hygiene(request):

    articles_list = Hygiene.objects.order_by('-date')[:50]
    mainx = Hygiene.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_articles/hygiene.html', context_dict)
    return response
	
def detail_hygiene(request,article_id):
    try:
        article = Hygiene.objects.get(link=article_id)
    except Hygiene.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_articles/generic_hygiene.html', {'article': article})

