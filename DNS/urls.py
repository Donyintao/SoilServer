# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	# Zone URL
	url(r'^zone_list/', views.ZoneList, name='zone_list'),
	url(r'^zone_add/', views.AddZone, name='zone_add'),
	# DNS URL
	url('^setting/', views.DNSList, name='setting'),
    url(r'^dns_add/', views.AddDNS, name='dns_add'),
	url(r'^dns_delete/', views.DNSDel, name='dns_delete'),
    url(r'^profile/', views.DNSProfile, name='profile'),
	url(r'^dns_update/', views.DNSUpdate, name='dns_update'),
]