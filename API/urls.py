# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^idc_valid', views.IDC_Valid, name='idc_valid'),
	url(r'^cabinet_valid', views.CabinetValid, name='cabinet_valid'),
	url(r'^group_valid/', views.GroupValid, name='group_valid'),
    url(r'^hosts_valid/', views.HostsValid, name='hosts_valid'),
	url(r'^type_valid/', views.FaultTypeValid, name='type_valid'),
	url(r'^fault_valid', views.FaultValid, name='fault_valid'),
]