# -*- coding: utf-8 -*-

import json
from forms import *
from models import *
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

'''机房校验'''
@csrf_exempt
def IDC_Valid(request):
    if request.method == 'POST':
        idc_validform = IDCValidForm(request.POST)
        if idc_validform.is_valid():
            # 数据校验状态: true表示正常.
            return HttpResponse(json.dumps({'valid': 'true'}))
        else:
            # 数据校验状态: false表示异常.
            return HttpResponse(json.dumps({'valid': 'false'}))
    else:
        idc_validform = IDCValidForm()

'''机柜校验'''
@csrf_exempt
def CabinetValid(request):
    if request.method == 'POST':
        cabinet_validform = CabinetValidForm(request.POST)
        if cabinet_validform.is_valid():
            # 校验状态: true表示正常.
            return HttpResponse(json.dumps({'valid': 'true'}))
        else:
            # 校验状态: false表示异常.
            return HttpResponse(json.dumps({'valid': 'false'}))
    else:
        cabinet_validform = CabinetValidForm()


'''主机组校验'''
@csrf_exempt
def GroupValid(request):
	if request.method == 'POST':
		group_validform = GroupValidForm(request.POST)
		if group_validform.is_valid():
			return HttpResponse(json.dumps({'valid': 'true'}))
		else:
			return HttpResponse(json.dumps({'valid': 'false'}))
	else:
		group_validform = GroupValidForm()
		
'''主机校验'''
@csrf_exempt
def HostsValid(request):
	if request.method == 'POST':
		hosts_validform = HostsValidForm(request.POST)
		if hosts_validform.is_valid():
			return HttpResponse(json.dumps({'valid': 'true'}))
		else:
			return HttpResponse(json.dumps({'valid': 'false'}))
	else:
		hosts_validform = HostsValidForm()

'''故障类型校验'''
@csrf_exempt
def FaultTypeValid(request):
	if request.method == 'POST':
		type_validform = FaultTypeValidForm(request.POST)
		if type_validform.is_valid():
			return HttpResponse(json.dumps({'valid': 'true'}))
		else:
			return HttpResponse(json.dumps({'valid': 'false'}))
	else:
		type_validform = FaultTypeValidForm()
		
'''故障信息校验'''
@csrf_exempt
def FaultValid(request):
	if request.method == 'POST':
		fault_validform = FaultValidForm(request.POST)
		if fault_validform.is_valid():
			return HttpResponse(json.dumps({'valid': 'true'}))
		else:
			return HttpResponse(json.dumps({'valid': 'false'}))
	else:
		fault_validform = FaultValidForm()