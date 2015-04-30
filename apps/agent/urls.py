#-*- coding: UTF-8 -*- 
'''
Created on 2014年12月23日

@author: jin
'''
from django.conf.urls import patterns, url
import os
from house.settings import MEDIA_ROOT
urlpatterns=patterns('apps.agent.views',
     url(r'^profile/$', 'profile'),
     url(r'^client_list/$', 'client_list'),
     url(r'^add_client/(recommend)/$', 'add_client'),
     url(r'^add_client/$', 'add_client'),
     url(r'^bind_account/$', 'bind_account'),
     url(r'^recommend/(\d*)/$', 'recommend'),
     url(r'^introduction/$', 'introduction'),
     url(r'^public_weixin_authorization_url/$', 'public_weixin_authorization_url'),
     url(r'^public_weixin_authorization/$', 'public_weixin_authorization'),
     url(r'^download/([0-9\-]*\.xlsx)/$', 'download_xlsx',),
     
)
