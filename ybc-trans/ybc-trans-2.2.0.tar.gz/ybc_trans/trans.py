from ybc_commons.ArgumentChecker import Checker
from ybc_commons.ArgumentChecker import Argument
from ybc_commons import httpclient
from ybc_commons.util.predicates import non_blank
from ybc_commons.context.contexts import check_arguments
from ybc_exception import exception_handler
_ZH_TO_EN_URL = 'translate/zh-en'
_EN_TO_ZH_URL = 'translate/en-zh'


@exception_handler('ybc_trans')
@check_arguments({'text': non_blank})
def en2zh(text: str):
    """
    英译汉

    :param text: 要翻译的英语内容(字符串类型,必填) 例子:'hello'
    :return: 翻译后的汉语内容(字符串类型)
    """
    Checker.check_arguments(
        [Argument('ybc_trans', 'en2zh', 'text', text, str, non_blank)])
    data = {'q': text}
    res = httpclient.post(_EN_TO_ZH_URL, data)
    if res['code'] != 0:
        return res['msg']
    return res['translation']


@exception_handler('ybc_trans')
@check_arguments({'text': non_blank})
def zh2en(text: str):
    """
    汉译英

    :param text: 要翻译的中文内容(字符串类型,必填) 例子:'你好'
    :return: 翻译后的英文内容(字符串类型)
    """
    Checker.check_arguments(
        [Argument('ybc_trans', 'zh2en', 'text', text, str, non_blank)])
    data = {'q': text}
    res = httpclient.post(_ZH_TO_EN_URL, data)
    if res['code'] != 0:
        return res['msg']
    return res['translation']
