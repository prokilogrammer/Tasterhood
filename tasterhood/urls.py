from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from main.api import LoginResource, UserProfileResource, UserResource, ContactResource

# Enable the admin console
admin.autodiscover()

# Enable v1 api
v1_api = Api(api_name='v1')
v1_api.register(ContactResource())
v1_api.register(UserResource())
v1_api.register(UserProfileResource())
v1_api.register(LoginResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasterhood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^main/', include('main.urls')),

    # APIs
    url(r'^api/', include(v1_api.urls)),
)
