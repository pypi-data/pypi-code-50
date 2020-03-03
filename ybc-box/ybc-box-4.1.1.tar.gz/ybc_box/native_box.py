import sys

import easygui as eg
from ybc_exception import exception_handler

from ybc_commons.context import check_arguments

handle_exception = exception_handler('ybc_box')


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
    return eg.buttonbox(msg, title, list(choices))


@handle_exception
@check_arguments
def choicebox(msg='', choices: (list, tuple) = tuple(), title=''):
    return eg.choicebox(msg, title, list(choices))


@handle_exception
@check_arguments
def enterbox(msg='', image: (str, list, tuple) = None, title='', default=''):
    """
    展示一个输入弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param image: 要展示的图片名(图片类型,必填) 例子:'1.jpg'
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :param default: 输入框预留文字(文本类型,非必填) 例子:'你好'
    :return: 返回在弹框中输入的文本(字符串类型)
    """
    return eg.enterbox(msg, title, image=image, default=default)


@handle_exception
def fileopenbox(msg='', title=''):
    """
    展示一个可以选择文件的弹框

    :param msg: 要展示的信息(文本类型,非必填) 例子:'你好'
    :param title: 弹框标题(文本类型,非必填) 例子:'你好'
    :return: 返回用户所选择文件的路径(字符串类型)
    """
    res = eg.fileopenbox(msg, title)
    return _adapt_path(res) if res else None


@handle_exception
@check_arguments
def indexbox(msg='', choices: (list, tuple) = tuple(), title=''):
    return eg.indexbox(msg, title, list(choices))


@handle_exception
@check_arguments
def msgbox(msg='', image: (str, list, tuple) = None, audio: str = ''):
    """
    展示一个消息弹框

    :param msg: 要展示的信息(文本类型,必填) 例子:'你好'
    :param image: 要展示的图片的文件名(文本类型或列表,非必填) 例子:'1.jpg'
    :param audio: 要播放的音频文件的名字(音频类型,非必填) 例子:'1.mp3'
    :return: 点击弹框的 ok 按钮返回字符串'ok'，点击关闭按钮返回 None
    """
    if isinstance(msg, (dict, list, tuple)):
        msg = str(msg)[1:-1]
    elif isinstance(msg, bool):
        msg = '1' if msg else '0'
    else:
        msg = str(msg)

    return eg.msgbox(msg, image=image)


@handle_exception
@check_arguments
def multchoicebox(msg='', choices: (list, tuple) = tuple(), title=''):
    return eg.multchoicebox(msg, title, list(choices))


@handle_exception
@check_arguments
def multenterbox(msg='', fields: (list, tuple) = tuple(),
                 title='', values: (list, tuple) = tuple()):
    return eg.multenterbox(msg, title, list(fields), list(values))


@handle_exception
@check_arguments
def multpasswordbox(msg='', fields: (list, tuple) = tuple(), title=''):
    return eg.multpasswordbox(msg, title, fields=list(fields))


@handle_exception
def passwordbox(msg='', title=''):
    return eg.passwordbox(msg, title)


@handle_exception
@check_arguments
def textbox(msg='', text='', title='', codebox: bool = True):
    return eg.textbox(msg, title, text, codebox)


@handle_exception
def ynbox(msg='', title=''):
    return eg.ynbox(msg, title)


@handle_exception
def codebox(msg='', text='', title=''):
    return eg.codebox(msg, title, text)


@handle_exception
def intbox(msg=''):
    return eg.integerbox('intbox', msg, lowerbound=None, upperbound=None)


@handle_exception
def integerbox(msg=''):
    return eg.integerbox('integerbox', msg, lowerbound=None, upperbound=None)


@handle_exception
def tablebox(msg='', datalist=(), list=None):
    print("暂不支持 ybc_box.tablebox 方法")
