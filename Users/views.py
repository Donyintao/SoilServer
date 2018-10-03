# -*- coding: UTF-8 -*-

from Auth.models import CustomUsers
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/users/login/")
def UserList(request):
	UserObj = CustomUsers.objects.all()
	UsersList = UserObj.values('id',
	                           'username',
	                           'nickname',
	                           'email',
	                           'is_active',
	                           'phone',
	                           'department',
	                           'last_login',
	                           'groups__name')
	return render(request, 'users/users_list.html',{'Users': UsersList})