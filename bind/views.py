# -*- coding: utf-8 -*-

import sys
import json
from models import *
from forms import *
import django.utils.timezone as timezone
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

'''Domain列表'''
@csrf_exempt
@login_required(login_url="/users/login/")
def DomainList(request):
    if request.method == 'GET':
        # Domain 列表
        result = DNS.objects.all()
        return render(request, 'bind/list.html', {'result': result})

'''Domain添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def DomainAdd(request):
    if request.method == 'GET':
        bind_type = DNS.dns_type_choice
        bind_zone = DNS.dns_zone_choice
        return render(request, 'bind/add.html', {'bind_type': bind_type, 'bind_zone': bind_zone})
    elif request.method == 'POST':
        dns_form = BindValidForm(request.POST)
        if dns_form.is_valid():
            zone = request.POST.get('zone')
            host = dns_form.cleaned_data['host']
            Type = dns_form.cleaned_data['type']
            data = dns_form.cleaned_data['data']
            # 添加解析
            AddObj = DNS(zone=zone, host=host, type=Type, data=data, ttl='60')
            AddObj.save()

            # 数据添加状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据添加状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        dns_form = BindValidForm()

'''域名删除操作'''
@csrf_exempt
@login_required(login_url="/users/login/")
def DomainDel(request):
    if request.method == 'POST':
        dns_delform = BindValidForm(request.POST)
        if dns_delform.is_valid():
            id = dns_delform.cleaned_data['id']
            DelObj = DNS.objects.filter(id=id).delete()
            # 数据添加状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据添加状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        dns_delform = BindValidForm()

'''域名编辑操作'''
def DomainProfile(request):
    if request.method == 'GET':
        id = request.GET['id']
        result = DNS.objects.filter(id=id).values('id', 'zone', 'host', 'type', 'data', 'ttl')
        bind_type = DNS.dns_type_choice
        bind_zone = DNS.dns_zone_choice
    return render(request, 'bind/profile.html', {'result': result, 'bind_type': bind_type, 'bind_zone': bind_zone})


'''域名更新操作'''
@csrf_exempt
def DomainUpdate(request):
    if request.method == 'POST':
        dns_upform = BindValidForm(request.POST)
        if dns_upform.is_valid():
            id = dns_upform.cleaned_data['id']
            zone = request.POST['zone']
            host = dns_upform.cleaned_data['host']
            type = dns_upform.cleaned_data['type']
            data = dns_upform.cleaned_data['data']

            # 更新域名信息
            UpdateObj = DNS.objects.filter(id=id).update(zone=zone,
                                                         host=host,
                                                         type=type,
                                                         data=data,
                                                         ttl='60',
                                                         update_datetime=timezone.now())

            # 数据更新状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据更新状态：false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        dns_upform = BindValidForm()