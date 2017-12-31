import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from tools import exceptions as wter
from tools.utils import validators, validatecode

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
    def post(self, request):
        data = request.data
        phone = data.get('phone')
        code = data.get('code')
        password = data.get('password')
        if not phone or not code or not password:
            return Response({'status': 1, 'msg': '数据不全'})
        valid, msg = validatecode.validate_code(phone, code)
        if not valid:
            return Response({'status': 1, 'msg': msg})
        user = User.objects.create_user(phone, password=password)
        return Response({'status': 0, 'data': {}})
