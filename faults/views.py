# -*- coding: utf-8 -*-

import json
import time
from models import *
from forms import *
import django.utils.timezone as timezone
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

'''统计时间'''
def CountTime(result, start_time, end_time):
    start_time = time.strptime(str(start_time).split('+')[0], "%Y-%m-%d %H:%M:%S")
    end_time = time.strptime(str(end_time).split('+')[0], "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(end_time)) - int(time.mktime(start_time))

    setattr(result, 'time', str(timestamp // 3600) + '小时' + str(timestamp % 3600 // 60) + '分')

'''故障列表'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultsList(request):
    result = FaultsContent.objects.select_related().all()
    for fault in result:
        CountTime(fault, fault.start_time, fault.end_time)
    return render(request, 'faults/list.html', {'result': result})


'''故障添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultsAdd(request):
    if request.method == 'GET':
        return render(request, 'faults/add.html')
    elif request.method == 'POST':
        fault_form = FaultsValidForm(request.POST)
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
            Type_name = FaultsClass.objects.filter(id=type).values('name')
            Type = FaultsClass.objects.get(name=Type_name)

            # 获取项目名称
            project_name = FaultsProject.objects.filter(id=project).values('name')
            project = FaultsProject.objects.get(name=project_name)

            # 添加数据
            AddObj = FaultsContent(name=name,
                                   level=level,
                                   type=Type,
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
            AddObj.save()

            # 数据添加状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据添加状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        fault_form = FaultsValidForm()


'''故障更新'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultsUpdate(request):
    if request.method == 'POST':
        fault_upform = FaultsValidForm(request.POST)
        print fault_upform
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
            Type_name = FaultsClass.objects.filter(id=type).values('name')
            Type = FaultsClass.objects.get(name=Type_name)

            # 获取项目名称
            project_name = FaultsProject.objects.filter(id=project).values('name')
            project = FaultsProject.objects.get(name=project_name)

            # 更新数据
            AddObj = FaultsContent.objects.filter(id=id).update(name=name,
                                                                level=level,
                                                                type=Type,
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
        fault_upform = FaultsValidForm()

'''故障删除'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultsDel(request):
    if request.method == 'POST':
        fault_delform = FaultsDelValidForm(request.POST)
        if fault_delform.is_valid():
            id = fault_delform.cleaned_data['id']
            DelObj = FaultsContent.objects.filter(id=id).delete()
            # 数据删除状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据删除状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        idc_delform = FaultsDelValidForm()

'''故障编辑'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultsProfile(request):
    if request.method == 'GET':
        id = request.GET['id']
        result = FaultsContent.objects.filter(id=id)
    return render(request, 'faults/profile.html', {'result': result})

'''故障详情'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FaultsDetails(request):
    if request.method == 'GET':
        id = request.GET['id']
    result = FaultsContent.objects.filter(id=id)
    return render(request, 'faults/details.html', {'result': result})

'''故障级别列表'''
def SeletedLevel(request):
    if request.method == 'GET':
        result = FaultsContent.fault_level_choices
        return HttpResponse(json.dumps(list(result)))

'''项目类型列表'''
def SeletedClass(request):
    if request.method == 'GET':
        result = FaultsClass.objects.all().values('id', 'name')
        return HttpResponse(json.dumps(list(result)))

'''项目名称列表'''
def SeletedProject(request):
    if request.method == 'GET':
        result = FaultsProject.objects.all().values('id', 'name')
        return HttpResponse(json.dumps(list(result)))

'''故障状态列表'''
def SeletedStatus(request):
    if request.method == 'GET':
        result = FaultsContent.fault_status_choices
        return HttpResponse(json.dumps(list(result)))

'''主导改进列表'''
def SeletedImprove(request):
    if request.method == 'GET':
        result = FaultsContent.fault_improve_choices
        return HttpResponse(json.dumps(list(result)))