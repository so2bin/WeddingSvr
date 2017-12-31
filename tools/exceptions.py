from rest_framework.exceptions import APIException
from rest_framework import status


class BaseError(APIException):
    detail = 'RunError'
    code = status.HTTP_400_BAD_REQUEST
    status_code = status.HTTP_400_BAD_REQUEST


class ParameterError(BaseError):
    detail = 'Parameter Error'


class ValidateError(BaseError):
    detail = 'Validate Error'


