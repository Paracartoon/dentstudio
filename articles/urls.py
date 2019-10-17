from django.conf.urls import patterns, include, url
from articles import views

urlpatterns = patterns('',
        url(r'^$', views.articles, name='articles'),
		url(r'^articles', views.articles, name='articles'),
		url(r'^(?P<article_id>[^/]+)/$', views.detail, name='detail')
		)
