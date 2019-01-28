# -*- coding: utf-8 -*-

from django.contrib import admin
from Users import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(CustomUserAdmin, self).__init__(*args, **kwargs)
        self.list_display = ('username', 'nickname', 'email', 'is_active', 'is_staff', 'is_superuser',
                             'phone','department')
        self.search_fields = ('username', 'email', 'nickname')

    def changelist_view(self, request, extra_context=None):
        if not request.user.is_superuser:
            self.fieldsets = ((None, {'fields': ('username', 'password',)}),
                              (_('Personal info'), {'fields': ('nickname', 'email', 'phone', 'department')}),
                              (_('Permissions'), {'fields': ('is_active', 'is_staff', 'groups')}),
                              (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                              )
            self.add_fieldsets = ((None, {'classes': ('wide',),
                                          'fields': ('username', 'nickname', 'password1', 'password2', 'email',
                                                     'phone', 'department', 'is_active', 'is_staff', 'groups'),
                                          }),
                                  )
        else:
            self.fieldsets = ((None, {'fields': ('username', 'password',)}),
                              (_('Personal info'), {'fields': ('nickname', 'email', 'phone', 'department')}),
                              (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
                              (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                              )
            self.add_fieldsets = ((None, {'classes': ('wide',),
                                          'fields': ('username', 'nickname', 'password1', 'password2', 'email',
                                                     'phone', 'department', 'is_active', 'is_staff', 'is_superuser',
                                                     'groups'),
                                          }),
                                  )
        return super(CustomUserAdmin, self).changelist_view(request, extra_context)

admin.site.register(models.CustomUser, CustomUserAdmin)
