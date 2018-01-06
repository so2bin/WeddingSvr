from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from suite.viewsets import CreateWorkViewSet, WorkListViewSet, UploadPictureViewSet


urlpatterns = [
    url(r'^create/$', CreateWorkViewSet.as_view()),
    url(r'^list/$', WorkListViewSet.as_view()),
    url(r'^upload_pic/$', UploadPictureViewSet.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
