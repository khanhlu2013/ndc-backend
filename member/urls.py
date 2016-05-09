from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from member import apis

urlpatterns = [
    url(r'^members/$', apis.Member_lst.as_view()),
    url(r'^members/(?P<pk>[0-9]+)/$', apis.Member_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)