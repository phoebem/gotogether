from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import gotogether.views
#from gotogether import urls

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', gotogether.views.index, name='index'),
    url(r'^user/(?P<uid>\d+)', gotogether.views.user, name='user'),
    #url(r'^splash', gotogether.views.splash, name='splash'),
    url(r'^login', gotogether.views.login, name='login'),
    url(r'^event/(?P<uid>\d+)/(?P<id>\d+)', gotogether.views.event, name='event'),
    url(r'^newevent/(?P<uid>\d+)/(?P<id>\d+)', gotogether.views.newevent, name='newevent'),
    url(r'^profile/(?P<uid>\d+)/(?P<id>\d+)', gotogether.views.profile, name='profile'),
    url(r'^pcontacts/(?P<uid>\d+)/(?P<pid>\d+)', gotogether.views.pcontacts, name='pcontacts'),
    url(r'^econtacts/(?P<uid>\d+)/(?P<pid>\d+)', gotogether.views.econtacts, name='econtacts'),
    url(r'^activity/(?P<uid>\d+)/(?P<pid>\d+)/(?P<id>\d+)', gotogether.views.activity, name='activity'),
    url(r'^camping/(?P<uid>\d+)/(?P<pid>\d+)/(?P<id>\d+)', gotogether.views.camping, name='camping'),
    url(r'^food/(?P<uid>\d+)/(?P<pid>\d+)/(?P<id>\d+)', gotogether.views.food, name='food'),
    url(r'^pactivity/(?P<uid>\d+)/(?P<pid>\d+)/(?P<id>\d+)', gotogether.views.pactivity, name='pactivity'),
    url(r'^pcamping/(?P<uid>\d+)/(?P<pid>\d+)/(?P<id>\d+)', gotogether.views.pcamping, name='pcamping'),
    url(r'^pfood/(?P<uid>\d+)/(?P<pid>\d+)/(?P<id>\d+)', gotogether.views.pfood, name='pfood'),
    url(r'^location/(?P<uid>\d+)/(?P<pid>\d+)', gotogether.views.location, name='location'),
    url(r'^rsvp/(?P<uid>\d+)/(?P<id>\d+)', gotogether.views.rsvp, name='rsvp'),
    url(r'^rental/(?P<uid>\d+)/(?P<pid>\d+)/(?P<id>\d+)', gotogether.views.rental, name='rental'),
    #url(r'^hotel/(?P<uid>\d+)/(?P<eid>\d+)/(?P<id>\d+)', gotogether.views.hotel, name='hotel'),
    url(r'^venue/(?P<uid>\d+)/(?P<eid>\d+)/(?P<id>\d+)', gotogether.views.business, name='venue'),
    url(r'^booking/(?P<uid>\d+)/(?P<eid>\d+)/(?P<id>\d+)', gotogether.views.booking, name='booking'),
    url(r'^admin/', include(admin.site.urls)),
]
