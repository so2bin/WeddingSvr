from rest_framework.response import Response
from rest_framework import status


class Status(object):
    OK = 0
    WRONG = 1
    ERROR = 2


def JsonResponse(state, msg="", data=None, **kwargs):
    """
    统一返回方式
    :param state:
    :param msg:
    :param data:
    :param kwargs:
    :return:
    """
    return Response({
        'status': state,
        'msg': msg,
        'data': data
    }, **kwargs)
