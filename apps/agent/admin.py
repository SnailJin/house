#-*- coding: utf-8 -*-
'''
Created on Jul 4, 2013

@author: jin
'''

from django.contrib import admin
from apps.agent.models import Client, RecommendRecord
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('username','user_username','IDCard')
 
class RecommendRecordAdmin(admin.ModelAdmin):
     search_fields = ('user_username','client_username')
    
admin.site.register(Client,ClientAdmin)
admin.site.register(RecommendRecord,RecommendRecordAdmin)


