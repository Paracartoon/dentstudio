from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from articles.models import Article
from django.http import HttpResponseNotFound

def articles(request):

    articles_list = Article.objects.all()
    context_dict = {'articles': articles_list,}
    response = render(request,'home/articles.html', context_dict)
    return response
	
def detail(request,article_id):
    try:
        article = Article.objects.get(link=article_id)
    except Article.DoesNotExist:
        return HttpResponseNotFound("К сожалению, запрошенная вами статья не найдена")
    return render(request, 'articles/generic.html', {'article': article})