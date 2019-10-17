from django.conf.urls import patterns, include, url
from service_articles import views

urlpatterns = patterns('',
        url(r'^cosmetology/$', views.cosmetology, name='articles-cosmetology'),
		url(r'^gnatology/$', views.gnatology, name='articles-gnatology'),
		url(r'^terapy/$', views.terapy, name='articles-terapy'),
		url(r'^hygiene/$', views.hygiene, name='articles-hygiene'),
		url(r'^ortoped/$', views.ortoped, name='articles-ortoped'),
		url(r'^ortodont/$', views.ortodont, name='articles-ortodont'),
		url(r'^implant/$', views.implant, name='articles-implant'),
		url(r'^parodont/$', views.parodontology, name='articles-parodont'),
		url(r'^cosmetology/(?P<article_id>[^/]+)/$', views.detail_cosmetology, name='generic_cosmetology'), 
		url(r'^gnatology/(?P<article_id>[^/]+)/$', views.detail_gnatology, name='generic_gnatology'),
		url(r'^terapy/(?P<article_id>[^/]+)/$', views.detail_terapy, name='generic_terapy'),
		url(r'^hygiene/(?P<article_id>[^/]+)/$', views.detail_hygiene, name='generic_hygiene'),
		url(r'^ortoped/(?P<article_id>[^/]+)/$', views.detail_ortoped, name='generic_ortoped'),
		url(r'^ortodont/(?P<article_id>[^/]+)/$', views.detail_ortodont, name='generic_ortodont'),
		url(r'^implant/(?P<article_id>[^/]+)/$', views.detail_implant, name='generic_implant'),
		url(r'^parodont/(?P<article_id>[^/]+)/$', views.detail_parodontology, name='generic_parodont'),
		
		
		)