################################################
#   相册数据表
#
from django.db import models
from django.utils import timezone
from django.db.models import F

from suite.const import SuiteType
from tools.utils.imgNo import DEF_START_IMG_NO
from tools import exceptions as wter
from userinfo.models import Accounts


class SuiteManager(models.Manager):
    def add_num(self, _id, attr='img_num', num=1):
        row = self.filter(id=_id).first()
        if not row:
            return 0
        if not hasattr(row, attr):
            wter.ParameterError('Suite没有属性：%s' % attr)
        old_val = getattr(row, attr, 0)
        setattr(row, attr, old_val+num)
        row.log_time = timezone.now()
        row.save()
        return num

    def get_list(self, user, **kwargs):
        # kwargs.pop('creator')
        rows = self.filter(creator=user.id, **kwargs).order_by('-create_time')
        res = []
        for row in rows:
            owner = Accounts.objects.get(user_id=user.id)
            res.append({
                'id': row.id,
                'title': row.title,
                'main_img': row.main_img,
                'head_img': row.head_img,
                'img_num': row.img_num,
                'like_num': row.like_num,
                'favor_num': row.favor_num,
                'creator': {
                    'id': user.id,
                    'nickname': owner.nickname
                },
                'beautor': row.beautor,
                'create_time': row.create_time.strftime('%Y-%m-%d %H:%M:%S')
            })
        return res


class Suite(models.Model):
    """
    picture suite info
    """
    class Meta:
        db_table = "pic_suite"
        index_together = ('creator', 'create_time')
    objects = SuiteManager()

    title = models.CharField(verbose_name='标题', max_length=100)
    main_img = models.CharField(verbose_name='主图url', max_length=255)
    head_img = models.CharField(verbose_name='主图url', max_length=255)
    img_num = models.IntegerField(verbose_name='相册图片数', default=0)
    watch_num = models.IntegerField(verbose_name='总观看数', default=0)
    online_num = models.IntegerField(verbose_name='在线人数', default=0)
    cur_code = models.CharField(verbose_name='当前上传图片最大编号', default=DEF_START_IMG_NO, max_length=16)
    # 社交
    like_num = models.IntegerField(verbose_name='点赞数', default=0)
    favor_num = models.IntegerField(verbose_name='收藏数', default=0)
    comment_num = models.IntegerField(verbose_name='留言数', default=0)
    # 相关人
    creator = models.IntegerField(verbose_name='相册创建人id')
    photographer = models.CharField(verbose_name='摄影师名字', default="", max_length=60)
    beautor = models.CharField(verbose_name='美图师名字', default="", max_length=60)
    # 相册权限类型ID
    suite_type = models.IntegerField(verbose_name='相册类型', choices=SuiteType.CHOICES)

    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    log_time = models.DateTimeField(verbose_name='更新时间', default=timezone.now)

