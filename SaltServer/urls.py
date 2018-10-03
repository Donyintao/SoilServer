# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from Auth import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^api/', include('API.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^cmdb/', include('CMDB.urls')),
	url(r'^dns/', include('DNS.urls')),
    url(r'^fault/', include('Fault.urls')),
    url(r'^users/', include('Users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
]
