from django.conf.urls import patterns, include, url
from service_cosmetology import views

urlpatterns = patterns('',
        url(r'^$', views.articles_cosmetology, name='articles_cosmetology'),
		url(r'^service_cosmetology', views.articles_cosmetology, name='articles_cosmetology'),
		url(r'^(?P<article_id>[^/]+)/$', views.detail, name='detail')
		)