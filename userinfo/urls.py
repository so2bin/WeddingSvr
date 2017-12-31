from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from userinfo.viewsets import ValidateCodeViewSet, RegisterValidateViewSet


urlpatterns = [
    url(r'^validate/code/$', ValidateCodeViewSet.as_view()),
    url(r'^validate/login/$', RegisterValidateViewSet.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)