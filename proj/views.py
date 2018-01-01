import logging
from rest_framework.views import APIView
from tools.utils.http import JsonResponse, Status

log = logging.getLogger('wed')


class SvrTestAPI(APIView):
    """
    测试网络用API
    """
    def get(self, request):
        return JsonResponse(Status.OK)
