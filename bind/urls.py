# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/', views.DomainAdd, name='domain_add'),
    url(r'^list/', views.DomainList, name='domain_list'),
    url(r'^delete/', views.DomainDel, name='domain_delete'),
    url(r'^update/', views.DomainUpdate, name='domain_update'),
    url(r'^profile/', views.DomainProfile, name='domain_profile'),
]