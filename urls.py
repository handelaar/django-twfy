from django.conf.urls.defaults import *
from parliament.models import Member, Hansard

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from parliament import views

admin.autodiscover()

members_dict = { 'queryset': Member.objects.filter(left_reason="still_in_office").order_by("last_name"), }
debates_dict = { 'queryset': Hansard.objects.filter(major=1,htype=10).order_by("hpos"), "date_field": "hdate", }



urlpatterns = patterns('',
    # Example:
    #(r'^djangowfy/', include('django-twfy.parliament.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    
    (r'^members/$', 'django.views.generic.list_detail.object_list', members_dict),
    (r'^members/(?P<member_id>\d+)/$', 'parliament.views.memberdetail'),
    
    #
    #  This one shows a debate index for Major type=1 at (eg) debates/2009/jul/02
    #
    
    (r'^debates/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', debates_dict),

)
