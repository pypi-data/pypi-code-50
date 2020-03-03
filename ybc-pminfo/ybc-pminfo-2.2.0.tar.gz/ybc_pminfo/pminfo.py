from ybc_commons.ArgumentChecker import Checker
from ybc_commons.ArgumentChecker import Argument
from ybc_commons import httpclient
from ybc_commons.util.predicates import non_blank
from ybc_commons.context.contexts import check_arguments
from ybc_exception import exception_handler
_PM_INFO_URL = 'pm-info'


@exception_handler('ybc_pminfo')
@check_arguments({'city': non_blank})
def pm25(city: str):
    """
    获取指定城市的pm2.5信息

    :param city: 城市名(字符串类型,必填) 例如:'北京'
    :return: 指定城市的pm2.5信息(字典类型)
    """
    Checker.check_arguments(
        [Argument('ybc_pminfo', 'pm25', 'city', city, str, non_blank)])
    data = {'city': city}
    res = httpclient.post(_PM_INFO_URL, data)
    if res['code'] != 0:
        print(res['msg'])
        return -1
    return res['pmInfo']
