# -*- coding: utf-8 -*-
'''
Created on 2015年4月20日

@author: jin
'''
def get_obj_attr(obj,name):
    nameList=name.split('.')
    for key in nameList:
        obj=getattr(obj, key)
    return obj