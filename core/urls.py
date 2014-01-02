from django.utils import six   # python 3 compatibity
from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(_(r'^videos/$'), 'list_videos', name='videos'),
    url(_(r'^video/(?P<slug>[\w-]+)\.html$'), 'player', name='video_player'),
)
