# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from Users.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^bind/', include('bind.urls')),
    url(r'^users/', include('Users.urls')),
    url(r'^assets/', include('assets.urls')),
    url(r'^faults/', include('faults.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
]
