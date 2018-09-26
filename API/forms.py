# -*- coding: UTF-8 -*-

import re
from DNS.models import *
from CMDB.models import *
from Fault.models import *
from django import forms
from django.forms import widgets, fields

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
			name  = HostGroup.objects.get(name=Group)
			Count = Server.objects.filter(group__name=name).count()
		
		if  Count == 0:
			return id
		else:
			raise forms.ValidationError('主机组内可能存在主机，禁止删除.')

class HostsValidForm(forms.Form):
	id = forms.IntegerField(required=False)
	sn = forms.CharField(max_length=128, required=False)
	hostname = forms.CharField(max_length=128, required=False)
	ip_address = forms.CharField(max_length=128, required=False)
	nip_address = forms.CharField(max_length=128, required=False)
	idc = forms.CharField(max_length=128, required=False)
	cabinet = forms.CharField(max_length=128, required=False)
	group = forms.CharField(max_length=128, required=False)
	manufactory = forms.CharField(max_length=128, required=False)
	server_model = forms.CharField(max_length=128, required=False)
	system_distribution = forms.CharField(max_length=128, required=False)
	system_type = forms.CharField(max_length=128, required=False)
	system_release = forms.CharField(max_length=128, required=False)
	kernel_release = forms.CharField(max_length=128, required=False)

	def clean_hostname(self):
		hostname = self.cleaned_data['hostname']
		if Server.objects.filter(hostname=hostname).exists():
			raise forms.ValidationError('主机名称已存在，请重新输入.')
		return hostname

	def clean_ip_address(self):
		ip_address = self.cleaned_data['ip_address']
		if Server.objects.filter(ip_address=ip_address).exists():
			raise forms.ValidationError('公网地址已存在，请重新输入.')
		return ip_address

	def clean_nip_address(self):
		nip_address = self.cleaned_data['nip_address']
		if Server.objects.filter(nip_address=nip_address).exists():
			raise forms.ValidationError('内网地址已存在，请重新输入.')
		return nip_address

class DNSValidForm(forms.Form):
	id = forms.IntegerField(required=False)
	zone = forms.CharField(max_length=128, required=False)
	host = forms.CharField(max_length=128, required=False)
	type = forms.CharField(max_length=128, required=False)
	data = forms.CharField(max_length=128, required=False)

class FaultTypeValidForm(forms.Form):
	id = forms.IntegerField(required=False)
	name = forms.CharField(max_length=128, required=False)

	def clean_name(self):
		name = self.cleaned_data['name']
		if FaultType.objects.filter(name=name).exists():
			raise forms.ValidationError('故障名称已存在，请重新输入.')
		return name