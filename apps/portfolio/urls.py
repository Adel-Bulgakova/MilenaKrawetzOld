from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.get_portfolio_list),
    # url(r'^(?P<pk>\d+)/$', picture_detail_view.as_view())
)