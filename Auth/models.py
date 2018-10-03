# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.
class CustomUsers(AbstractUser):
    phone = models.CharField(u'手机号', max_length=11, blank=False, null=False, unique=True)
    nickname = models.CharField(u'中文名', max_length=64, blank=False, null=False)
    department = models.CharField(u'部门', max_length=64, blank=False, null=False)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'CustomUsers'
        verbose_name = u'用户'
        verbose_name_plural = u"用户"