from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^portfolio/', views.get_portfolio_list),
    url(r'^home/', views.get_random_images),
    url(r'^$', views.get_random_images),
    url(r'^', views.get_random_images),
)