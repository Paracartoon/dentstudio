from django.conf.urls import patterns, include, url
from appointment import views

urlpatterns = patterns('',
        url(r'^$', views.appointment_form, name='appointment'),
		url(r'^appointment', views.appointment_form, name='appointment'),
		url(r'^sent_ok/', views.sent_ok, name='appointment/sent_ok'),
		)