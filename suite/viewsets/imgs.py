import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.contrib.auth.models import User

from tools import exceptions as wter
from tools.utils.http import JsonResponse, Status
from suite.models import Suite, PicLog

log = logging.getLogger('wed')


class UploadPictureViewSet(APIView):
    """
    上传大图，后台上传小图
    """
    @transaction.atomic
    def post(self, request):
        data = request.data

        suite_id = data.get('suite_id')
        code = data.get('code')
        origin_url = data.get('origin_url')
        origin_key = data.get('origin_key')
        origin_size = data.get('origin_size')
        beautor = data.get('beautor', '')
        if not all([suite_id, code, origin_url, origin_key, origin_size]):
            return JsonResponse(Status.WRONG, msg='参数不全')
        author = request.user.id
        PicLog.objects.cre_obj(suite_id=suite_id, code=code, origin_url=origin_url, origin_key=origin_key,
                               origin_size=origin_size, author=author, beautor=beautor)
        return JsonResponse(Status.OK, data={'url': origin_url, 'key': origin_key})

