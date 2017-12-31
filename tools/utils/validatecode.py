###########################
#  验证码
import random
import datetime
from django.utils import timezone
from tools.tbls.validatecode import ValidateCodes
from tools import exceptions as wter

DEFAULT_VALIDATE_CODE_LEN = 4
MAX_CODE = 9999
CODE_EFFECTIVE_SECONDS = 10*60  # seconds
CODE_SEND_INTERVAL = 60  # seconds  minimum send interval


def _gen_code(_len=DEFAULT_VALIDATE_CODE_LEN):
    """
    generate a validate code with len
    :param _len:
    :return:
    """
    return str(random.randint(0, MAX_CODE)).zfill(_len)


def gene_validate_code(phone):
    """
    generate a validate code for phone, ang log in database
    :param phone:
    :return:
    """
    if not phone:
        raise wter.ParameterError('Phone cannot be empty')
    code = _gen_code()
    now = timezone.now()
    expire = now + datetime.timedelta(seconds=CODE_EFFECTIVE_SECONDS)
    ValidateCodes.objects.create(phone=phone, code=code, expiration=expire)
    return code


def validate_code(phone, code):
    """
    validate the code is effective to this phone
    :param phone:
    :param code:
    :return:
    """
    if not phone or not code:
        raise wter.ParameterError('Invalid Code')
    row = ValidateCodes.objects.filter(phone=phone, code=code).order_by('id').last()
    if not row:
        return False, '无效验证码'
    if row.is_used:
        return False, '验证码已被使用'
    now = timezone.now()
    if row.expiration < now:
        return False, '验证已失效'
    return True, ''


def can_send_code(phone):
    """
    a phone can send one code in 60 seconds
    :param phone:
    :return:
    """
    row = ValidateCodes.objects.filter(phone=phone, is_used=False).last()
    if not row:
        return True, 0
    now = timezone.now()
    next_time = row.sendtime + datetime.timedelta(seconds=CODE_SEND_INTERVAL)
    if now > next_time:
        return True, 0
    else:
        dt = next_time - now
        return False, dt.seconds
