# -*- coding: utf-8 -*-

from Users.models import CustomUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login/")
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/users/login/")
def UserList(request):
    result = CustomUser.objects.all().values('id',
                            'username',
                            'nickname',
                            'email',
                            'is_active',
                            'phone',
                            'department',
                            'last_login',
                            'groups__name')
    return render(request, 'users/users_list.html', {'result': result})