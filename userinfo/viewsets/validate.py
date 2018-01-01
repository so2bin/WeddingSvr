import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

from tools import exceptions as wter
from tools.utils import validators, validatecode
from userinfo.models import Accounts

log = logging.getLogger('wed')


class ValidateCodeViewSet(APIView):
    """
    验证码登录接口
    """
    def post(self, requse):
        data = requse.data
        phone = data.get('phone')
        if not data:
            return Response({'status': 1, 'msg': '手机号不能为空'})
        if not validators.test_phone(phone):
            return Response({'status': 1, 'msg': '无效手机号'})
        if User.objects.filter(username=phone):
            return Response({'status': 1, 'msg': '手机号已经注册'})
        can_send, left_sec = validatecode.can_send_code(phone)
        if not can_send:
            return Response({'status': 1, 'msg': '间隔不能小于60秒，剩余%s' % left_sec})
        # call send
        code = validatecode.gene_validate_code(phone)

        log.info('send validate code: %s, %s' % (phone, code))
        return Response({'status': 0})


class RegisterValidateViewSet(APIView):
    """
    带上验证码完成注册
    """
    @transaction.atomic
    def post(self, request):
        data = request.data
        phone = data.get('phone')
        code = data.get('code')
        password = data.get('password')
        nickname = data.get('nickname')
        if not phone or not code or not password or not nickname:
            return Response({'status': 1, 'msg': '数据不全'})
        valid, msg = validatecode.validate_code(phone, code)
        if not valid:
            return Response({'status': 1, 'msg': msg})
        user = User.objects.create_user(phone, password=password)
        Accounts.objects.create(user_id=user.id, phone=user.username, nickname=nickname)
        return Response({'status': 0, 'data': {
            'id': user.id, 'phone': user.username, 'nickname': nickname
        }})


class LoginViewSet(APIView):
    """
    login in
    """
    def post(self, request):
        data = request.data
        phone = data.get('phone')
        password = data.get('password')
        if not phone or not password:
            return Response({'status': 1, 'msg': '帐号/密码不能为空'})
        user = authenticate(username=phone, password=password)
        if not user:
            return Response({'status': 1, 'msg': '登陆验证失败，无效帐号密码'})
        else:
            if user.is_active:
                login(request, user)
                uinfo = Accounts.objects.get(user_id=user.id)
                return Response({'status': 0, 'data': {
                    'id': user.id, 'phone': user.username, 'nickname': uinfo.nickname
                }})
            else:
                return Response({'status': 1, 'msg': '用户已失效'})


class LogoutViewSet(APIView):
    """
    login out
    """
    def get(self, request):
        logout(request)
        return Response({'status': 0})

