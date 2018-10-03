# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	# DNS URL
	url(r'^list/', views.DNS_List, name='dns_list'),
    url(r'^add/', views.DNS_Add, name='dns_add'),
	url(r'^delete/', views.DNS_Del, name='dns_delete'),
    url(r'^profile/', views.DNS_Profile, name='dns_profile'),
	url(r'^update/', views.DNS_Update, name='dns_update'),
]