from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^about/', views.about),
    url(r'^', views.home),
)