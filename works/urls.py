from django.conf.urls import patterns, include, url
from works import views

urlpatterns = patterns('',
        url(r'^$', views.works, name='works'),
		url(r'^works', views.works, name='works'),
		url(r'^(?P<work_id>[^/]+)/$', views.detail, name='detail')
		)