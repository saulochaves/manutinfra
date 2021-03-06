# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from manutinfra.api import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manutinfra.views.home', name='home'),
    # url(r'^manutinfra/', include('manutinfra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^$', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve',{ 'document_root': settings.MEDIA_ROOT }),
	(r'^api/',include ('manutinfra.api.urls')),
    (r'^$','django.contrib.auth.views.login',{'template_name' : 'login.html'}),
)
