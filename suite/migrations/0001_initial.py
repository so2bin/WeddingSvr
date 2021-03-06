# Generated by Django 2.0 on 2018-01-06 02:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PicLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suite_id', models.IntegerField(verbose_name='相册id')),
                ('code', models.CharField(max_length=16, verbose_name='照片编号')),
                ('origin_url', models.CharField(max_length=400, verbose_name='大图url')),
                ('origin_key', models.CharField(max_length=255, verbose_name='大图COS Key')),
                ('thumb_url', models.CharField(max_length=400, verbose_name='小图url')),
                ('thumb_key', models.CharField(max_length=255, verbose_name='小图COS Key')),
                ('origin_size', models.IntegerField(default=None, null=True, verbose_name='大图尺寸')),
                ('thumb_size', models.IntegerField(default=None, null=True, verbose_name='大图尺寸')),
                ('watch_num', models.IntegerField(default=0, verbose_name='总观看数')),
                ('watch_origin_num', models.IntegerField(default=0, verbose_name='原图总观看数')),
                ('like_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('favor_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('comment_num', models.IntegerField(default=0, verbose_name='留言数')),
                ('author', models.IntegerField(default=None, null=True, verbose_name='摄影师(上传人)')),
                ('beautor', models.CharField(default='', max_length=60, verbose_name='美图师名字')),
                ('log_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='上传时间')),
            ],
            options={
                'db_table': 'pic_log',
            },
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('main_img', models.CharField(max_length=255, verbose_name='主图url')),
                ('head_img', models.CharField(max_length=255, verbose_name='主图url')),
                ('img_num', models.IntegerField(default=0, verbose_name='相册图片数')),
                ('watch_num', models.IntegerField(default=0, verbose_name='总观看数')),
                ('online_num', models.IntegerField(default=0, verbose_name='在线人数')),
                ('cur_code', models.CharField(default='0000', max_length=16, verbose_name='当前上传图片最大编号')),
                ('like_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('favor_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('comment_num', models.IntegerField(default=0, verbose_name='留言数')),
                ('creator', models.IntegerField(verbose_name='相册创建人id')),
                ('photographer', models.CharField(default='', max_length=60, verbose_name='摄影师名字')),
                ('beautor', models.CharField(default='', max_length=60, verbose_name='美图师名字')),
                ('suite_type', models.IntegerField(choices=[(0, '免费版'), (1, '通用版'), (2, '企业版')], verbose_name='相册类型')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('log_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'pic_suite',
            },
        ),
        migrations.AlterIndexTogether(
            name='suite',
            index_together={('creator', 'create_time')},
        ),
        migrations.AlterUniqueTogether(
            name='piclog',
            unique_together={('suite_id', 'code')},
        ),
    ]
