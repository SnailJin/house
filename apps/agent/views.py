#-*- coding: UTF-8 -*- 
'''
Created on 2014年12月23日

@author: jin
'''
from django.shortcuts import render
from house.models import UserProfile
from apps.agent.models import RecommendRecord, Client
from apps.agent.forms import ClientForm
from django.http.response import HttpResponseRedirect, HttpResponse
import re
from django.utils import simplejson
from house.settings import PublicWeiXinAppID, PublicWeiXinAppSecret,\
    PublicWeiXinRedirectUri, DEFAULT_PAWORD
from django.contrib import auth
def profile(request,template_name="profile.html"):
    args={}
    try:
        userProfile=UserProfile.objects.select_related('user').get(user=request.user)
        args.update({"username":userProfile.user.first_name,'userId':userProfile.user_id,"gender":userProfile.gender,\
                     "phone":userProfile.phone,})
        args["recommendCount"]=RecommendRecord.objects.filter(user=request.user).count()
        args['clientList']=Client.objects.filter(user=request.user)[:5]
        args['more']=True if len(args['clientList'])>4 else False
    except  Exception as e:
        args={'result':'error','error_message':e.message}
        template_name="error.html"
    return render(request,template_name,args)
        
def add_client(request,channel=None,template_name="add_client.html"):
    '''
    添加客户
    '''
    args={'title':'我要推荐','button':'提交'} if  channel=='recommend' else {'title':'添加客户','button':'提交'}
    try:
        if request.method=="POST":
            clientForm=ClientForm(request.POST)
            if clientForm.is_valid():
                if Client.objects.filter(user=request.user,IDCard=clientForm.cleaned_data["IDCard"]).exists():
                    if channel !='recommend':
                        from django.forms.util import ErrorList
                        errors = clientForm._errors.setdefault("IDCard", ErrorList())
                        errors.append(u"该身份证已经添加过!")
                        args['clientForm']=clientForm
                    else:
                        client=Client.objects.get(user=request.user,IDCard=clientForm.cleaned_data["IDCard"])
                        RecommendRecord(user=request.user,client=client).save()
                        return HttpResponseRedirect('/agent/client_list/')
                else:
                    client=clientForm.save(commit=False)
                    client.user=request.user 
                    client.save()
                    if channel=='recommend':
                        client=Client.objects.get(user=request.user,IDCard=clientForm.cleaned_data["IDCard"])
                        RecommendRecord(user=request.user,client=client).save()
                    return HttpResponseRedirect('/agent/client_list/')
            else:
                args['clientForm']=clientForm
        else:
            args['clientForm']=ClientForm()
    except  Exception as e:
        args={'result':'error','error_message':e.message}
        template_name="error.html"
    return render(request,template_name,args)

def client_list(request,template_name="client_list.html"):
    '''
    客户列表
    '''
    args={}
    try:
        args['clientList']=Client.objects.filter(user=request.user)
    except  Exception as e:
        args={'result':'error','error_message':e.message}
        template_name="error.html"
    return render(request,template_name,args)

def bind_account(request,template_name="bind_account.html"):
    '''
     绑定账户
    '''
    args={'result':'success'}
    try:
        if request.method=="POST":
            bankCard=request.POST['bankCard'].strip()
            if len(bankCard)==0:
                args={'result':'error','error_message':'银行卡不能为空!'}
            elif  re.match(r'^\d{16,19}$',bankCard) is  None:
                args={'result':'error','error_message':'银行卡位数不对!'}
            else:
                UserProfile.objects.filter(user=request.user).update(bankCard=bankCard)
                args['result']='success'
            
    except  Exception as e:
        args={'result':'error','error_message':e.message}
        template_name="error.html"
    if request.is_ajax():
        json=simplejson.dumps(args)
        return HttpResponse(json)
    else:
        return render(request,template_name,args)
    
    
def recommend(request,clientId):
    '''
     绑定账户
    '''
    args={'result':'success'}
    try:
        if request.method=="POST":
            clientId=int(clientId)
            if Client.objects.filter(user=request.user,id=clientId).exists():
                RecommendRecord(user=request.user,client_id=clientId).save()
                args={'result':'success'}
            else:
                args={'result':'error','error_message':'没有该用户!'}
            
    except  Exception as e:
        args={'result':'error','error_message':e.message}
    json=simplejson.dumps(args)
    return HttpResponse(json)


def public_weixin_authorization_url(request):
    from common.weinxin_api import WeiXinClient
    client = WeiXinClient(client_id=PublicWeiXinAppID,client_secret=PublicWeiXinAppSecret,redirect_uri=PublicWeiXinRedirectUri,scope="snsapi_base",state="#")
    return HttpResponseRedirect(client.public_authorization_url())  

def public_weixin_authorization(request):
    from common.weinxin_api import WeiXinClient
    client = WeiXinClient(client_id=PublicWeiXinAppID,client_secret=PublicWeiXinAppSecret,redirect_uri=PublicWeiXinRedirectUri)
    access=client.request_access_token(request.GET.get('code'))
    if UserProfile.objects.filter(uid=client.openid).exists():
        user=auth.authenticate(username=client.openid,password=DEFAULT_PAWORD)
        auth.login(request, user)
        return HttpResponseRedirect('/agent/profile/')
    else:
        request.session.update({'uid':client.openid,})
        request.session['access_token']=access.get('access_token')
        request.session['expires_in']=access.get('expires_in')
        return HttpResponseRedirect('/update_profile/')
    
    
def introduction(request,template_name="introduction.html"):
    return render(request,template_name)