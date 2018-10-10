# -*- coding: utf-8 -*-

import sys
import json
import time
from models import *
from API.forms import *
import django.utils.timezone as timezone
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

'''故障类型列表'''
@csrf_exempt
@login_required(login_url="/users/login/")
def TypeList(request):
	TypeList = FaultType.objects.all().values('id','name')
	return render(request, 'fault/type_list.html', {'Fault': TypeList})

'''故障类型添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def TypeAdd(request):
	if request.method == 'POST':
		type_form = FaultTypeValidForm(request.POST)
		if type_form.is_valid():
			name = type_form.cleaned_data['name']
			AddObj = FaultType(name=name)
			AddObj.save()
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		type_form = FaultTypeValidForm()

'''统计时间'''
def CountTime(FaultObj,start_time,end_time):

	start_time = time.strptime(str(start_time).split('+')[0], "%Y-%m-%d %H:%M:%S")
	end_time = time.strptime(str(end_time).split('+')[0], "%Y-%m-%d %H:%M:%S")
	timestamp = int(time.mktime(end_time)) - int(time.mktime(start_time))
	
	setattr(FaultObj, 'time', str(timestamp // 3600) + '小时' + str(timestamp % 3600 // 60) + '分')

'''故障列表'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultList(request):
	FaultObj = FaultContent.objects.select_related().all()
	for fault in FaultObj:
		CountTime(fault, fault.start_time, fault.end_time)
	return render(request, 'fault/fault_list.html', {'FaultObj': FaultObj})

'''故障添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultAdd(request):
	if request.method == 'GET':
		return render(request, 'fault/fault_add.html')
	elif request.method == 'POST':
		fault_form = FaultValidForm(request.POST)
		if fault_form.is_valid():
			# 项目概述
			name = fault_form.cleaned_data['name']
			# 项目级别
			level = fault_form.cleaned_data['level']
			# 项目类型
			type = fault_form.cleaned_data['type']
			# 影响项目
			project = fault_form.cleaned_data['project']
			# 故障状态
			status = fault_form.cleaned_data['status']
			# 主导改进
			improve = fault_form.cleaned_data['improve']
			# 开始时间
			start_time = fault_form.cleaned_data['start_time']
			# 结束时间
			end_time = fault_form.cleaned_data['end_time']
			# 故障影响
			effect = fault_form.cleaned_data['effect']
			# 处理流程
			content = fault_form.cleaned_data['content']
			# 故障原因
			reasons = fault_form.cleaned_data['reasons']
			# 解决方案
			solution = fault_form.cleaned_data['solution']
			# 经验总结
			lesson = fault_form.cleaned_data['lesson']
			
			# 获取项目类型
			Type_name = FaultType.objects.filter(id=type).values('name')
			Types = FaultType.objects.get(name=Type_name)
			
			# 添加数据
			AddObj = FaultContent(name=name,
			                      level = level,
								  type = Types,
								  project = project,
								  status = status,
								  improve = improve,
								  effect = effect,
								  content = content,
								  reasons = reasons,
								  solution = solution,
								  lesson = lesson,
			                      start_time=start_time,
			                      end_time=end_time)
			AddObj.save()
			
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		fault_form = FaultValidForm()


'''故障更新'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultUpdate(request):
	if request.method == 'POST':
		fault_upform = FaultValidForm(request.POST)
		if fault_upform.is_valid():
			id = fault_upform.cleaned_data['id']
			# 项目概述
			name = fault_upform.cleaned_data['name']
			# 项目级别
			level = fault_upform.cleaned_data['level']
			# 项目类型
			type = fault_upform.cleaned_data['type']
			# 影响项目
			project = fault_upform.cleaned_data['project']
			# 故障状态
			status = fault_upform.cleaned_data['status']
			# 主导改进
			improve = fault_upform.cleaned_data['improve']
			# 开始时间
			start_time = fault_upform.cleaned_data['start_time']
			# 结束时间
			end_time = fault_upform.cleaned_data['end_time']
			# 故障影响
			effect = fault_upform.cleaned_data['effect']
			# 处理流程
			content = fault_upform.cleaned_data['content']
			# 故障原因
			reasons = fault_upform.cleaned_data['reasons']
			# 解决方案
			solution = fault_upform.cleaned_data['solution']
			# 经验总结
			lesson = fault_upform.cleaned_data['lesson']
			
			# 获取项目类型
			Type_name = FaultType.objects.filter(id=type).values('name')
			Types = FaultType.objects.get(name=Type_name)
			
			# 更新数据
			AddObj = FaultContent.objects.filter(id=id).update(name=name,
			                      level=level,
			                      type=Types,
			                      project=project,
			                      status=status,
			                      improve=improve,
			                      effect=effect,
			                      content=content,
			                      reasons=reasons,
			                      solution=solution,
			                      lesson=lesson,
			                      start_time=start_time,
			                      end_time=end_time)
			
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		fault_upform = FaultValidForm()
		
'''故障详情'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultDetails(request):
	if request.method == 'GET':
		id = request.GET['id']
		FaultObj = FaultContent.objects.filter(id=id)
	return render(request, 'fault/fault_details.html', {'Fault': FaultObj})

'''故障编辑'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultProfile(request):
	if request.method == 'GET':
		id = request.GET['id']
		FaultObj = FaultContent.objects.filter(id=id)
	return render(request, 'fault/fault_profile.html', {'Fault': FaultObj})

'''故障删除'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultDel(request):
	if request.method == 'POST':
		fault_delform = FaultDelValidForm(request.POST)
		if fault_delform.is_valid():
			id = fault_delform.cleaned_data['id']
			DelObj = FaultContent.objects.filter(id=id).delete()
			# 数据删除状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据删除状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		idc_delform = IDCValidForm()

'''故障级别列表'''
def SeletedLevel(request):
	if request.method == 'GET':
		result = FaultContent.fault_level_choices
		return HttpResponse(json.dumps(list(result)))

'''项目类型列表'''
def SeletedTyeps(request):
	if request.method == 'GET':
		result = FaultType.objects.all().values('id', 'name')
		return HttpResponse(json.dumps(list(result)))
	
'''项目名称列表'''
def SeletedProject(request):
	if request.method == 'GET':
		result = FaultContent.fault_project_choices
		return HttpResponse(json.dumps(list(result)))
	
'''故障状态列表'''
def SeletedStatus(request):
	if request.method == 'GET':
		result = FaultContent.fault_status_choices
		return HttpResponse(json.dumps(list(result)))
	
'''主导改进列表'''
def SeletedImprove(request):
	if request.method == 'GET':
		result = FaultContent.fault_improve_choices
		return HttpResponse(json.dumps(list(result)))