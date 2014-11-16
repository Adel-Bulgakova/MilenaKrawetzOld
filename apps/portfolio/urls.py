from django.conf.urls import patterns, url
from views import pictures_list_view, picture_detail_view

urlpatterns = patterns('',
    url(r'^$', pictures_list_view.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', picture_detail_view.as_view())
)