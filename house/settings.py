# -*- coding: utf-8 -*-
# Django settings for pinlove project.
import os
import sys
PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

CRONJOBS = [
    ('1 30 * * *', 'common.excel.create_excel')
]
MANAGERS = ADMINS
ADMIN_MEDIA_PREFIX = '/admin_media/'
# AUTHENTICATION_BACKENDS = ('house.backends',)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False
DEFAULT_PAWORD='house_password_1234554321'


# Additional locations of static files
STATICFILES_DIRS = (
   ('css',os.path.join(PATH,'static/css').replace('\\','/') ),  
    ('js',os.path.join(PATH,'static/js').replace('\\','/') ), 
    ('img',os.path.join(PATH,'static/img').replace('\\','/') ), 
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'buxmr2-s(7c6)fd_omfcdh_e3w!*oi)yc222=v=5c_0=x79#00'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.cache.UpdateCacheMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS=(
    "django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
'django.core.context_processors.request',
)

ROOT_URLCONF = 'house.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'house.wsgi.application'

TEMPLATE_DIRS = (
     # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.="/static/img/logo.png"/></a></d
    # Don't forget to use absolute paths, not relative paths.
)
templates=['templates',]
for template in templates:
    TEMPLATE_DIRS += (os.path.join(PATH,template).replace('\\','/'),) 


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'apps.agent',
    'house',
    'apps.django_crontab',
)
 
PAYPAL_RECEIVER_EMAIL = "pinloveteam@gmail.com"
PAYPAL_TEST=False
#test account
# PAYPAL_RECEIVER_EMAIL = "pinloveteam-facilitator@gmail.com"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
    
# # Host for sending e-mail.
# EMAIL_HOST = 'smtp.webfaction.com'
# 
# 
# # Port for sending e-mail.
# EMAIL_PORT = 587
# 
# # Optional SMTP authentication information for EMAIL_HOST.
# EMAIL_HOST_USER = 'pinloveteam'
# EMAIL_HOST_PASSWORD = 'redyellowblue123#'
DEFAULT_FROM_EMAIL = 'pinloveteam@pinlove.com'
# SERVER_EMAIL = 'pinloveteam@pinpinlove.com'
# EMAIL_USE_TLS = True
# 
# # EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_FILE_PATH = 'email_message/' # change this to a proper location

AWS_ACCESS_KEY_ID = 'AKIAI4FL6KRW6QR2GBRA'
AWS_SECRET_ACCESS_KEY = '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'
EMAIL_BACKEND = 'django_ses.SESBackend'

WEBSITE="http://ec2-52-68-188-233.ap-northeast-1.compute.amazonaws.com"
PublicWeiXinAppID="wx0fa8047ebccc831f"
PublicWeiXinAppSecret="34382631530580dc1c08670835bf5226"
PublicWeiXinRedirectUri="%s/agent/public_weixin_authorization/"%(WEBSITE)

#set the session paramter session的控制
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE=60*60*12
# 本地环境
# DATABASES = {
#                                       
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'weixin',                      # Or path to database file if using sqlite3.
#                                                 # The following settings are not used with sqlite3:
#         'USER': 'root',                         #pinloveteam
#         'PASSWORD': 'jin521436',                       #redyellowblue123#
#         'HOST': '',                             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '',      
#                                                 # Set to empty string for default.
#     }
# }
# MEDIA_URL = '/media/'
# STATIC_URL = '/static/'
# MEDIA_ROOT = os.path.join(os.path.dirname(PATH),'update').replace('\\','/')
# STATIC_ROOT = os.path.join(PATH,'static').replace('\\','/')
# DEBUG = True
# TEMPLATE_DEBUG = True

#---服务器环境-----
DEBUG = False
TEMPLATE_DEBUG = DEBUG
DATABASES = {
                                           
      'default': {
          'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'weixin',                      # Or path to database file if using sqlite3.
                                                  # The following settings are not used with sqlite3:
          'USER': 'root',
          'PASSWORD': 'jin521436',
          'HOST': '',                             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
          'PORT': '',                             # Set to empty string for default.
          'OPTIONS':{'init_command':'SET storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci',},
      }
  }
#upload 上传地址
MEDIA_URL = '/media/'
MEDIA_ROOT =os.path.join(os.path.dirname(PATH),'update').replace('\\','/')
#静态文件地址
STATIC_ROOT = os.path.join(PATH,'static').replace('\\','/')
STATIC_URL = '/static/'

if __name__=='__main__':
    print os.path.join(os.path.dirname(PATH))
    print MEDIA_ROOT