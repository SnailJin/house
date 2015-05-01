# -*- coding: utf-8 -*-
'''
Created on 2014年4月17日

@author: jin
'''
from django.core.management.base import BaseCommand
import logging
from common.excel import create_excel
import datetime
loger=logging.getLogger(__name__)
'''
调用方式1：
 attribute：
   
    args=( operation)python manage.py 
    operation: task ,test_education
    example:
     1. python manage.py user task
     
         
'''
class Command(BaseCommand):
    def handle(self, *args, **options):
      try:
          create_excel()
      except Exception as e:
          self.stdout.write(e.message)
      finally:
          timeStr=datetime.datetime.now().strftime('%Y-%m-%d')
          self.stdout.write('%s运行一次'%(timeStr))
             