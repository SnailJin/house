from django.conf.urls import patterns, include, url
from house import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'house.views.home', name='home'),
    # url(r'^house/', include('house.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agent/', include('apps.agent.urls')),
    url(r'^$', 'house.views.index',{'template_name':'index.html'}),
     url(r'^update_profile/$', 'house.views.update_profile',{'template_name':'update_profile.html'}),
     url(r'^test/$', 'house.views.test'),
)
if settings.DEBUG:
   urlpatterns += patterns('',
                          url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT },name="static"),
                           url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT },name="site_media"),
                          url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT },name="media"),
)
    