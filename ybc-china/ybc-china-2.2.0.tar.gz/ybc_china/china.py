from ybc_commons.ArgumentChecker import Checker
from ybc_commons.ArgumentChecker import Argument
from ybc_commons import httpclient
from ybc_commons.context.contexts import check_arguments
from ybc_commons.util.predicates import non_blank
from ybc_exception import exception_handler
_CHINA_ALL_CITIES_PATH = 'china/all-cities'
_CHINA_PROVINCES_PATH = 'china/provinces'
_CHINA_CITIES_PATH = 'china/cities'


@exception_handler('ybc_china')
def all_cities():
    """
    获取中国所有的城市

    :return: 中国所有的城市，除县级城市以外(列表类型)
    """
    res = httpclient.get(_CHINA_ALL_CITIES_PATH)
    return res['allCities']


@exception_handler('ybc_china')
def provinces():
    """
    获取中国所有的省份

    :return: 中国所有的省份(列表类型)
    """
    res = httpclient.get(_CHINA_PROVINCES_PATH)
    return res['provinces']


@exception_handler('ybc_china')
@check_arguments({'province': non_blank})
def cities(province: str):
    """
    获取指定省份下的所有城市

    :param province: 省份名字(文本类型,必填) 例子:'云南'/'云南省'
    :return: 指定省份下的所有城市(列表类型)
    """
    Checker.check_arguments([
        Argument('ybc_china', 'cities', 'province', province, str, non_blank)
    ])
    data = {'province': province}
    res = httpclient.post(_CHINA_CITIES_PATH, data)
    if res['code'] != 0:
        return res['msg']
    return res['cities']
