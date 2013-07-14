from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('user_mode.views',
    # Examples:
    # url(r'^$', 'PCS.views.home', name='home'),
    # url(r'^PCS/', include('PCS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/$', 'login', 
        name = 'user_mode_login'),
    url(r'^logout/$', 'logout', 
        name = 'user_mode_logout'),
    url(r'^register/$', 'register', 
        name = 'user_mode_register'),
    url(r'^dashboard/$', 'dashboard', 
        name = 'user_mode_dashboard'),
    url(r'^dashboard/crn_search/$', 'crn_search', 
        name = 'user_mode_crn_search'),
    url(r'^dashboard/profile/$', 'profile', 
        name = 'user_mode_profile'),
    url(r'^remove_crn/$', 'remove_crn', 
        name = 'user_mode_remove_crn'),
)
