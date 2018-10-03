# -*- coding: utf-8 -*-

import sys
import json
from models import *
from API.forms import *
import django.utils.timezone as timezone
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

'''机房列表'''
def IDC_List(request):
	IDC_List = HostIDC.objects.all().values('id', 'name', 'address')
	NewList = []
	for IDC in IDC_List:
		amount = HostCabinet.objects.filter(cabinet_idc__name=IDC['name']).count()
		IDC.update({'count': amount})
		NewList.append(IDC)

	return render(request, 'cmdb/idc_list.html', {'IDC': NewList})

'''机房编辑'''
def IDC_Profile(request):
	if request.method == 'GET':
		id = request.GET['id']
		IDC_List = HostIDC.objects.filter(id=id)
	return render(request, 'cmdb/idc_profile.html', {'IDC': IDC_List})

'''机房添加'''
@csrf_exempt
def IDC_Add(request):
	if request.method == 'POST':
		idc_form = IDCValidForm(request.POST)
		if idc_form.is_valid():
			name = idc_form.cleaned_data['name']
			address = idc_form.cleaned_data['address']
			AddObj = HostIDC(name=name,address=address)
			AddObj.save()
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		idc_form = IDCValidForm()

'''机房删除'''
@csrf_exempt
def IDC_Del(request):
    if request.method == 'POST':
        idc_delform = IDCValidForm(request.POST)
        if idc_delform.is_valid():
            id = idc_delform.cleaned_data['id']
            DelObj = HostIDC.objects.filter(id=id).delete()
            # 数据删除状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据删除状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        idc_delform = IDCValidForm()

'''机房更新操作'''
@csrf_exempt
def IDC_Update(request):
    if request.method == 'POST':
        idc_upform = IDCValidForm(request.POST)
        if idc_upform.is_valid():
            id = idc_upform.cleaned_data['id']
            address = idc_upform.cleaned_data['address']
            UpdateObj = HostIDC.objects.filter(id=id).update(address=address)
            # 数据更新状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据更新状态：false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        idc_upform = IDCValidForm()

'''机柜查询'''
def Cabinet(request):
    # 机房信息
    IDC_List = HostIDC.objects.all().values('id','name', 'address')
    # 机柜信息
    CabinetList = HostCabinet.objects.all().values('id', 'name', 'status', 'cabinet_idc__name')
    return render(request, 'cmdb/cabinet_list.html', {'IDC': IDC_List, 'Cabinet': CabinetList})

'''机柜编辑'''
def CabinetProfile(request):
	if request.method == 'GET':
		id = request.GET['id']
		CabinetList = HostCabinet.objects.filter(id=id).values('id', 'name', 'cabinet_idc__name')
	return render(request, 'cmdb/cabinet_profile.html', {'Cabinet': CabinetList})

'''机柜添加'''
@csrf_exempt
def CabinetAdd(request):
	if request.method == 'POST':
		cabinet_form = CabinetValidForm(request.POST)
		if cabinet_form.is_valid():
			name = cabinet_form.cleaned_data['name']
			cabinet = cabinet_form.cleaned_data['cabinet']
			# 获取机房名称
			name = HostIDC.objects.get(name=name)
			# 添加机柜信息
			AddObj = HostCabinet(name=cabinet, cabinet_idc=name)
			AddObj.save()
			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		cabinet_form = CabinetValidForm()

'''机柜更新'''
@csrf_exempt
def CabinetUpdate(request):
	if request.method == 'POST':
		cabinet_upform = CabinetValidForm(request.POST)
		if cabinet_upform.is_valid():
			id = cabinet_upform.cleaned_data['id']
			cabinet = cabinet_upform.cleaned_data['cabinet']
			# 更新机柜信息
			UpdateObj = HostCabinet.objects.filter(id=id).update(name=cabinet)
			# 数据更新状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据更新状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		cabinet_upform = CabinetValidForm()

'''机柜删除'''
@csrf_exempt
def CabinetDel(request):
	if request.method == 'POST':
		cabinet_delform = CabinetDelValidForm(request.POST)
		if cabinet_delform.is_valid():
			id = cabinet_delform.cleaned_data['id']
			DelObj = HostCabinet.objects.filter(id=id).delete()
			# 数据删除状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据删除状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		cabinet_delform = CabinetDelValidForm()

'''主机组查询'''
def HostsGroup(request):
	# 查看主机组
	GroupList = HostGroup.objects.all().values('id', 'name')
	NewList = []
	for Group in GroupList:
		amount = Server.objects.filter(group__name=Group['name']).count()
		Group.update({'count': amount})
		NewList.append(Group)
		
	return render(request, 'cmdb/group_list.html', {'Group': NewList})

'''主机组添加'''
@csrf_exempt
def GroupAdd(request):
    if request.method == 'POST':
        group_form = GroupValidForm(request.POST)
        if group_form.is_valid():
            name = group_form.cleaned_data['name']
            AddObj = HostGroup(name=name)
            AddObj.save()
            # 数据添加状态: true表示异常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据添加状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))

    else:
        group_form = GroupValidForm()

'''主机组编辑'''
def GroupProfile(request):
    if request.method == 'GET':
        id = request.GET['id']
        GroupList = HostGroup.objects.filter(id=id).values('id', 'name')
    return render(request,'cmdb/group_profile.html', {'Group': GroupList})

'''主机组更新操作'''
@csrf_exempt
def GroupUpdate(request):
	if request.method == 'POST':
		group_upform = GroupValidForm(request.POST)
		if group_upform.is_valid():
			id = group_upform.cleaned_data['id']
			name = group_upform.cleaned_data['name']
			UpdateObj = HostGroup.objects.filter(id=id).update(name=name)
			# 数据更新状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据更新状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		group_upform = GroupValidForm(request.POST)

'''主机组删除操作'''
@csrf_exempt
def GroupDel(request):
	if request.method == 'POST':
		group_delform = GroupDelValidForm(request.POST)
		if group_delform.is_valid():
			id = group_delform.cleaned_data['id']
			DelObj = HostGroup.objects.filter(id=id).delete()
			# 数据删除状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据删除状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		group_delform = GroupDelValidForm()
		
'''主机查询'''
def HostsList(request):
	HostList = Server.objects.all().values('id',
										   'sn',
										   'hostname',
										   'ip_address',
										   'nip_address',
										   'group__name',
										   'idc__name',
										   'cabinet__name',
										   'manufactory__manufactory',
										   'system_type',
										   'server_model',
										   'system_release',
										   'kernel_release',
										   'trade_datetime',
										   'expire_datetime',
										   'create_datetime',
										   'update_datetime')
	return render(request, 'cmdb/hosts_list.html', {'Hosts': HostList})


'''主机详情信息'''
def HostsDetails(request):
	if request.method == 'GET':
		id = request.GET['id']
		# 获取主机基础信息
		ServerObj = Server.objects.filter(id=id).values('id',
														'sn',
		                                                'hostname',
		                                                'ip_address',
		                                                'nip_address',
		                                                'group__name',
		                                                'idc__name',
		                                                'cabinet__name',
		                                                'manufactory__manufactory',
		                                                'system_type',
														'server_model',
														'system_release',
														'kernel_release',
		                                                'trade_datetime',
		                                                'expire_datetime',
														'create_datetime',
														'update_datetime')
		hostname = Server.objects.get(id=id)
		# 获取主机CPU信息
		CPUObj = CPU.objects.filter(hostname=hostname).values('id',
															  'cpu_model',
															  'cpu_count',
															  'cpu_core_count',
															  'create_datetime',
															  'update_datetime')
	return render(request, 'cmdb/hosts_details.html', { 'Server': ServerObj, 'CPU': CPUObj })

'''主机添加'''
@csrf_exempt
def AddHosts(request):
	if request.method == 'GET':
		GroupList = HostGroup.objects.all().values('name')
		return render(request, 'cmdb/hosts_add.html', {'Group': GroupList})
	elif request.method == 'POST':
		hosts_form = HostsValidForm(request.POST)
		if hosts_form.is_valid():
			sn = hosts_form.cleaned_data['sn']
			server_model = hosts_form.cleaned_data['server_model']
			hostname = hosts_form.cleaned_data['hostname']
			ip_address = hosts_form.cleaned_data['ip_address']
			nip_address = hosts_form.cleaned_data['nip_address']
			system_type = hosts_form.cleaned_data['system_type']
			system_distribution = hosts_form.cleaned_data['system_distribution']
			system_release = hosts_form.cleaned_data['system_release']
			kernel_release = hosts_form.cleaned_data['kernel_release']
			group = hosts_form.cleaned_data['group']
			idc = hosts_form.cleaned_data['idc']
			cabinet = hosts_form.cleaned_data['cabinet']

			# 获取主机组名称
			host_group = HostGroup.objects.filter(id=group).values('name')[0]['name']
			group_name = HostGroup.objects.get(name=host_group)

			# 获取机柜名称
			host_cabinet = HostCabinet.objects.filter(cabinet_idc=idc, id=cabinet).values('name')[0]['name']
			cabinet_name = HostCabinet.objects.get(name=host_cabinet)

			# 获取机房名称
			host_idc = HostIDC.objects.filter(id=idc).values('name')[0]['name']
			idc_name = HostIDC.objects.get(name=host_idc)

			# 获取制造厂商
			manufactory = Manufactory.objects.get(manufactory='Dell Inc.')

			CabinetObj = HostCabinet.objects.filter(name=cabinet_name).update(status=1)

			# 添加主机信息
			ServerObj = Server(sn=sn,
							   server_model=server_model,
							   hostname=hostname,
							   ip_address=ip_address,
							   nip_address=nip_address,
							   system_type=system_type,
							   system_distribution=system_distribution,
							   system_release=system_release,
							   kernel_release=kernel_release,
							   idc=idc_name,
							   cabinet=cabinet_name,
							   manufactory=manufactory)
			ServerObj.save()

			# 更新主机组信息
			ServerObj.group.add(group_name)
			ServerObj.save()

			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		hosts_form = HostsValidForm()

'''主机编辑'''
def HostsProfile(request):
	if request.method == 'GET':
		id = request.GET['id']
		ServerObj = Server.objects.filter(id=id).values('id',
														'sn',
														'hostname',
														'ip_address',
														'nip_address',
														'group__name',
														'idc__name',
														'cabinet__name',
														'manufactory__manufactory',
														'system_type',
														'server_model',
														'system_distribution',
														'system_release',
														'kernel_release',
														'trade_datetime',
														'expire_datetime',
														'create_datetime',
														'update_datetime')
		return render(request, 'cmdb/hosts_profile.html', {'Server': ServerObj})

'''主机更新'''
@csrf_exempt
def HostsUpdate(request):
	if request.method == 'POST':
		hosts_upform = HostsValidForm(request.POST)
		if hosts_upform.is_valid():
			id = hosts_upform.cleaned_data['id']
			sn = hosts_upform.cleaned_data['sn']
			server_model = hosts_upform.cleaned_data['server_model']
			ip_address = hosts_upform.cleaned_data['ip_address']
			nip_address = hosts_upform.cleaned_data['nip_address']
			system_type = hosts_upform.cleaned_data['system_type']
			system_distribution = hosts_upform.cleaned_data['system_distribution']
			system_release = hosts_upform.cleaned_data['system_release']
			kernel_release = hosts_upform.cleaned_data['kernel_release']
			group = hosts_upform.cleaned_data['group']
			idc = hosts_upform.cleaned_data['idc']
			cabinet = hosts_upform.cleaned_data['cabinet']

			# 获取新机柜名称
			host_cabinet = HostCabinet.objects.filter(cabinet_idc=idc, id=cabinet).values('name')[0]['name']
			cabinet_name = HostCabinet.objects.get(name=host_cabinet)
			# 获取新主机组名称
			host_group = HostGroup.objects.filter(id=group).values('name')[0]['name']
			group_name = HostGroup.objects.get(name=host_group)

			# 获取原机柜和原主机组
			hosts = Server.objects.filter(id=id).values('cabinet__name', 'group__name')
			old_group = hosts[0]['group__name']
			old_group = HostGroup.objects.get(name=old_group)

			# 更新原机柜状态. 标注: 未使用
			cabinet = hosts[0]['cabinet__name']
			CabinetObj = HostCabinet.objects.filter(name=cabinet).update(status=0)

			# 获取新主机组名称
			host_group = HostGroup.objects.filter(id=group).values('name')[0]['name']
			group_name = HostGroup.objects.get(name=host_group)

			# 获取机房名称
			host_idc = HostIDC.objects.filter(id=idc).values('name')[0]['name']
			idc_name = HostIDC.objects.get(name=host_idc)

			# 获取制造厂商
			manufactory = Manufactory.objects.get(manufactory='Dell Inc.')

            # 更新机柜信息
			NewCabinet = HostCabinet.objects.filter(name=cabinet_name).update(status=1)

			# 更新主机信息
			UpdateObj = Server.objects.filter(id=id).update(sn=sn,
															server_model=server_model,
															ip_address=ip_address,
															nip_address=nip_address,
															system_type=system_type,
															system_distribution=system_distribution,
															system_release=system_release,
															kernel_release=kernel_release,
															idc=idc_name,
															cabinet=cabinet_name,
															manufactory=manufactory,
															update_datetime=timezone.now())


			ServerObj = Server.objects.filter(id=id).first()
			# 移除原主机组信息
			ServerObj.group.remove(old_group)
			# 添加新主机组信息
			ServerObj.group.add(group_name)

			# 数据添加状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据添加状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		hosts_upform = HostsValidForm()


'''主机删除'''
@csrf_exempt
def HostsDel(request):
	if request.method == 'POST':
		hosts_delform = HostsValidForm(request.POST)
		if hosts_delform.is_valid():
			id = hosts_delform.cleaned_data['id']
			# 更新原机柜状态. 标注: 未使用
			cabinet = Server.objects.filter(id=id).values('cabinet__name')[0]['cabinet__name']
			CabinetObj = HostCabinet.objects.filter(name=cabinet).update(status=0)
			# 删除主机信息
			DelObj = Server.objects.filter(id=id).delete()
			# 数据删除状态: true表示正常.
			return HttpResponse(json.dumps({'status': 'true'}))
		else:
			# 数据删除状态: false表示异常.
			return HttpResponse(json.dumps({'status': 'false'}))
	else:
		hosts_delform = HostsValidForm()

def SeletedIDC(request):
	if request.method == 'GET':
		result = HostIDC.objects.all().values('id','name')
    	return HttpResponse(json.dumps(list(result)))

def SeletedCabinet(request):
	if request.method == 'GET':
		id = request.GET.get("id")
		result = HostCabinet.objects.filter(cabinet_idc=id,status=0).values('id','name')
		return HttpResponse(json.dumps(list(result)))

def SeletedGroup(request):
	if request.method == 'GET':
		result = HostGroup.objects.all().values('id','name')
		return HttpResponse(json.dumps(list(result)))

def SeletedHosts(request):
	if request.method == 'GET':
		id = request.GET.get('id')
		result = Server.objects.filter(host_group=id).values('id','hostname')
		return HttpResponse(json.dumps(list(result)))