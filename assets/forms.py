# -*- coding: UTF-8 -*-

from django import forms
from assets.models import *

class IDCValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=128, required=False)
    address = forms.CharField(max_length=128, required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        if HostIDC.objects.filter(name=name).exists():
            raise forms.ValidationError('机房名称已存在，请重新输入.')
        return name

class CabinetValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=128, required=False)
    cabinet = forms.CharField(max_length=128, required=False)

    def clean_cabinet(self):
        cabinet = self.cleaned_data.get('cabinet')
        if HostCabinet.objects.filter(name=cabinet).exists():
            raise forms.ValidationError('机柜名称已存在，请重新输入.')
        return cabinet

class CabinetDelValidForm(forms.Form):
    id = forms.IntegerField(required=False)

    def clean_id(self):
        id = self.cleaned_data['id']
        if HostCabinet.objects.filter(id=id).exists():
            status = HostCabinet.objects.filter(id=id).values('status')
            if status[0]['status']:
                raise forms.ValidationError('已使用的机柜禁止删除，请下架服务器后再尝试删除.')
            else:
                return id
        else:
            raise forms.ValidationError('机柜编号不存在，请选择正确的机柜编号.')

class GroupValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=128, required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        if HostGroup.objects.filter(name=name).exists():
            raise forms.ValidationError('主机组名称已存在，请重新输入.')
        return name

class GroupDelValidForm(forms.Form):
    id = forms.IntegerField(required=False)

    def clean_id(self):
        id = self.cleaned_data['id']
        if HostGroup.objects.filter(id=id).exists():
            # 统计主机组的主机数量
            Group = HostGroup.objects.filter(id=id).values('name')
            name = HostGroup.objects.get(name=Group)
            Count = Server.objects.filter(group__name=name).count()

        if Count == 0:
            return id
        else:
            raise forms.ValidationError('主机组内可能存在主机，禁止删除.')

class ManufactoryValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    manufactory = forms.CharField(required=False)
    support_num = forms.CharField(required=False)

    def clean_manufactory(self):
        manufactory = self.cleaned_data['manufactory']
        if Manufactory.objects.filter(manufactory=manufactory).exists():
            # 检查厂商名称是否存在
            manufactory_name = Manufactory.objects.filter(manufactory=manufactory).values('manufactory')
            manufactory_name = Manufactory.objects.get(manufactory=manufactory_name)
            if manufactory != manufactory_name:
                return manufactory
            else:
                raise forms.ValidationError('厂商名称已存在，请重新输入.')
        return manufactory

class HostsValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    sn = forms.CharField(max_length=128, required=False)
    hostname = forms.CharField(max_length=128, required=False)
    ip_address = forms.CharField(max_length=128, required=False)
    nip_address = forms.CharField(max_length=128, required=False)
    idc = forms.IntegerField(required=False)
    cabinet = forms.IntegerField(required=False)
    group = forms.IntegerField(required=False)
    manufactory = forms.IntegerField(required=False)
    server_model = forms.CharField(max_length=128, required=False)
    system_distribution = forms.CharField(max_length=128, required=False)
    system_type = forms.CharField(max_length=128, required=False)
    system_release = forms.CharField(max_length=128, required=False)
    kernel_release = forms.CharField(max_length=128, required=False)
    manager = forms.IntegerField(required=False)
    admin = forms.IntegerField(required=False)

    def clean_hostname(self):
        hostname = self.cleaned_data['hostname']
        print hostname
        if Server.objects.filter(hostname=hostname).exists():
            raise forms.ValidationError('主机名称已存在，请重新输入.')
        return hostname

    def clean_ip_address(self):
        ip_address = self.cleaned_data['ip_address']
        if Server.objects.filter(ip_address=ip_address).exists():
            raise forms.ValidationError('外网地址已存在，请重新输入.')
        return ip_address

    def clean_nip_address(self):
        nip_address = self.cleaned_data['nip_address']
        if Server.objects.filter(nip_address=nip_address).exists():
            raise forms.ValidationError('私网地址已存在，请重新输入.')
        return nip_address

class HostsUpValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    sn = forms.CharField(max_length=128, required=False)
    hostname = forms.CharField(max_length=128, required=False)
    ip_address = forms.CharField(max_length=128, required=False)
    nip_address = forms.CharField(max_length=128, required=False)
    idc = forms.IntegerField(required=False)
    cabinet = forms.IntegerField(required=False)
    group = forms.IntegerField(required=False)
    manufactory = forms.IntegerField(required=False)
    server_model = forms.CharField(max_length=128, required=False)
    system_distribution = forms.CharField(max_length=128, required=False)
    system_type = forms.CharField(max_length=128, required=False)
    system_release = forms.CharField(max_length=128, required=False)
    kernel_release = forms.CharField(max_length=128, required=False)
    manager = forms.IntegerField(required=False)
    admin = forms.IntegerField(required=False)

class HostnameValidForm(forms.Form):
    hostname = forms.CharField(max_length=128, required=False)
    # 主机名称初始化值
    str_hostname = forms.CharField(max_length=128, required=False)
    def clean(self):
        hostname = self.cleaned_data['hostname']
        str_hostname = self.cleaned_data['str_hostname']

        if Server.objects.filter(hostname=hostname).exists():
            if hostname == str_hostname:
                return hostname
            else:
                raise forms.ValidationError('主机名称已存在，请重新输入.')
        return hostname

class PrevateUpValidForm(forms.Form):
    nip_address = forms.CharField(max_length=128, required=False)
    # 外网地址初始化值
    str_nip_address = forms.CharField(max_length=128, required=False)

    def clean(self):
        nip_address = self.cleaned_data['nip_address']
        str_nip_address = self.cleaned_data['str_nip_address']

        if Server.objects.filter(nip_address=nip_address).exists():
            if nip_address == str_nip_address:
                return nip_address
            else:
                raise forms.ValidationError('私网地址已存在，请重新输入.')
        return nip_address

class PublicUpValidForm(forms.Form):
    ip_address = forms.CharField(max_length=128, required=False)
    # 外网地址初始化值
    str_ip_address = forms.CharField(max_length=128, required=False)

    def clean(self):
        ip_address = self.cleaned_data['ip_address']
        str_ip_address = self.cleaned_data['str_ip_address']

        if Server.objects.filter(ip_address=ip_address).exists():
            if ip_address == str_ip_address:
                return ip_address
            else:
                raise forms.ValidationError('公网地址已存在，请重新输入.')
        return ip_address