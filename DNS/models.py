# -*- coding: utf-8 -*-

from django.db import models
import django.utils.timezone as timezone

class DNS(models.Model):
	dns_type_choice = (
		('A', 'A- 将域名指向一个IPV4地址'),
		('CNAME', 'CNAME- 将域名指向另外一个域名'),
		('AAAA', 'AAAA- 将域名指向一个IPV6地址'),
	)
	zone = models.CharField(u'域名', max_length=128, blank=False, null=False)
	host = models.CharField(u'记录名称', max_length=128, blank=False, null=False)
	type = models.CharField(u'记录类型', max_length=128, choices=dns_type_choice, default='A')
	data = models.CharField(u'记录值', max_length=128, blank=False, null=False)
	ttl = models.IntegerField(u'TTL时间', blank=False,null=False)
	mx_priority = models.IntegerField(u'MX优先级', blank=True, null=True)
	refresh = models.IntegerField(u'刷新时间间隔', blank=True, null=True)
	retry = models.IntegerField(u'重试时间间隔', blank=True, null=True)
	expire = models.IntegerField(u'过期时间', blank=True, null=True)
	minimum = models.IntegerField(u'最小时间', blank=True, null=True)
	serial = models.IntegerField(u'序列号', blank=True, null=True)
	resp_person = models.CharField(u'责任人', max_length=128, blank=True, null=True)
	status = models.BooleanField(u'记录状态', default=1)
	create_datetime = models.DateTimeField(u'创建时间', default=timezone.now)
	update_datetime = models.DateTimeField(u'更新时间', auto_now=True)

	class Meta:
		db_table = 'dns_records'