# 相册权限类型枚举
class SPT(object):
    B_START_IMG = 0  # 启动页图
    B_HEAD_IMG = 1  # 置顶图
    B_ALBUM = 2  # 云相册小图标
    B_TRANSITION = 3  # 过渡动画
    B_LINK_AD = 4  # 链接过渡广告
    B_WATERMARK = 5  # 支持自定义水印
    B_SHOWCREATORINFO = 6  # 显示摄影师信息
    B_VIDEO = 7   # 是否支持视频
    B_CSS = 8  # 是否支持切换css样式主题
    B_BEAUTYIMG = 9  # 是否支持后台企图


class SuiteType(object):
    # 免费版
    T_LVL0 = 0
    S_LVL0 = '免费版'
    P_LVL0 = {
        # id     版本名         相册容量      最多支持摄影师数  相册保留天数    价格
        'id': T_LVL0, 'name': S_LVL0, 'cap': 200, 'uploadNum': 2, 'keepDays': 30, 'price': 0,
        # 启动页图              置顶图                 云相册小图标       过渡动画                 链接过渡广告
        SPT.B_START_IMG: True, SPT.B_HEAD_IMG: True,  SPT.B_ALBUM: True, SPT.B_TRANSITION: True, SPT.B_LINK_AD: True,
        #  是否支持自定义水印     是否显示摄影师信息              是否支持视频      是否支持样式主题切换
        SPT.B_WATERMARK: False, SPT.B_SHOWCREATORINFO: False, SPT.B_VIDEO: False, SPT.B_CSS: False,
    }
    # 通用版
    T_LVL1 = 1
    S_LVL1 = '通用版'
    P_LVL1 = {
        'id': T_LVL1, 'name': S_LVL1, 'cap': 1000, 'uploadNum': 5, 'keepDays': 300, 'price': 200,
        SPT.B_START_IMG: True, SPT.B_HEAD_IMG: True,  SPT.B_ALBUM: True, SPT.B_TRANSITION: True, SPT.B_LINK_AD: True,
        SPT.B_WATERMARK: True, SPT.B_SHOWCREATORINFO: True, SPT.B_VIDEO: False, SPT.B_CSS: False
    }
    # 企业版
    T_LVL2 = 2
    S_LVL2 = '企业版'
    P_LVL2 = {
        'id': T_LVL2, 'name': S_LVL2, 'cap': 5000, 'uploadNum': 10, 'keepDays': 3000, 'price': 1000,
        SPT.B_START_IMG: True, SPT.B_HEAD_IMG: True,  SPT.B_ALBUM: True, SPT.B_TRANSITION: True, SPT.B_LINK_AD: True,
        SPT.B_WATERMARK: True, SPT.B_SHOWCREATORINFO: True, SPT.B_VIDEO: True, SPT.B_CSS: True
    }

    CHOICES = (
        (T_LVL0, S_LVL0),
        (T_LVL1, S_LVL1),
        (T_LVL2, S_LVL2),
    )

