from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^book/$', book,name='book'),
    url(r'^renwu(\d+)/$', renwu),
    url(r'^(\d+)/(\d+)/$', weizhi_url),
    url(r'^static_file/$', static_file),
    url(r'^zhuanyi/$',zhuanyi),
    url(r'^page(?P<Pnum>\d*)/$',page_test),

]
