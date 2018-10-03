# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group
from Auth.models import CustomUsers

# Create your models here.
class FaultType(models.Model):
	name = models.CharField(max_length=255, verbose_name=u"故障类型")

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = u'fault_type'

class FaultContent(models.Model):
	fault_level_choices = (
		(0, u"P0"),
		(1, u"P1"),
		(2, u"P2"),
		(3, u"P3"),
		(4, u"P4"),
	)

	fault_status_choices = (
		(0, u"处理中"),
		(1, u"改进中"),
		(2, u"已恢复"),
		(3, u"已完结"),
	)

	fault_improve_choices = (
		(0, u"开发"),
		(1, u"运维"),
		(2, u"机房"),
		(3, u"网络"),
		(4, u"其他"),
	)

	fault_project_choices = (
		(0, u"商城系统"),
		(1, u"物流系统"),
		(2, u"配送系统"),
	)

	name = models.CharField(u'故障名称', max_length=255, blank=False, null=False, unique=True)
	level = models.IntegerField(u'故障级别', choices=fault_level_choices)
	type = models.ForeignKey(u'FaultType', verbose_name=u'故障类型')
	effect = models.TextField(u'故障影响', blank=True, null=True)
	reasons = models.TextField(u'故障原因', blank=True, null=True)
	solution = models.TextField(u'解决方案', blank=True, null=True)
	content = models.TextField(u'处理流程', blank=True, null=True)
	project = models.IntegerField(u'影响项目', choices=fault_project_choices)
	status = models.IntegerField(u'故障状态', choices=fault_status_choices)
	improve = models.IntegerField(u'主导改进', choices=fault_improve_choices)
	lesson = models.TextField(blank=True, verbose_name=u'经验总结')
	start_time = models.DateTimeField(u'开始时间')
	end_time = models.DateTimeField(u'结束时间')
	create_datetime = models.DateTimeField(u'创建时间', auto_now=True)
	update_datetime = models.DateTimeField(u'更新时间', auto_now_add=True)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = u'fault_content'