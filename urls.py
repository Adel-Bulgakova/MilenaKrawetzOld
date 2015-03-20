from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^about/', include('home.urls')),
    url(r'^', include('portfolio.urls')),
)
