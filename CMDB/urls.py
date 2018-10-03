# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	# IDC URL
	url(r'^idc_list/', views.IDC_List, name='idc_list'),
	url(r'^idc_add/', views.IDC_Add, name='idc_add'),
	url(r'^idc_delete/', views.IDC_Del, name='idc_delete'),
	url(r'^idc_profile/', views.IDC_Profile, name='idc_profile'),
	url(r'^idc_update/', views.IDC_Update, name='idc_update'),
	# Cabinet URL
	url(r'^cabinet_list/', views.Cabinet, name='cabinet_list'),
	url(r'^cabinet_add/', views.CabinetAdd, name='cabinet_add'),
    url(r'^cabinet_profile/',views.CabinetProfile, name='cabinet_profile'),
	url(r'^cabinet_update/', views.CabinetUpdate, name='cabinet_update'),
	url(r'^cabinet_delete/', views.CabinetDel, name='cabinet_delete'),
	# Group URL
    url(r'^group_list/', views.HostsGroup, name='group_list'),
    url(r'^group_add/', views.GroupAdd, name='group_add'),
    url(r'^group_update/', views.GroupUpdate, name='group_update'),
    url(r'^group_profile', views.GroupProfile, name='group_profile'),
    url(r'^group_delete/', views.GroupDel, name='group_delete'),
	# Hosts URL
	url(r'^hosts_list/', views.HostsList, name='hosts_list'),
	url(r'^hosts_add/', views.AddHosts, name='hosts_add'),
	url(r'^hosts_delete/', views.HostsDel, name='hosts_delete'),
	url(r'^hosts_profile/', views.HostsProfile, name='hosts_profile'),
	url(r'^hosts_update', views.HostsUpdate, name='hosts_update'),
	url(r'^hosts_details/', views.HostsDetails, name='hosts_details'),
	# Seleted URL
	url(r'^idc_seleted/', views.SeletedIDC, name='idc_seleted'),
	url(r'^cabinet_seleted/', views.SeletedCabinet, name='cabinet_seleted'),
	url(r'^group_seleted/', views.SeletedGroup, name='group_seleted'),
]