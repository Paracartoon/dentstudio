from django.conf.urls import patterns, include, url
from job import views

urlpatterns = patterns('',
        url(r'^$', views.job, name='job'),
		url(r'^job', views.job, name='job'),
		
		)