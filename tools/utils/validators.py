############################
#  验证器相关

from tools import const


def test_phone(phone):
    """
    validate phone number
    :param phone:
    :return:
    """
    phone = phone.strip()
    phone = phone.replace('-', '').replace(' ', '')
    if not phone or len(phone) < 11:
        return False
    if not const.RE_PHONE.match(phone):
        return False
    else:
        return True


