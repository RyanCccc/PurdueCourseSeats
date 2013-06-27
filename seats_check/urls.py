from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('seats_check.views',
    # Examples:
    # url(r'^$', 'PCS.views.home', name='home'),
    # url(r'^PCS/', include('PCS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^(?P<class_crn>\w+)/$', 'seats_check', 
        name = 'seats_check_seat_check'),
    url(r'^(?P<class_crn>\w+)/(?P<term>\w+)/$', 'seats_check', 
        name = 'seats_check_seat_check'),
)
