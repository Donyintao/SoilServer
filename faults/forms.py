# -*- coding: UTF-8 -*-

from models import *
from django import forms

class FaultsValidForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(required=False)
    level = forms.IntegerField(required=False)
    type = forms.CharField(required=False)
    effect = forms.CharField(widget=forms.Textarea, required=False)
    reasons = forms.CharField(widget=forms.Textarea, required=False)
    solution = forms.CharField(widget=forms.Textarea, required=False)
    content = forms.CharField(widget=forms.Textarea, required=False)
    lesson = forms.CharField(widget=forms.Textarea, required=False)
    project = forms.IntegerField(required=False)
    status = forms.IntegerField(required=False)
    improve = forms.IntegerField(required=False)
    start_time = forms.DateTimeField(required=False)
    end_time = forms.DateTimeField(required=False)


class FaultsDelValidForm(forms.Form):
    id = forms.IntegerField(required=False)

    def clean_id(self):
        id = self.cleaned_data['id']
        if FaultsContent.objects.filter(id=id).exists():
            return id
        else:
            raise forms.ValidationError('当前故障简述编号不存在，请选择的故障简述编号.')
