from django.conf.urls.defaults import *

urlpatterns = patterns('polls.views',
    (r'^$', 'index'),
    (r'^(?P<poll_id>\w+)/$', 'detail'),
    (r'^(?P<poll_id>\w+)/results/$', 'results'),
    (r'^(?P<poll_id>\w+)/vote/$', 'vote'),
)