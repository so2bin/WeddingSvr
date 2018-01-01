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


class CreateWorkViewSet(APIView):
    """
    创建相册
    """
    @transaction.atomic
    def post(self, request):
        data = request.data

        title = data.get('title')
        main_img = data.get('main_img')
        head_img = data.get('head_img')
        suite_type = data.get('sute_type')
        if not all([title, main_img, head_img, suite_type]):
            return JsonResponse(Status.WRONG, msg='参数不全')

        sut = Suite.objects.create(
            title=title, main_img=main_img, head_img=head_img,
            creator=request.user.id
        )
        return JsonResponse(Status.OK, data={
            'title': title,
            'main_img': main_img,
            'head_img': head_img,
            'creator': request.user.id
        })


class WorkListViewSet(APIView):
    """
    相册列表
    """
    def get(self, request):
        return Suite.objects.get_list(user=request.user)
