# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '2018/5/10 20:21'

import re
from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):     # 继承forms.ModelForm，而不是forms.Forms ModelForm的使用
    class Meta:
        model = UserAsk       # Model类 # 需要form校验的字段，此处字段名应与form表单提交的input的name保持一致
        fields = ['name', 'mobile', 'course_name']    # 需要校验的字段

    def clean_mobile(self):    # 对字段进行更深一层的自定义封闭，固定写法
        mobile = self.cleaned_data['mobile']  # 取出mobile字段的值，cleaned_data为一个字典型数据
        reg = "^1[34578]\d{9}$"  # 手机号码匹配正则表达式
        p = re.compile(reg)      # p为re对象
        if p.match(mobile):    # 能正确匹配
            return mobile      # 根据需要还可以返回其它值
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')  # 抛出错误异常


