# -*- coding: utf-8 -*-
'''
Created on 2015年4月22日

@author: jin
'''
from django import forms
from house.models import UserProfile
import re
from django.core import validators
class UserProfileForm(forms.ModelForm):
    '''
    用户信息表
    '''
    def __init__(self,*args,**kwarg):
        super(UserProfileForm,self).__init__(*args,**kwarg)
        for key in self.fields:
            self.fields[key].widget.attrs['class']="form-control"
        self.fields['gender'].choices=self.fields['gender'].choices[1:]
            
    username=forms.CharField(label='姓名',max_length=30,required=True,
                             validators=[validators.RegexValidator(re.compile(ur'^[\u4e00-\u9fa5a-zA-Z\xa0-\xff_][\u4e00-\u9fa50-9a-zA-Z\xa0-\xff_\s]{1,19}$'),'姓名格式有误', 'invalid')])
    class Meta:
        model=UserProfile
        exclude=('user','data','uid','bankCard')
