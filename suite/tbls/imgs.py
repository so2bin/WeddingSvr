################################################
#   上传图片记录表
#
from django.db import models
from django.utils import timezone
from django.db import transaction

from suite.models import Suite
from suite.tasks import create_thumb


class PicLogManager(models.Manager):
    @transaction.atomic
    def cre_obj(self, suite_id, code, origin_url, origin_key, origin_size,
                author, beautor=""):
        cre = self.create(suite_id=suite_id, code=code, origin_url=origin_url,
                          origin_key=origin_key, origin_size=origin_size,
                          author=author, beautor=beautor)
        Suite.objects.add_num(cre.id, 'img_num', 1)
        # TODO 后台创建小图
        create_thumb(cre.id)


class PicLog(models.Model):
    """
    picture upload logs
    """
    class Meta:
        db_table = "pic_log"
        unique_together = ('suite_id', 'code')
    objects = PicLogManager()

    suite_id = models.IntegerField(verbose_name='相册id')
    code = models.CharField(verbose_name='照片编号', max_length=16)
    origin_url = models.CharField(verbose_name='大图url', max_length=400)
    origin_key = models.CharField(verbose_name='大图COS Key', max_length=255)
    thumb_url = models.CharField(verbose_name='小图url', max_length=400)
    thumb_key = models.CharField(verbose_name='小图COS Key', max_length=255)
    origin_size = models.IntegerField(verbose_name='大图尺寸', default=None, null=True)
    thumb_size = models.IntegerField(verbose_name='大图尺寸', default=None, null=True)
    watch_num = models.IntegerField(verbose_name='总观看数', default=0)
    watch_origin_num = models.IntegerField(verbose_name='原图总观看数', default=0)
    # 社交
    like_num = models.IntegerField(verbose_name='点赞数', default=0)
    favor_num = models.IntegerField(verbose_name='收藏数', default=0)
    comment_num = models.IntegerField(verbose_name='留言数', default=0)

    author = models.IntegerField(verbose_name='摄影师(上传人)', null=True, default=None)
    beautor = models.CharField(verbose_name='美图师名字', default="", max_length=60)

    log_time = models.DateTimeField(verbose_name='上传时间', default=timezone.now)
