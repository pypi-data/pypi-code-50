# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import six

# Six 就是来解决这个烦恼的，这是一个专门用来兼容 Python 2 和 Python 3 的模块，
    # 它解决了诸如 urllib 的部分方法不兼容， str 和 bytes 类型不兼容等“知名”问题。
    # import six
    # six.PY2 #返回一个表示当前运行环境是否为python2的boolean值
    # six.PY3 #返回一个表示当前运行环境是否为python3的boolean值
    # six.integer_types # 在python2中，存在 int 和 long 两种整数类型；在python3中，仅存在一种类型int
    # six.string_types # 在python2中，使用的为basestring；在python3中，使用的为str
    # six.text_type # 在python2中，使用的文本字符的类型为unicode；在python3中使用的文本字符的类型为str
    # six.binary_type # 在python2中，使用的字节序列的类型为str；在python3中使用的字节序列的类型为bytes
    # from dingtalk.core.utils import to_binary, to_text


from aishow_model_app.core.utils import to_binary, to_text


class DingTalkException(Exception):

    def __init__(self, errcode, errmsg):
        """
        :param errcode: Error code
        :param errmsg: Error message
        """
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        _repr = 'Error code: {code}, message: {msg}'.format(
            code=self.errcode,
            msg=self.errmsg
        )

        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)

    def __repr__(self):
        _repr = '{klass}({code}, {msg})'.format(
            klass=self.__class__.__name__,
            code=self.errcode,
            msg=self.errmsg
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)


class DingTalkClientException(DingTalkException):
    """WeChat API client exception class"""
    def __init__(self, errcode, errmsg, client=None,
                 request=None, response=None):
        super(DingTalkClientException, self).__init__(errcode, errmsg)
        self.client = client
        self.request = request
        self.response = response


class InvalidSignatureException(DingTalkException):
    """Invalid signature exception class"""

    def __init__(self, errcode=-40001, errmsg='Invalid signature'):
        super(InvalidSignatureException, self).__init__(errcode, errmsg)


class InvalidCorpIdOrSuiteKeyException(DingTalkException):
    """Invalid app_id exception class"""

    def __init__(self, errcode=-40005, errmsg='Invalid CorpIdOrSuiteKey'):
        super(InvalidCorpIdOrSuiteKeyException, self).__init__(errcode, errmsg)
