from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from geoserver.views import home

from tastypie.api import Api
from .api import PollDataResource

v1_api = Api(api_name='v1')
v1_api.register(PollDataResource())

urlpatterns = patterns('',
    url(r'^geo$', home, name='home'),
    url(r'^geo/api/', include(v1_api.urls)),
)
