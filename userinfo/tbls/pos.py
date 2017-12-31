from django.db import models


class Position(models.Model):
    """
    position info
    """
    class Meta:
        db_table = "position"

    longitude = models.IntegerField(verbose_name='经度', default=None, null=True)
    latitude = models.IntegerField(verbose_name='维度', default=None, null=True)
    zoom = models.IntegerField(verbose_name='经纬度缩放', default=1)
    nation = models.CharField(verbose_name='国家', max_length=31, default=None, null=True)
    province = models.CharField(verbose_name='省/州/自治区', max_length=100)
    city = models.CharField(verbose_name='市', max_length=100)
    region = models.CharField(verbose_name='区/县', max_length=100)
    street = models.CharField(verbose_name='街道', max_length=200)
    detail = models.CharField(verbose_name='详细', max_length=300)

