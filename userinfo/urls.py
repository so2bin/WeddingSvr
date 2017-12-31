from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from userinfo.viewsets import ValidateCodeViewSet, RegisterValidateViewSet
from userinfo.viewsets import LoginViewSet, LogoutViewSet


urlpatterns = [
    url(r'^validate/code/$', ValidateCodeViewSet.as_view()),
    url(r'^validate/login-up/$', RegisterValidateViewSet.as_view()),
    url(r'^validate/login/$', LoginViewSet.as_view()),
    url(r'^validate/login-out/$', LogoutViewSet.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
