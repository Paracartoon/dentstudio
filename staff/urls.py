from django.conf.urls import patterns, include, url
from staff import views

urlpatterns = patterns('',
        url(r'^$', views.people, name='people'),
		url(r'^people', views.people, name='people'),
		url(r'^(?P<person_id>[^/]+)/$', views.detail, name='detail')
		)