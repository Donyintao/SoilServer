# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # IDC URL
    url(r'^idc_add/', views.IDC_Add, name='idc_add'),
    url(r'^idc_list/', views.IDC_List, name='idc_list'),
    url(r'^idc_valid', views.IDC_Valid, name='idc_valid'),
    url(r'^idc_delete/', views.IDC_Del, name='idc_delete'),
    url(r'^idc_update/', views.IDC_Update, name='idc_update'),
    url(r'^idc_profile/', views.IDC_Profile, name='idc_profile'),
    # Cabinet URL
    url(r'^cabinet_list/', views.Cabinet, name='cabinet_list'),
    url(r'^cabinet_add/', views.CabinetAdd, name='cabinet_add'),
    url(r'^cabinet_valid', views.CabinetValid, name='cabinet_valid'),
    url(r'^cabinet_delete/', views.CabinetDel, name='cabinet_delete'),
    url(r'^cabinet_update/', views.CabinetUpdate, name='cabinet_update'),
    url(r'^cabinet_profile/',views.CabinetProfile, name='cabinet_profile'),
    # Group URL
    url(r'^group_list/', views.Group, name='group_list'),
    url(r'^group_add/', views.GroupAdd, name='group_add'),
    url(r'^group_valid/', views.GroupValid, name='group_valid'),
    url(r'^group_delete/', views.GroupDel, name='group_delete'),
    url(r'^group_update/', views.GroupUpdate, name='group_update'),
    url(r'^group_profile', views.GroupProfile, name='group_profile'),
    # Firm URL
    url(r'^firm_list/', views.Firm, name='firm_list'),
    url(r'^firm_add/', views.FirmAdd, name='firm_add'),
    url(r'^firm_delete/', views.FirmDel, name='firm_delete'),
    url(r'^firm_update/', views.FirmUpdate, name='firm_update'),
    url(r'^firm_profile/', views.FirmProfile, name='firm_profile'),
    # Hosts URL
    url(r'^hosts_list/', views.Hosts, name='hosts_list'),
    url(r'^hosts_add/', views.HostsAdd, name='hosts_add'),
    url(r'^hosts_valid/', views.HostsValid, name='hosts_valid'),
    url(r'^hosts_delete/', views.HostsDel, name='hosts_delete'),
    url(r'^hosts_update/', views.HostsUpdate, name='hosts_update'),
    url(r'^hosts_profile/', views.HostsProfile, name='hosts_profile'),
    url(r'^hosts_details/', views.HostsDetails, name='hosts_details'),
    url(r'^hosts_upvalid/', views.HostsUpValid, name='hosts_upvalid'),
    # Seleted URL
    url(r'^idc_seleted/', views.SeletedIDC, name='idc_seleted'),
    url(r'^firm_seleted/', views.SeletedFirm, name='firm_seleted'),
    url(r'^group_seleted/', views.SeletedGroup, name='group_seleted'),
    url(r'^users_seleted/', views.SeletedUsers, name='users_seleted'),
    url(r'^cabinet_seleted/', views.SeletedCabinet, name='cabinet_seleted'),
]