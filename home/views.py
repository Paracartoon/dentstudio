from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from news.models import New
from articles.models import Article
from home.models import Customer
from django.contrib.auth.models import User
from service_articles.models import Cosmetology, Gnatology, Terapy, Ortoped, Ortodont, Hygiene, Implant, Parodontology


def index(request):
    news_list = New.objects.order_by('-date')[:2]
    articles_list = Article.objects.order_by('-date')[:3]
    context_dict = {'news': news_list, 'articles': articles_list,}
    response = render(request,'home/index.html', context_dict)
    return response
	
def inside(request):

    context_dict = {}
    response = render(request,'home/inside.html', context_dict)
    return response

def profile(request):
    
   
    context_dict = {}
    response = render(request,'account/profile.html', context_dict)
    return response
	
def chat(request):

    context_dict = {}
    response = render(request,'home/chat.html', context_dict)
    return response
 
def contacts(request):
    
    context_dict = {}
    response = render(request,'home/contacts.html', context_dict)
    return response

	
def services(request):

    implant = Implant.objects.order_by('-date')[:2]
    ortoped = Ortoped.objects.order_by('-date')[:2]
    gnatolog = Gnatology.objects.order_by('-date')[:2]
    ortodont = Ortodont.objects.order_by('-date')[:2]
    terapy = Terapy.objects.order_by('-date')[:2]
    hygiene = Hygiene.objects.order_by('-date')[:2]
    cosmetolog = Cosmetology.objects.order_by('-date')[:2]
    parodont = Parodontology.objects.order_by('-date')[:2]
    context_dict = {'implantolog': implant, 'ortoped': ortoped, 'gnatolog': gnatolog, 'terapy': terapy, 'hygiene': hygiene, 'cosmetolog': cosmetolog, 'parodont': parodont, 'ortodont': ortodont}
    response = render(request,'home/services.html', context_dict)
    return response
	
def prices(request):

    context_dict = {}
    response = render(request,'home/prices.html', context_dict)
    return response
	

 

 


