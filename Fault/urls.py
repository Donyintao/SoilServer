# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	# Fault URL
	url(r'^fault_add/', views.FaultAdd, name='fault_add'),
	url(r'^fault_list/', views.FaultList, name='fault_list'),
	url(r'^fault_delete/', views.FaultDel, name='fault_delete'),
	url(r'^fault_details/',views.FaultDetails, name='fault_details'),
	# Fault Type URL
	url(r'^type_list/', views.TypeList, name='type_list'),
	url(r'^type_add/', views.TypeAdd, name='type_add'),
	# Fault Seleted
	url(r'^level_seleted/', views.SeletedLevel, name='level_seleted'),
    url(r'^types_seleted/', views.SeletedTyeps, name='types_seleted'),
	url(r'^project_seleted/', views.SeletedProject, name='project_seleted'),
	url(r'^status_seleted/', views.SeletedStatus, name='status_seleted'),
	url(r'^improve_seleted/', views.SeletedImprove, name='improve_seleted'),
]