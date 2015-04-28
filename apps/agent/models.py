# -*- coding: utf-8 -*-
'''
Created on Sep 24, 2013

@author: jin
'''
from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import User
class Client(models.Model):
    user=models.ForeignKey(User)
    username=models.CharField(verbose_name=r'姓名',max_length='125')
    gender=models.CharField(verbose_name=r'性别',max_length='2',choices=(('M','男'),('F','女')))
    IDCard=models.CharField(verbose_name=r'身份证 ',max_length=20,validators=[
            validators.RegexValidator(re.compile('^\d{15}(?:\d{3}|\d{2}[a-zA-Z]|)$'), "证件位数或格式不正确！", 'invalid')
        ])
    phone=models.CharField(verbose_name='手机号码',max_length=20,validators=[
            validators.RegexValidator(re.compile('^\d{11}$'), "手机号码位数为11位！", 'invalid')
        ])
    
    class Meta:
        verbose_name = u'客户' 
        verbose_name_plural = u'客户'
        db_table = "client" 

class RecommendRecord(models.Model):
    user=models.ForeignKey(User)
    client=models.ForeignKey(Client)
    time=models.DateTimeField(verbose_name=r'时间',auto_now=True)
    class Meta:
        verbose_name = u'推荐记录' 
        verbose_name_plural = u'推荐记录'
        db_table = 'recommend_record'
        