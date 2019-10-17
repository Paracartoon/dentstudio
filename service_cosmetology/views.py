from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from service_cosmetology.models import Article_Cosmetology
from django.http import HttpResponseNotFound

def articles_cosmetology(request):

    articles_list = Article_Cosmetology.objects.all()
    mainx = Article_Cosmetology.objects.get(link="mainx")
    context_dict = {'articles': articles_list, 'mainx':mainx}
    response = render(request,'service_cosmetology/articles.html', context_dict)
    return response
	
def detail(request,article_id):
    try:
        article = Article_Cosmetology.objects.get(link=article_id)
    except Article_Cosmetology.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'service_cosmetology/generic.html', {'article': article})
