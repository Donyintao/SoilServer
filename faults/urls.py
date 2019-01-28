# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # Faults URL
    url(r'^add/', views.FaultsAdd, name='faults_add'),
    url(r'^list/', views.FaultsList, name='faults_list'),
    url(r'^delete/', views.FaultsDel, name='faults_delete'),
    url(r'^update/', views.FaultsUpdate, name='faults_update'),
    url(r'^details/', views.FaultsDetails, name='faults_details'),
    url(r'^profile/', views.FaultsProfile, name='faults_profile'),
    # Fault Seleted
    url(r'^level_seleted/', views.SeletedLevel, name='level_seleted'),
    url(r'^class_seleted/', views.SeletedClass, name='class_seleted'),
    url(r'^status_seleted', views.SeletedStatus, name='status_seleted'),
    url(r'^project_seleted/', views.SeletedProject, name='project_seleted'),
    url(r'^improve_seleted/', views.SeletedImprove, name='improve_seleted'),
]