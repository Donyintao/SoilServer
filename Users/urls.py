# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/', views.UserList, name='users_list'),
]