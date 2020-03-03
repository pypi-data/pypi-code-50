from functools import partial

from ybc_commons.context import check_arguments
from ybc_exception import ParameterTypeError
from ybc_exception import exception_handler
from ybc_kit import send_function_call_request
import sys

handle_exception = exception_handler('ybc_box')

send_to_oss_and_await = partial(
    send_function_call_request, 'python.easygui')


def _adapt_path(path=''):
    sys_platform = sys.platform
    if sys_platform == 'win32':
        return path.replace('/', '\\')
    if sys_platform == 'linux':
        return path.replace('\\', '/')
    if sys_platform == 'darwin':
        return path.replace('\\', '/')
    return path


@handle_exception
@check_arguments
def buttonbox(msg='', choices: (list, tuple) = tuple(), title=''):
    """
    展示一个按钮弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'下面选项为汽车品牌'
    :param choices: 选项(列表类型,非必填) 例子:['奥迪','奔驰']
    :param title: 弹框标题(文本类型,非必填) 例子:'选择你最喜欢的品牌'
    :return: 返回选中选项(字符串类型)
    """
    return send_to_oss_and_await('buttonbox', msg, title, choices)


@handle_exception
@check_arguments
def choicebox(msg='', choices: (list, tuple) = tuple(), title=''):
    """
    展示一个选项弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'下面选项为汽车品牌'
    :param choices: 选项(列表类型,非必填) 例子:['奥迪','奔驰']
    :param title: 弹框标题(文本类型,非必填) 例子:'选择你最喜欢的品牌'
    :return: 返回选中选项(字符串类型)
    """
    return send_to_oss_and_await('choicebox', msg, title, choices)


@handle_exception
@check_arguments
def enterbox(msg='', image: (str, list, tuple) = None, title='', default=''):
    """
    展示一个输入弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'请输入内容'
    :param image: 要展示的图片名(图片类型,非必填) 例子:'1.jpg'
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :param default: 输入框预留文字(文本类型,非必填) 例子:'请输入内容'
    :return: 返回在弹框中输入的文本(字符串类型)
    """
    return send_to_oss_and_await(
        'enterbox', msg, title, image=image, default=default)


@handle_exception
def fileopenbox(msg='', title=''):
    """
    展示一个可以选择文件的弹框

    :param msg: 要展示的信息(文本类型,非必填) 例子:'我的文件'
    :param title: 弹框标题(文本类型,非必填) 例子:'请选择一张图片'
    :return: 返回用户所选择文件的路径(字符串类型)
    """
    res = send_to_oss_and_await('fileopenbox', msg, title)
    return _adapt_path(res[0]) if res else None


@handle_exception
@check_arguments
def indexbox(msg='', choices: (list, tuple) = tuple(), title=''):
    """
    展示一个选项弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param choices: 选项(列表类型,非必填) 例子:['奥迪','奔驰']
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :return: 返回选中选项(字符串类型)
    """
    return send_to_oss_and_await('indexbox', msg, title, choices)


@handle_exception
@check_arguments
def msgbox(msg='', image: (str, list, tuple) = None, audio: str = ''):
    """
    展示一个消息弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'我想展示的信息'
    :param image: 要展示的图片的文件名(文本类型或列表,非必填) 例子:'1.jpg'
    :param audio: 要播放的音频文件的名字(音频类型,非必填) 例子:'1.mp3'
    :return: 点击弹框的'确认'按钮返回字符串'ok'，点击关闭按钮返回 None
    """
    if isinstance(msg, (dict, list, tuple)):
        msg = str(msg)[1:-1]
    elif isinstance(msg, bool):
        msg = '1' if msg else '0'
    else:
        msg = str(msg)

    return send_to_oss_and_await('msgbox', msg, image=image, audio=audio)


@handle_exception
@check_arguments
def multchoicebox(msg='', choices: (list, tuple) = tuple(), title=''):
    """
    展示一个多选弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param choices: 选项(列表类型,非必填) 例子:['奥迪','奔驰']
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :return: 返回选中选项(列表类型)
    """
    return send_to_oss_and_await('multchoicebox', msg, title, choices)


@handle_exception
@check_arguments
def multenterbox(msg='', fields: (list, tuple) = tuple(),
                 title='', values: (list, tuple) = tuple()):
    """
    展示一个多输入弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param fields: 输入项(列表类型,非必填) 例子:['奥迪','奔驰']
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :param  values: 输入值(列表类型,非必填) 例子:['奥迪','奔驰']
    :return: 返回输入的值(列表类型)
    """
    return send_to_oss_and_await('multenterbox', msg, title, fields, values)


@handle_exception
@check_arguments
def multpasswordbox(msg='', fields: (list, tuple) = tuple(), title=''):
    """
    展示一个多输入密码弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param fields: 输入项(列表类型,非必填) 例子:['奥迪','奔驰']
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :return: 返回输入的值(列表类型)
    """
    return send_to_oss_and_await('multpasswordbox', msg, title, fields=fields)


@handle_exception
def passwordbox(msg='', title=''):
    """
    展示一个输入密码弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :return: 返回输入的值(字符串类型)
    """
    return send_to_oss_and_await('passwordbox', msg, title)


@handle_exception
@check_arguments
def textbox(msg='', text='', title='', codebox: bool = True):
    """
    展示一个文本输入弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param text: 要输入的文本(文本类型,非必填) 例子:'你好'
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :param codebox: 是否以代码格式展示(bool类型,非必填) 例子:True
    :return: 返回输入弹框里的文本内容(字符串类型)
    """
    return send_to_oss_and_await('textbox', msg, title, text, codebox)


@handle_exception
def ynbox(msg='', title=''):
    """
    展示一个是/否选项弹框

    :param msg: 要展示的信息(文本类型,非必填) 例子:'你好'
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :return: 返回选中的选项(bool类型)
    """
    return send_to_oss_and_await('ynbox', msg, title)


@handle_exception
def codebox(msg='', text='', title=''):
    """
    展示一个代码输入弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param text: 要输入的文本(文本类型,非必填) 例子:'你好'
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :return: 返回输入的代码(字符串类型)
    """
    return send_to_oss_and_await('codebox', msg, title, text)


@handle_exception
def intbox(msg=''):
    """
    展示一个整数输入弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'请输入整数'
    :return: 返回输入的数字(int类型)
    """
    return send_to_oss_and_await('intbox', msg)


@handle_exception
def integerbox(msg=''):
    """
    展示一个整数输入弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :return: 返回输入的数字(int类型)
    """
    return send_to_oss_and_await('integerbox', msg)


@handle_exception
def tablebox(msg='', datalist=(), list=None):
    """
    展示一个表格弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param datalist: 要展示的数据(二维列表,非必填) 例子:[['星期一', '晴天'], ['星期二', '小雨']]
    :param list: 表格表头(列表类型,非必填) 例子:['星期','天气']
    :return: 点击弹框的'确认'按钮返回字符串'ok'，点击关闭按钮返回 None
    """
    header = list
    list = type([])

    illegal_arguments = []

    if (not isinstance(datalist, list)
            or not all(isinstance(item, list)
                       for item in datalist)):
        illegal_arguments.append('datalist')

    if header is not None and not isinstance(header, list):
        illegal_arguments.append('list')

    if illegal_arguments:
        raise ParameterTypeError('tablebox', '、'.join(illegal_arguments))

    # List[List[?]] -> List[List[str]]
    datalist = [[str(item) for item in data] for data in datalist]
    if header is not None:
        header = [str(item) for item in header]

    max_len = len(header) if header is not None else 0
    for data in datalist:
        max_len = max(max_len, len(data))

    if header is not None:
        while len(header) < max_len:
            header.append('')
    for data in datalist:
        while len(data) < max_len:
            data.append('')

    return send_to_oss_and_await('tablebox', msg, datalist, header)
