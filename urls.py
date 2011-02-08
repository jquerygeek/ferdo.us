from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='site-homepage'),
    (r'^blog/', include('blog.urls')),
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns()