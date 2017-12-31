#######################################
#  验证码

from django.db import models
from django.utils import timezone


class ValidateCodesManager(models.Manager):
    pass


class ValidateCodes(models.Model):
    """
    validate codes history
    """
    class Meta:
        db_table = "validate_codes"
        index_together = ('phone', 'code')

    objects = ValidateCodesManager()

    phone = models.CharField(verbose_name='手机号', max_length=16)
    code = models.IntegerField(verbose_name='验证码')
    expiration = models.DateTimeField(verbose_name='过期时间')
    sendtime = models.DateTimeField(verbose_name='发送时间', default=timezone.now)
    is_used = models.BooleanField(verbose_name='是否已用', default=False)




