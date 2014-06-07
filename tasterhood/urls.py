from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasterhood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Disabling admin console for time being
    url(r'^admin/', include(admin.site.urls)),

    url(r'^main/', include('main.urls')),
)
