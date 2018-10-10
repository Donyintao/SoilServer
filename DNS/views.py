# -*- coding: utf-8 -*-

import sys
import json
from models import *
from API.forms import *
import django.utils.timezone as timezone
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


'''Zone列表'''
@csrf_exempt
def ZoneList(request):
	if request.method == 'GET':
		result = Zone.objects.all()
		return render(request, 'dns/zone_list.html', {'result': result})

'''Zone添加'''
@csrf_exempt
def AddZone(request):
	if request.method == 'POST':
		zone_form = ZoneValidForm(request.POST)
		if zone_form.is_valid():
			name = zone_form.cleaned_data['name']
			# 添加域名
			AddObj = Zone(name=name)
			AddObj.save()
			
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		zone_form = ZoneValidForm()

'''DNS列表'''
@csrf_exempt
def DNSList(request):
	if request.method == 'GET':
		name = request.GET['name']
		# 获取Zone信息
		ZoneObj = Zone.objects.filter(name=name).values('id','name')
		zone = ZoneObj[0]['id']
		# DNS 列表
		DNSList = DNS.objects.filter(zone=zone).values('id', 'zone', 'zone__name', 'host', 'type', 'data', 'ttl', 'create_datetime', 'update_datetime')
		# DNS类型
		DNS_TYPE = DNS.dns_type_choice
		return render(request, 'dns/dns_list.html', {'ZoneObj': ZoneObj, 'DNSList': DNSList, 'DNS_TYPE': DNS_TYPE})

'''域名添加操作'''
@csrf_exempt
def AddDNS(request):
	if request.method == 'POST':
		dns_form = DNSValidForm(request.POST)
		if dns_form.is_valid():
			# Zone ID信息
			id = request.POST['id']
			host = dns_form.cleaned_data['host']
			type = dns_form.cleaned_data['type']
			data = dns_form.cleaned_data['data']
			# 获取Zone名称
			name = Zone.objects.filter(id=id).values('name')[0]['name']
			zone = Zone.objects.get(name=name)
			# 添加解析
			AddObj = DNS(zone=zone, host=host, type=type, data=data, ttl='60')
			AddObj.save()
			
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		dns_form = DNSValidForm()

'''域名删除操作'''
@csrf_exempt
def DNSDel(request):
	if request.method == 'POST':
		dns_delform = DNSValidForm(request.POST)
		if dns_delform.is_valid():
			id = dns_delform.cleaned_data['id']
			DelObj = DNS.objects.filter(id=id).delete()
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		dns_delform = DNSValidForm()

'''域名编辑操作'''
def DNSProfile(request):
	if request.method == 'GET':
		id = request.GET['id']
		DNSList = DNS.objects.filter(id=id).values('id', 'zone', 'zone__name', 'host', 'type', 'data', 'ttl')
		# DNS类型
		DNS_TYPE = DNS.dns_type_choice
	return render(request,'dns/dns_profile.html', {'DNSList': DNSList, 'DNS_TYPE': DNS_TYPE})

'''域名更新操作'''
@csrf_exempt
def DNSUpdate(request):
	if request.method == 'POST':
		dns_upform = DNSValidForm(request.POST)
		if dns_upform.is_valid():
			id = dns_upform.cleaned_data['id']
			zone = request.POST['zone']
			host = dns_upform.cleaned_data['host']
			type = dns_upform.cleaned_data['type']
			data = dns_upform.cleaned_data['data']
			
			# 获取Zone信息
			ZoneObj = Zone.objects.filter(id=zone).values('id', 'name')
			zone = ZoneObj[0]['id']
			
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
		dns_upform = DNSValidForm()