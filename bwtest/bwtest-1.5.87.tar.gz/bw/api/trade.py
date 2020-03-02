# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

import six
from typing import Text, List, Dict, NoReturn, Any, Union

from bw.csdk.cpp_sdk import py_bwi_place_order, py_bwi_get_unfinished_orders, py_bwi_get_orders, py_bwi_get_positions,\
    py_bwi_cancel_all_orders, py_bwi_close_all_positions, py_bwi_cancel_order, py_bwi_get_execution_reports,\
        py_bwi_get_sector,COrder
    
from bw.enum import OrderQualifier_Unknown, OrderDuration_Unknown
from bw.model.storage import context
from bw.yy.data import *

from bw.yy.account import Order, OrderStyle_Volume, OrderStyle_Value, OrderStyle_Percent, \
    OrderStyle_TargetVolume, OrderStyle_TargetValue, OrderStyle_TargetPercent, ExecRpts,PositionSide_Unknown, \
PositionSide_Long,PositionSide_Short,OrderSide_Unknown ,OrderSide_Buy ,OrderSide_Sell



from bw.utils import load_to_list, datetime2timestamp


def _inner_place_order(o):
    # type: (Order) ->List[Dict[Text, Any]]
    """
    下单并返回order的信息. 同步调用, 在下单返回的order,错误返回空的list
    """
    # # 在回测模式且wait_group=True时, 设置这个created_at, 也就是通知c底层要根据这个时间设置price
    if context.is_backtest_model() and context.has_wait_group:
        o.created_at =  datetime2timestamp( context.now ) *1000  # millisec --->cppsdk cover
    # print(o)
    
    result = py_bwi_place_order(o)
    
    return result


def order_volume(symbol, volume, side, order_type, position_effect,
                 price=0, order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown, account=''):
    # type: (Text, float, int, int, int, float, int, int, Text) ->List[Dict[Text, Any]]
    """
    按指定量委托
    """
    order_style = OrderStyle_Volume
    # print('order_volume start')
    account_id = get_account_id(account)
    # print('account=',account,'account_id=',account_id)

    o = COrder()
    o.symbol = symbol
    o.volume = (volume)
    o.price = price
    o.side = side
    o.order_type = order_type
    o.position_effect = position_effect
    o.order_style = order_style
    o.order_qualifier = order_qualifier
    o.order_duration = order_duration
    o.account_id = account_id

    return _inner_place_order(o)


def order_value(symbol, value, side, order_type, position_effect,
                price=0, order_duration=OrderDuration_Unknown, 
                order_qualifier=OrderQualifier_Unknown, account=''):
    # type:(Text, float, int, int, int, float, int, int, Text) ->List[Dict[Text, Any]]
    """
    按指定价值委托
    """
    order_style = OrderStyle_Value
    account_id = get_account_id(account)

    o = COrder()
    o.symbol = symbol
    o.value = value
    o.price = price
    o.side = side
    o.order_type = order_type
    o.position_effect = position_effect
    o.order_style = order_style
    o.order_qualifier = order_qualifier
    o.order_duration = order_duration
    o.account_id = account_id

    return _inner_place_order(o)


def order_percent(symbol, percent, side, order_type, position_effect,
                  price=0, order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown, account=''):
    # type: (Text, float, int, int, int, float, int, int, Text)->List[Dict[Text, Any]]
    """
    按指定比例委托
    """
    order_style = OrderStyle_Percent
    account_id = get_account_id(account)

    o = COrder()
    o.symbol = symbol
    o.percent = percent
    o.price = price
    o.side = side
    o.order_type = order_type
    o.position_effect = position_effect
    o.order_qualifier = order_qualifier
    o.order_duration = order_duration
    o.order_style = order_style
    o.account_id = account_id

    return _inner_place_order(o)


def order_target_volume(symbol, volume, position_side, order_type, price=0, order_duration=OrderDuration_Unknown,
                        order_qualifier=OrderQualifier_Unknown, account=''):
    # type: (Text, float, int, int, float, int, int, Text) ->List[Dict[Text, Any]]
    """
    调仓到目标持仓量
    """
    order_style = OrderStyle_TargetVolume

    account_id = get_account_id(account)
    o = COrder()
    o.symbol = symbol
    o.target_volume = volume
    o.price = price
    o.position_side = position_side
    o.order_type = order_type
    o.order_qualifier = order_qualifier
    o.order_duration = order_duration
    o.order_style = order_style
    o.account_id = account_id
    if position_side == PositionSide_Unknown:
        raise Exception('持仓类型不正确!')
    o.side = OrderSide_Buy if position_side==PositionSide_Long else OrderSide_Sell


    return _inner_place_order(o)


def order_target_value(symbol, value, position_side, order_type, price=0,
                       order_duration=OrderDuration_Unknown,
                        order_qualifier=OrderQualifier_Unknown, account=''):
    # type: (Text, float, int, int, float, int, int, Text) ->List[Dict[Text, Any]]
    """
    调仓到目标持仓额
    """
    order_style = OrderStyle_TargetValue
    account_id = get_account_id(account)

    o = COrder()
    o.symbol = symbol
    o.target_value = value
    o.price = price
    o.position_side = position_side
    o.order_type = order_type
    o.order_qualifier = order_qualifier
    o.order_duration = order_duration
    o.order_style = order_style
    o.account_id = account_id
    if position_side == PositionSide_Unknown:
        raise Exception('持仓类型不正确!')
    o.side = OrderSide_Buy if position_side==PositionSide_Long else OrderSide_Sell
    # o.side = position_side== PositionSide.

    return _inner_place_order(o)


def order_target_percent(symbol, percent, position_side, order_type, price=0, order_duration=OrderDuration_Unknown,
                         order_qualifier=OrderQualifier_Unknown, account=''):
    # type: (Text, float, int, int, float, int, int, Text) ->List[Dict[Text, Any]]
    """
    调仓到目标持仓比例
    """
    order_style = OrderStyle_TargetPercent
    account_id = get_account_id(account)

    o = COrder()
    o.symbol = symbol
    o.target_percent = percent
    o.price = price
    o.position_side = position_side
    o.order_type = order_type
    o.order_qualifier = order_qualifier
    o.order_duration = order_duration
    o.order_style = order_style
    o.account_id = account_id
    if position_side == PositionSide_Unknown:
        raise Exception('持仓类型不正确!')
    o.side = OrderSide_Buy if position_side==PositionSide_Long else OrderSide_Sell

    return _inner_place_order(o)


def get_unfinished_orders():
    # type: ()->List[Dict[Text, Any]]
    """
    查询所有未结委托
    """
    unfinished_orders = []
    for account in six.itervalues(context.accounts):
        # print('-*'*50,account.id)
        result = py_bwi_get_unfinished_orders(account.id)
        if result:
            unfinished_orders.extend(result)

    return unfinished_orders


def get_orders():
    # type: () ->List[Dict[Text, Any]]
    """
    查询日内全部委托
    """
    all_orders = []
    for account in six.itervalues(context.accounts):
        result= py_bwi_get_orders(account.id)
        # print('*---'*20,len(result),account.id)
        if result:
            all_orders.extend(result)
    return all_orders

def get_positions():
    # type: () ->List[Dict[Text, Any]]
    """
    查询日内全部委托
    """
    all_pos = []
    for account in six.itervalues(context.accounts):
        result= py_bwi_get_positions(account.id)
        # print('*---'*20,len(result),account.id)
        if result:
            all_pos.extend(result)
    return all_pos

def order_cancel_all():
    # type: () ->NoReturn
    """
    撤销所有委托
    """
    py_bwi_cancel_all_orders()


def order_close_all():
    # type: () ->List[Dict[Text, Any]]
    """
    平当前所有可平持仓
    """
    py_bwi_close_all_positions()
    #return oder list
    return None


def order_cancel(wait_cancel_orders):
    # type: (Union[Dict[Text,Any], List[Dict[Text, Any]]]) ->NoReturn
    """
    撤销委托. 传入单个字典. 或者list字典. 每个字典包含key: cl_ord_id, account_id
    """
    wait_cancel_orders = load_to_list(wait_cancel_orders)

    py_bwi_cancel_order(wait_cancel_orders)


# def order_batch(order_infos,account=''):
#     """
#     批量委托接口
#     """

#     py_bwi_place_order()
#     res = Orders()
#     return res


def get_account_id(name_or_id):
    # type: (Text) ->Text
    for one in six.itervalues(context.accounts):
        if one.match(name_or_id):
            return one.id
    # print('not matched ',name_or_id)
    # 都没有匹配上, 等着后端去拒绝
    if  name_or_id.strip().__len__() == 0:
        return "DEFAULT"
    return name_or_id


def get_execution_reports():
    # type: () -> List[Dict[Text, Any]]
    """
    返回执行回报
    """
    reports = []
    for account in six.itervalues(context.accounts):
        req = account.id
        result = py_bwi_get_execution_reports(req)
        if result:
            reports.extend(result)
            
    return reports
