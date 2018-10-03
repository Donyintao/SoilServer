# -*- coding: utf-8 -*-

import sys
import json
from models import *
from API.forms import *
import django.utils.timezone as timezone
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

'''DNS列表'''
def DNS_List(request):
	DNS_List = DNS.objects.all().values('id', 'zone', 'host', 'type', 'data', 'ttl', 'create_datetime', 'update_datetime')
	# DNS类型
	DNS_TYPE = DNS.dns_type_choice
	return render(request, 'dns/dns_list.html', {'DNS': DNS_List, 'DNS_TYPE': DNS_TYPE})

'''域名添加操作'''
@csrf_exempt
def DNS_Add(request):
	if request.method == 'POST':
		dns_form = DNSValidForm(request.POST)
		if dns_form.is_valid():
			host = dns_form.cleaned_data['host']
			type = dns_form.cleaned_data['type']
			data = dns_form.cleaned_data['data']
			AddObj = DNS(zone='missfresh.net', host=host, type=type, data=data, ttl='60')
			AddObj.save()
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		idc_form = DNSValidForm()

'''域名删除操作'''
@csrf_exempt
def DNS_Del(request):
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
		idc_form = DNSValidForm()

'''域名编辑操作'''
def DNS_Profile(request):
	if request.method == 'GET':
		id = request.GET['id']
		DNS_List = DNS.objects.filter(id=id).values('id', 'zone', 'host', 'type', 'data', 'ttl')
		# DNS类型
		DNS_TYPE = DNS.dns_type_choice
	return render(request,'dns/dns_profile.html', {'DNS': DNS_List, 'DNS_TYPE': DNS_TYPE})

'''域名更新操作'''
@csrf_exempt
def DNS_Update(request):
	if request.method == 'POST':
		dns_upform = DNSValidForm(request.POST)
		print dns_upform
		if dns_upform.is_valid():
			id = dns_upform.cleaned_data['id']
			host = dns_upform.cleaned_data['host']
			type = dns_upform.cleaned_data['type']
			data = dns_upform.cleaned_data['data']
			UpdateObj = DNS.objects.filter(id=id).update(zone='missfresh.net',
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
		idc_upform = DNSValidForm()