#-*- coding: UTF-8 -*- 
'''
Created on 2014年12月23日

@author: jin
'''
import logging
from django.shortcuts import render_to_response, render
from house.forms import UserProfileForm
from django.http.response import HttpResponseRedirect, HttpResponse
from house.settings import DEFAULT_PAWORD
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password
def index(request,template_name):
    '''
    首页
    '''
    try:
        return render_to_response(template_name,{})
    except Exception as e:
        logging.error(e.message)
        
def update_profile(request,template_name):
    '''
    更新用户信息
    '''
    args={}
    try:
        if request.method=='POST':
            userProfileForm=UserProfileForm(request.POST)
            user=auth.authenticate(username='oFP0btwgYGn81VzfxG_x8H8jDihA',password=DEFAULT_PAWORD)
            auth.login(request, user)
            if userProfileForm.is_valid():
                username=userProfileForm.cleaned_data['username']
                uid=request.session.get('uid')
                user=User(first_name=username,username=uid,password=make_password(DEFAULT_PAWORD))
                userProfile=userProfileForm.save(commit=False)
#                 user.save()
                user=auth.authenticate(username=uid,password=DEFAULT_PAWORD)
                auth.login(request, user)
                userProfile.uid=uid
                userProfile.user=request.user
#                 userProfile.save()
                return HttpResponseRedirect('/agent/profile/')
            else:
                args['userProfileForm']=userProfileForm
#                 errors=userProfileForm.errors
#                 args={'result':'error','error_message':errors[0][1][0]if errors[0][0]==u'__all__' else '%s %s'%(userProfileForm.base_fields[errors[0][0]].label,errors[0][1][0])} 
        else:
            args['userProfileForm']=UserProfileForm() 
    except Exception as e:
        logging.error(e.message)
        args={'result':'error','error_message':e.message}
        template_name='error.html'
    return render(request,template_name,args)

def test(request):
    from common.excel import create_excel
    create_excel()
    return HttpResponse('successs')
    