# -*- coding: utf-8 -*-

from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractUser
from Auth.models import *


class HostGroup(models.Model):
	name = models.CharField(u'主机组', max_length=128, blank=False, null=False, unique=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = 'hosts_groups'

class HostIDC(models.Model):
	name = models.CharField(u'机房', max_length=128, blank=False, null=False, unique=True)
	address = models.CharField(u'地址', max_length=128, blank=True, null=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = 'hosts_idc'

class HostCabinet(models.Model):
	name = models.CharField(u'机柜', max_length=128, blank=False, null=False, unique=True)
	status = models.BooleanField(u'机柜状态', default=0)
	idc = models.ForeignKey('HostIDC', verbose_name=u'机房地址')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = 'hosts_cabinet'

class Manufactory(models.Model):
	manufactory = models.CharField(u'厂商名称',max_length=64, unique=True)
	support_num = models.CharField(u'支持电话',max_length=30,blank=True)

	def __unicode__(self):
		return self.manufactory

	class Meta:
		db_table = u'hosts_manufactory'

class Server(models.Model):
	sn = models.CharField(u'SN号', max_length=128, null=True, blank=True)
	hostname = models.CharField(u'主机名称', max_length=128, blank=False, null=False, unique=True)
	ip_address = models.GenericIPAddressField(u'公网地址', max_length=45, null=True, blank=True, unique=True)
	nip_address = models.GenericIPAddressField(u'内网地址', max_length=45, null=False, blank=False, unique=True)
	group = models.ManyToManyField(u'HostGroup', verbose_name=u'主机组')
	idc = models.ForeignKey(u'HostIDC', verbose_name=u'机房地址')
	cabinet = models.ForeignKey(u'HostCabinet', verbose_name=u'机柜地址')
	manufactory = models.ForeignKey(u'Manufactory', verbose_name=u'制造商', null=True, blank=True)
	server_model = models.CharField(u'服务器型号', max_length=128, null=True, blank=True)
	system_distribution = models.CharField(u'发行版本', max_length=64, blank=True, null=True)
	system_type = models.CharField(u'系统类型', max_length=64, blank=True, null=True)
	system_release = models.CharField(u'系统版本', max_length=64, blank=True, null=True)
	kernel_release = models.CharField(u'内核版本', max_length=64, blank=True, null=True)
	create_datetime = models.DateTimeField(u'创建时间', auto_now=True)
	update_datetime = models.DateTimeField(u'更新时间', auto_now_add=True)
	trade_datetime  = models.DateTimeField(u'购买时间', null=True, blank=True)
	expire_datetime = models.DateTimeField(u'过保修期', null=True, blank=True)
 
	
	def __unicode__(self):
		return self.hostname
	
	class Meta:
		db_table = u'hosts_servers'

class CPU(models.Model):
	hostname = models.ForeignKey(u'Server', null=True, blank=True)
	cpu_model = models.CharField(u'CPU型号', max_length=128, blank=True)
	cpu_count = models.SmallIntegerField(u'物理CPU个数')
	cpu_core_count = models.SmallIntegerField(u'逻辑CPU核数')
	create_datetime = models.DateTimeField(u'创建时间', blank=True, auto_now_add=True)
	update_datetime = models.DateTimeField(u'修改时间', blank=True, auto_now=True)
	memo = models.TextField(u'备注', null=True, blank=True)

	class Meta:
		db_table = u'hosts_cpu'

class Disk(models.Model):
	sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
	hostname = models.ForeignKey(u'Server', null=True, blank=True)
	slot = models.CharField(u'插槽位', max_length=64)
	manufactory = models.CharField(u'制造商', max_length=64, blank=True, null=True)
	model = models.CharField(u'磁盘型号', max_length=128, blank=True, null=True)
	capacity = models.FloatField(u'磁盘容量GB')
	disk_iface_choice = (
		('SATA', 'SATA'),
		('SAS', 'SAS'),
		('SCSI', 'SCSI'),
		('SSD', 'SSD'),
	)
	iface_type = models.CharField(u'接口类型', max_length=64, choices=disk_iface_choice, default='SAS')
	create_date = models.DateTimeField(blank=True, auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)
	memo = models.TextField(u'备注', blank=True, null=True)

class NIC(models.Model):
	name = models.CharField(u'网卡名', max_length=64, blank=True, null=True)
	sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
	hostname = models.ForeignKey(u'Server', null=True, blank=True)
	model = models.CharField(u'网卡型号', max_length=128, blank=True, null=True)
	macaddress = models.CharField(u'MAC', max_length=64, unique=True)
	ipaddress = models.GenericIPAddressField(u'IP', blank=True, null=True)
	netmask = models.CharField(max_length=64, blank=True, null=True)
	bonding = models.CharField(max_length=64, blank=True, null=True)
	memo = models.CharField(u'备注', max_length=128, blank=True, null=True)
	create_date = models.DateTimeField(blank=True, auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		db_table = u'hosts_network'

class RAM(models.Model):
	sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
	hostname = models.ForeignKey(u'Server', null=True, blank=True)
	model = models.CharField(u'内存型号', max_length=128)
	slot = models.CharField(u'插槽', max_length=64)
	capacity = models.IntegerField(u'内存大小(MB)')
	memo = models.CharField(u'备注', max_length=128, blank=True, null=True)
	create_date = models.DateTimeField(blank=True, auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		db_table = u'hosts_memory'