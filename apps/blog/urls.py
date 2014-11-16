from django.conf.urls import patterns, url

from views import posts_list_view, post_detail_view

urlpatterns = patterns('',
    url(r'^$', posts_list_view.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', post_detail_view.as_view()),
)
