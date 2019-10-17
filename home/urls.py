from django.conf.urls import patterns, include, url
from home import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^inside/', views.inside, name='inside'),
		url(r'^accounts/', include('allauth.urls')),
		
		)