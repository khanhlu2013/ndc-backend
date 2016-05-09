from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from event import apis

urlpatterns = [
    url(r'^events/$', apis.Event_lst.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', apis.Event_detail.as_view()),
    url(r'^venues/$', apis.Venue_lst.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
