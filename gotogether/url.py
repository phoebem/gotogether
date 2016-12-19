from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^user/(?P<uid>\d+)', views.user, name='user'),
    url(r'^splash', splash, name='splash'),
    url(r'^login', login, name='login'),
    url(r'^event/(?P<uid>\d+)/(?P<id>\d+)', event, name='event'),
    url(r'^profile/(?P<uid>\d+)/(?P<id>\d+)', profile, name='profile'),
]

