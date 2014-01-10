from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'videos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('core.urls', namespace="core")),


    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


