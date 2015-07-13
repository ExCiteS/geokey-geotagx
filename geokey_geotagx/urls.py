from django.conf.urls import patterns, url

from views import Import

urlpatterns = patterns(
    '',
    url(r'^api/geotagx/import/$', Import.as_view(), name='import'),
)
