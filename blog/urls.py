from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^$', 'index'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^(?P<post_id>\w+)/(?P<post_slug>[a-zA-Z0-9_.-]+)/$', 'detail'),
)