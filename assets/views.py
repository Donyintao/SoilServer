# -*- coding: utf-8 -*-

import sys
import json
from forms import *
from models import *
from Users.models import CustomUser
import django.utils.timezone as timezone
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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

'''机房列表'''
@csrf_exempt
@login_required(login_url="/users/login/")
def IDC_List(request):
    # 查询列表
    List = HostIDC.objects.all().values('id', 'name', 'address')
    # 返回结果
    result = []
    for idc in List:
        # 统计每个机房的机柜数量
        Amount = HostCabinet.objects.filter(idc__name=idc['name']).count()
        idc.update({'count': Amount})
        result.append(idc)
    return render(request, 'assets/idc_list.html', {'result': result})

'''机房添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def IDC_Add(request):
    if request.method == 'POST':
        idc_form = IDCValidForm(request.POST)
        if idc_form.is_valid():
            name = idc_form.cleaned_data['name']
            address = idc_form.cleaned_data['address']
            # 添加机房
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
@login_required(login_url="/users/login/")
def IDC_Del(request):
    if request.method == 'POST':
        idc_delform = IDCValidForm(request.POST)
        if idc_delform.is_valid():
            id = idc_delform.cleaned_data['id']
            # 删除机房
            DelObj = HostIDC.objects.filter(id=id).delete()
            # 数据删除状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据删除状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        idc_delform = IDCValidForm()

'''机房编辑'''
@csrf_exempt
@login_required(login_url="/users/login/")
def IDC_Profile(request):
    if request.method == 'GET':
        id = request.GET['id']
        result = HostIDC.objects.filter(id=id)
    return render(request, 'assets/idc_profile.html', {'result': result})

'''机房更新操作'''
@csrf_exempt
@login_required(login_url="/users/login/")
def IDC_Update(request):
    if request.method == 'POST':
        idc_upform = IDCValidForm(request.POST)
        if idc_upform.is_valid():
            id = idc_upform.cleaned_data['id']
            address = idc_upform.cleaned_data['address']
            # 更新机房
            UpdateObj = HostIDC.objects.filter(id=id).update(address=address)
            # 数据更新状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据更新状态：false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        idc_upform = IDCValidForm()


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

'''机柜查询'''
@csrf_exempt
@login_required(login_url="/users/login/")
def Cabinet(request):
    # 机房信息
    IDC_List = HostIDC.objects.all().values('id', 'name', 'address')
    # 机柜信息
    CabinetList = HostCabinet.objects.all().values('id', 'name', 'status', 'idc__name')
    return render(request, 'assets/cabinet_list.html', {'IDC': IDC_List, 'Cabinet': CabinetList})

'''机柜添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def CabinetAdd(request):
    if request.method == 'POST':
        cabinet_form = CabinetValidForm(request.POST)
        if cabinet_form.is_valid():
            name = cabinet_form.cleaned_data['name']
            cabinet = cabinet_form.cleaned_data['cabinet']
            # 获取机房名称
            idc = HostIDC.objects.get(name=name)
            # 添加机柜信息
            AddObj = HostCabinet(name=cabinet, idc=idc)
            AddObj.save()
            # 数据添加状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据添加状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        cabinet_form = CabinetValidForm()

'''机柜编辑'''
@csrf_exempt
@login_required(login_url="/users/login/")
def CabinetProfile(request):
    if request.method == 'GET':
        id = request.GET['id']
        result = HostCabinet.objects.filter(id=id).values('id', 'name', 'idc__name')
    return render(request, 'assets/cabinet_profile.html', {'result': result})

'''机柜更新'''
@csrf_exempt
@login_required(login_url="/users/login/")
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
@login_required(login_url="/users/login/")
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

'''主机组校验'''
@csrf_exempt
@login_required(login_url="/users/login/")
def GroupValid(request):
    if request.method == 'POST':
        group_validform = GroupValidForm(request.POST)
        if group_validform.is_valid():
            return HttpResponse(json.dumps({'valid': 'true'}))
        else:
            return HttpResponse(json.dumps({'valid': 'false'}))
    else:
        group_validform = GroupValidForm()

'''主机组查询'''
@csrf_exempt
@login_required(login_url="/users/login/")
def Group(request):
    # 查看主机组
    GroupList = HostGroup.objects.all().values('id', 'name')
    result = []
    for Group in GroupList:
        amount = Server.objects.filter(group__name=Group['name']).count()
        Group.update({'count': amount})
        result.append(Group)

    return render(request, 'assets/group_list.html', {'result': result})

'''主机组添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
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
@csrf_exempt
@login_required(login_url="/users/login/")
def GroupProfile(request):
    if request.method == 'GET':
        id = request.GET['id']
        result = HostGroup.objects.filter(id=id).values('id', 'name')
    return render(request, 'assets/group_profile.html', {'result': result})

'''主机组更新操作'''
@csrf_exempt
@login_required(login_url="/users/login/")
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
@login_required(login_url="/users/login/")
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

'''厂商列表'''
@csrf_exempt
@login_required(login_url="/users/login/")
def Firm(request):
    if request.method == 'GET':
        result = Manufactory.objects.all()
    return render(request, 'assets/firm_list.html', {'result': result})

'''厂商添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FirmAdd(request):
    if request.method == 'POST':
        firm_form = ManufactoryValidForm(request.POST)
        if firm_form.is_valid():
            manufactory = firm_form.cleaned_data['manufactory']
            support_num = firm_form.cleaned_data['support_num']
            # 添加厂商
            AddObj = Manufactory(manufactory=manufactory, support_num=support_num)
            AddObj.save()
            # 数据添加状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据添加状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        firm_form = ManufactoryValidForm()


'''厂商编辑'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FirmProfile(request):
    if request.method == 'GET':
        id = request.GET['id']
        result = Manufactory.objects.filter(id=id).values('id', 'manufactory', 'support_num')
    return render(request, 'assets/firm_profile.html', {'result': result})

'''厂商更新'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FirmUpdate(request):
    if request.method == 'POST':
        firm_upform = ManufactoryValidForm(request.POST)
        if firm_upform.is_valid():
            id = firm_upform.cleaned_data['id']
            manufactory = firm_upform.cleaned_data['manufactory']
            support_num = firm_upform.cleaned_data['support_num']
            UpdateObj = Manufactory.objects.filter(id=id).update(manufactory=manufactory, support_num=support_num)
            # 数据更新状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据更新状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        group_upform = ManufactoryValidForm(request.POST)

'''厂商删除'''
@csrf_exempt
@login_required(login_url="/users/login/")
def FirmDel(request):
    if request.method == 'POST':
        firm_delform = ManufactoryValidForm(request.POST)
        if firm_delform.is_valid():
            id = firm_delform.cleaned_data['id']
            DelObj = Manufactory.objects.filter(id=id).delete()
            # 数据删除状态: true表示正常.
            return HttpResponse(json.dumps({'status': 'true'}))
        else:
            # 数据删除状态: false表示异常.
            return HttpResponse(json.dumps({'status': 'false'}))
    else:
        group_delform = GroupDelValidForm()

'''主机添加校验'''
@csrf_exempt
def HostsValid(request):
    if request.method == 'POST':
        hosts_form = HostsValidForm(request.POST)
        if hosts_form.is_valid():
            return HttpResponse(json.dumps({'valid': 'true'}))
        else:
            return HttpResponse(json.dumps({'valid': 'false'}))
    else:
        hosts_validform = HostsValidForm()

'''主机更新校验'''
@csrf_exempt
def HostsUpValid(request):
    if request.method == 'POST':
        # 主机名称校验
        hosts_upform = HostnameValidForm(request.POST)
        # 私网地址校验
        hosts_nipform = PrevateUpValidForm(request.POST)
        # 公网地址校验
        hosts_ipform = PublicUpValidForm(request.POST)

        if hosts_upform.is_valid() and hosts_nipform.is_valid() and hosts_ipform.is_valid():
            return HttpResponse(json.dumps({'valid': 'true'}))
        else:
            return HttpResponse(json.dumps({'valid': 'false'}))
    else:
        hosts_validform = HostsValidForm()


'''主机查询'''
@csrf_exempt
@login_required(login_url="/users/login/")
def Hosts(request):
    if request.method == 'GET':
        result = Server.objects.all().values('id',
                                             'hostname',
                                             'nip_address',
                                             'system_type',
                                             'system_release',
                                             'group__name',
                                             'idc__name',
                                             'cabinet__name',
                                             'create_datetime',
                                             'update_datetime',
                                             'admin__username',
                                             'manager__username')
    return render(request, 'assets/hosts_list.html', {'result': result})

'''主机添加'''
@csrf_exempt
@login_required(login_url="/users/login/")
def HostsAdd(request):
    if request.method == 'GET':
        return render(request, 'assets/hosts_add.html')
    elif request.method == 'POST':
        hosts_form = HostsValidForm(request.POST)
        print hosts_form
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
            manufactory = hosts_form.cleaned_data['manufactory']
            manager = hosts_form.cleaned_data['manager']
            admin = hosts_form.cleaned_data['admin']

            # 获取主机组名称
            name = HostGroup.objects.filter(id=group).values('name')[0]['name']
            group_name = HostGroup.objects.get(name=name)

            # 获取机柜名称
            name = HostCabinet.objects.filter(idc=idc, id=cabinet).values('name')[0]['name']
            cabinet_name = HostCabinet.objects.get(name=name)

            # 获取机房名称
            name = HostIDC.objects.filter(id=idc).values('name')[0]['name']
            idc_name = HostIDC.objects.get(name=name)

            # 获取服务厂商
            host_manufactory = Manufactory.objects.filter(id=manufactory).values('manufactory')[0]['manufactory']
            manufactory_name = Manufactory.objects.get(manufactory=host_manufactory)

            # 开发负责人
            username = CustomUser.objects.filter(id=manager).values('username')[0]['username']
            manager_name = CustomUser.objects.get(username=username)

            # 运维负责人
            username = CustomUser.objects.filter(id=admin).values('username')[0]['username']
            admin_name = CustomUser.objects.get(username=username)

            # 更新机柜状态
            CabinetObj = HostCabinet.objects.filter(id=cabinet).update(status=1)

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
                               manufactory=manufactory_name,
                               manager=manager_name,
                               admin=admin_name)
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

'''主机详情信息'''
@csrf_exempt
@login_required(login_url="/users/login/")
def HostsDetails(request):
    if request.method == 'GET':
        id = request.GET['id']
        # 获取主机基础信息
        result = Server.objects.filter(id=id).values('id',
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
                                                     'update_datetime',
                                                     'manager__nickname',
                                                     'admin__nickname',
                                                     'cpu__cpu_model',
                                                     'cpu__cpu_count',
                                                     'cpu__cpu_core_count',
                                                     'cpu__create_datetime',
                                                     'cpu__update_datetime',
                                                     'nic__name',
                                                     'nic__ipaddress',
                                                     'nic__macaddress',
                                                     'nic__netmask',
                                                     'nic__create_datetime',
                                                     'nic__update_datetime')
    return render(request, 'assets/hosts_details.html', {'result': result})

'''主机编辑'''
@csrf_exempt
@login_required(login_url="/users/login/")
def HostsProfile(request):
    if request.method == 'GET':
        id = request.GET['id']
        result = Server.objects.filter(id=id).values('id',
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
                                                     'update_datetime',
                                                     'manager__nickname',
                                                     'admin__nickname')
        return render(request, 'assets/hosts_profile.html', {'result': result})

'''主机更新'''
@csrf_exempt
@login_required(login_url="/users/login/")
def HostsUpdate(request):
    if request.method == 'POST':
        hosts_upform = HostsUpValidForm(request.POST)
        if hosts_upform.is_valid():
            id = hosts_upform.cleaned_data['id']
            sn = hosts_upform.cleaned_data['sn']
            server_model = hosts_upform.cleaned_data['server_model']
            hostname = hosts_upform.cleaned_data['hostname']
            ip_address = hosts_upform.cleaned_data['ip_address']
            nip_address = hosts_upform.cleaned_data['nip_address']
            system_type = hosts_upform.cleaned_data['system_type']
            system_distribution = hosts_upform.cleaned_data['system_distribution']
            system_release = hosts_upform.cleaned_data['system_release']
            kernel_release = hosts_upform.cleaned_data['kernel_release']
            group = hosts_upform.cleaned_data['group']
            idc = hosts_upform.cleaned_data['idc']
            cabinet = hosts_upform.cleaned_data['cabinet']
            manufactory = hosts_upform.cleaned_data['manufactory']
            manager = hosts_upform.cleaned_data['manager']
            admin = hosts_upform.cleaned_data['admin']

            # 获取新主机组名称
            name = HostGroup.objects.filter(id=group).values('name')[0]['name']
            group_name = HostGroup.objects.get(name=name)

            # 获取原机柜和原主机组
            hosts = Server.objects.filter(id=id).values('cabinet__name', 'group__name')

            # 原主机组名称
            name = hosts[0]['group__name']
            OldGroup = HostGroup.objects.get(name=name)

            # 更新原机柜状态. 标注: 未使用
            name = hosts[0]['cabinet__name']
            OldCabinet = HostCabinet.objects.filter(name=name).update(status=0)

            # 更新机柜信息
            NewCabinet = HostCabinet.objects.filter(id=cabinet).update(status=1)

            # 更新主机信息
            UpdateObj = Server.objects.filter(id=id).update(sn=sn,
                                                            server_model=server_model,
                                                            hostname=hostname,
                                                            ip_address=ip_address,
                                                            nip_address=nip_address,
                                                            system_type=system_type,
                                                            system_distribution=system_distribution,
                                                            system_release=system_release,
                                                            kernel_release=kernel_release,
                                                            idc=idc,
                                                            cabinet=cabinet,
                                                            manufactory=manufactory,
                                                            manager=manager,
                                                            admin=admin,
                                                            update_datetime=timezone.now())

            ServerObj = Server.objects.filter(id=id).first()
            # 移除原主机组信息
            ServerObj.group.remove(OldGroup)
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
@login_required(login_url="/users/login/")
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
        result = HostCabinet.objects.filter(idc=id,status=0).values('id', 'name')
        return HttpResponse(json.dumps(list(result)))

def SeletedGroup(request):
    if request.method == 'GET':
        result = HostGroup.objects.all().values('id','name')
        return HttpResponse(json.dumps(list(result)))

def SeletedFirm(request):
    if request.method == 'GET':
        result = Manufactory.objects.all().values('id', 'manufactory')
        return HttpResponse(json.dumps(list(result)))

def SeletedHosts(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        result = Server.objects.filter(host_group=id).values('id', 'hostname')
        return HttpResponse(json.dumps(list(result)))

def SeletedUsers(request):
    if request.method == 'GET':
        result = CustomUser.objects.all().values('id', 'username', 'nickname')
        return HttpResponse(json.dumps(list(result)))