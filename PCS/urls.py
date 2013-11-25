import os
from django.conf.urls import patterns, include, url
from PCS import views, settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PCS.views.home', name='home'),
    # url(r'^PCS/', include('PCS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.banned, name='banned'),
    url(r'^secret/$', views.index, name='home'),
    url(r'^seats_check/', include('seats_check.urls')),
    url(r'^accounts/', include('user_mode.urls')),
    url(r'^weixin/', include('weixin.urls')),
    url(r'^not_completed$', views.not_completed, name='not_completed'),
    url(r'^api/$', views.api, name='api'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^used_book/', include('used_book.urls')),
)
