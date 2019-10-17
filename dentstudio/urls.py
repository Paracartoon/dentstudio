from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dentstudio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^home/', include('home.urls')),
	url(r'^appointment/', include('appointment.urls')),
    url(r'^people/', include('staff.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^inside/', views.inside, name='inside'),
    url(r'^chat/', views.chat, name='chat'),
	url(r'^accounts/', include('allauth.urls')),
    url(r'^job/', include('job.urls')),
    url(r'^news/', include('news.urls')),
	url(r'^prices/', views.prices, name='prices'),
	url(r'^services/', views.services, name='services'),
	url(r'^contacts/', views.contacts, name='contacts'),
	url(r'^articles/', include('articles.urls')),
	url(r'^works/', include('works.urls')),
	url(r'^service_articles/', include('service_articles.urls')),
	url(r'^photologue/', include('photologue.urls', namespace='photologue')),
	url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt',
                                            content_type='text/plain')),
	url(r'^sitemap\.xml/$', TemplateView.as_view(template_name='sitemap.xml',
                                            content_type='text/plain')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )



