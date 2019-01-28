# -*- coding: UTF-8 -*-

from django import forms

class BindValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    zone = forms.IntegerField(required=False)
    print zone
    host = forms.CharField(max_length=128, required=False)
    type = forms.CharField(max_length=128, required=False)
    data = forms.CharField(max_length=128, required=False)