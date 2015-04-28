# -*- coding: utf-8 -*-
'''
Created on Sep 24, 2013

@author: jin
'''
from django.db import models
from django.contrib.auth.models import User
import re
from django.core import validators
class UserProfile(models.Model):
    user=models.OneToOneField(User,verbose_name=r'用户')
    gender=models.CharField(verbose_name=r'性别',max_length='2',choices=(('M','男'),('F','女')))
    IDCard=models.CharField(verbose_name=r'身份证 ',max_length=20,unique=True,validators=[
            validators.RegexValidator(re.compile('^\d{15}(?:\d{3}|\d{2}[a-zA-Z]|)$'), "证件位数或格式不正确！", 'invalid')
        ])
    phone=models.CharField(verbose_name='手机号码',max_length=20,validators=[
            validators.RegexValidator(re.compile('^\d{11}$'), "手机号码位数为11位！", 'invalid')
        ])
    uid=models.CharField(verbose_name='微信uid',max_length=125,unique=True)
    bankCard=models.CharField(verbose_name='信用卡',max_length=30,)
    data=models.CharField(verbose_name='数据',max_length=255,)
    class Meta:
        verbose_name = u'用户详细信息' 
        verbose_name_plural = u'用户详细信息'
        db_table = "user_profile" 
