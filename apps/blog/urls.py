from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.get_posts_list),
    url(r'^(?P<pk>\d+)/$', views.get_post_detail),
)
