# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from enum import Enum

#解释Enum
# Python——枚举（enum）
#     使用普通类直接实现枚举
# 　　在Python中，枚举和我们在对象中定义的类变量时一样的，每一个类变量就是一个枚举项，访问枚举项的方式为：类名加上类变量，像下面这样：
#
# class color():
#     YELLOW = 1
#     RED = 2
#     GREEN = 3
#     PINK = 4
#
# # 访问枚举项
# print(color.YELLOW)  # 1
# 　　虽然这样是可以解决问题的，但是并不严谨，也不怎么安全，比如：
# 　　1、枚举类中，不应该存在key相同的枚举项（类变量）
# 　　2、不允许在类外直接修改枚举项的值
#
# class color():
#     YELLOW = 1
#     YELLOW = 3  # 注意这里又将YELLOW赋值为3，会覆盖前面的1
#     RED = 2
#     GREEN = 3
#     PINK = 4
#
# # 访问枚举项
# print(color.YELLOW)  # 3
# # 但是可以在外部修改定义的枚举项的值，这是不应该发生的
# color.YELLOW = 99
# print(color.YELLOW)  # 99
# 解决方案：使用enum模块
# 　　enum模块是系统内置模块，可以直接使用import导入，但是在导入的时候，不建议使用import
# enum将enum模块中的所有数据都导入，一般使用的最多的就是enum模块中的Enum、IntEnum、unique这几项
#
# # 导入枚举类
# from enum import Enum
#
# # 继承枚举类
# class color(Enum):
#     YELLOW = 1
#     BEOWN = 1
#     # 注意BROWN的值和YELLOW的值相同，这是允许的，此时的BROWN相当于YELLOW的别名
#     RED = 2
#     GREEN = 3
#     PINK = 4
#
# class color2(Enum):
#     YELLOW = 1
#     RED = 2
#     GREEN = 3
#     PINK = 4
#
# 　　使用自己定义的枚举类：
# print(color.YELLOW)  # color.YELLOW
# print(type(color.YELLOW))  # <enum 'color'>
# print(color.YELLOW.value)  # 1
# print(type(color.YELLOW.value))  # <class 'int'>
# print(color.YELLOW == 1)  # False
# print(color.YELLOW.value == 1)  # True
# print(color.YELLOW == color.YELLOW)  # True
# print(color.YELLOW == color2.YELLOW)  # False
# print(color.YELLOW is color2.YELLOW)  # False
# print(color.YELLOW is color.YELLOW)  # True
# print(color(1))  # color.YELLOW
# print(type(color(1)))  # <enum 'color'>
# 　　注意事项如下：
# 　　1、枚举类不能用来实例化对象
# 　　2、访问枚举类中的某一项，直接使用类名访问加上要访问的项即可，比如color.YELLOW
# 　　3、枚举类里面定义的Key = Value，在类外部不能修改Value值，也就是说下面这个做法是错误的color.YELLOW = 2  # Wrong, can't reassign member
# 　　4、枚举项可以用来比较，使用 ==，或者is
# 　　5、导入Enum之后，一个枚举类中的Key和Value，Key不能相同，Value可以相，但是Value相同的各项Key都会当做别名，
# 　　6、如果要枚举类中的Value只能是整型数字，那么，可以导入IntEnum，然后继承IntEnum即可，注意，此时，如果value为字符串的数字，也不会报错：from enum import IntEnum
# 　　7、如果要枚举类中的key也不能相同，那么在导入Enum的同时，需要导入unique函数from enum import Enum, unique


class SuitePushType(Enum):
    """套件相关回调枚举"""
    CHECK_URL = "check_url"  # 校验url
    CHANGE_AUTH = "change_auth"  # 授权变更
    SUITE_TICKET = "suite_ticket"  # 套件ticket     ticket 票; 券; 车票; 戏票; 入场券; 奖券;标签
    TMP_AUTH_CODE = "tmp_auth_code"  # 临时授权码
    SUITE_RELIEVE = "suite_relieve"  # 解除授权
    CHECK_CREATE_SUITE_URL = "check_create_suite_url"  # 校验创建套件时候的url
    CHECK_UPDATE_SUITE_URL = "check_update_suite_url"  # 校验更改套件时候的url
    CHECK_SUITE_LICENSE_CODE = "check_suite_license_code"  # 校验序列号
    MARKET_BUY = "market_buy"  # 用户购买下单
    ORG_MICRO_APP_STOP = "org_micro_app_stop"  # 企业逻辑停用微应用
    ORG_MICRO_APP_REMOVE = "org_micro_app_remove"  # 企业物理删除微应用
    ORG_MICRO_APP_RESTORE = "org_micro_app_restore"  # 企业逻辑启用微应用
