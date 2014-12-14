from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.get_posts_list),
    url(r'^(?P<pk>\d+)/$', views.get_post_detail),
)
	# (r'^$', views.get_posts_list),
	# (r'^(?P<url>.*)/product/(?P<pk>\d+)/$', views.product),
	# (r'^(?P<url>.*)/$', views.category),