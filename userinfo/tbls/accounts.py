from django.db import models


class Accounts(models.Model):
    """
    account info
    """
    class Meta:
        db_table = "user_accounts"
    user_id = models.IntegerField(verbose_name='user id', default=0, db_index=True)
    openid = models.CharField(verbose_name='微信openid', max_length=300, db_index=True)
    phone = models.CharField(verbose_name='手机号', max_length=16, db_index=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64)
    pos_id = models.IntegerField(verbose_name='位置记录id', null=True, default=None)
    small_head_img = models.CharField(verbose_name='头像小图', max_length=500, default="")
    big_head_img = models.CharField(verbose_name='头像大图', max_length=500, default="")
    age = models.IntegerField(verbose_name='年龄', default=0)

