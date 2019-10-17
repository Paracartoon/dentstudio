from django.conf.urls import patterns, include, url
from news import views

urlpatterns = patterns('',
        url(r'^$', views.news, name='news'),
		url(r'^(?P<news_id>[^/]+)/$', views.detail, name='detail') #news_id задается в качестве переменной в views, очень аккуратно с регексом!
		
		)