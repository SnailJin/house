# -*- coding: utf-8 -*-
'''
Created on 2015年4月20日

@author: jin
'''
import xlsxwriter
from house.models import UserProfile
from django.contrib.auth.models import User
import datetime
from common.commit import get_obj_attr
from apps.agent.models import RecommendRecord
import os
from house.settings import PATH, MEDIA_ROOT
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def create_excel():
    now=datetime.datetime.now()
    time=now.strftime('%Y-%m-%d')
    date_from = datetime.datetime(now.year, now.month, now.day-1, 0, 0, 0)
    date_to = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
    filePath=os.path.join(os.path.dirname(MEDIA_ROOT),'xslx/%s.xlsx'%(time)).replace('\\','/')
    workbook = xlsxwriter.Workbook(filePath)
    #推荐人
    headersList=['姓名','性别','身份证号','联系方式','银行卡卡号','注册时间']
    felidList=[u'user.first_name',u'gender','IDCard','phone','bankCard','user.date_joined']
    userIds=[ user.id for user in User.objects.filter(date_joined__gt=date_from,date_joined__lte=date_to)]
    userProfileList=UserProfile.objects.select_related('user').filter(user_id__in=userIds)
    create_excel_worksheet(workbook,headersList,felidList,'注册用户',userProfileList)
     
#     #推荐记录
    headersList=['被推荐人名字','性别','身份证号','联系方式','推荐人名字','推荐时间']
    felidList=[u'client.username',u'client.gender','client.IDCard','client.phone',u'user.first_name','time']
    recommendRecordList=RecommendRecord.objects.select_related('client','user').filter(time__gt=date_from,time__lte=date_to)
    create_excel_worksheet(workbook,headersList,felidList,'推荐用户',recommendRecordList)
    workbook.close()
    
    
def create_excel_worksheet(workbook,headerList,felidList,title,dataList):
    worksheet = workbook.add_worksheet(title)
    row,col = 0,0
    for header in headerList:
        worksheet.write(row,col,header)
        col=col+1
    row,col = 1,0
    for data in dataList:
        for felid in felidList:
            value=get_obj_attr(data, felid)
            if type(value) is datetime.datetime:
                value=value.strftime('%Y-%m-%d %H:%M:%S')
            if felid.find('gender')!=-1:
                dict={'M':'男','F':'女'}
                value=dict.get(value,None)
            worksheet.write_string (row, col,value) 
            col=col+1
        row,col = row+1,0
        
