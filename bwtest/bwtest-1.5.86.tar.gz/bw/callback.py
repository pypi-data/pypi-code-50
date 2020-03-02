# coding=utf-8
"""
回调任务分发
"""
from __future__ import unicode_literals, print_function, absolute_import

import collections
import datetime
import time

import six
from typing import Any, Dict, Text, List, Set, NoReturn

from bw.constant import CALLBACK_TYPE_TICK, CALLBACK_TYPE_BAR, \
    CALLBACK_TYPE_SCHEDULE, CALLBACK_TYPE_EXECRPT, \
    CALLBACK_TYPE_ORDER, CALLBACK_TYPE_INDICATOR, CALLBACK_TYPE_CASH, \
    CALLBACK_TYPE_POSITION, CALLBACK_TYPE_PARAMETERS, CALLBACK_TYPE_ERROR, \
    CALLBACK_TYPE_TIMER, CALLBACK_TYPE_BACKTEST_FINISH, CALLBACK_TYPE_STOP, \
    CALLBACK_TYPE_TRADE_CONNECTED, CALLBACK_TYPE_DATA_CONNECTED, \
    CALLBACK_TYPE_ACCOUNTSTATUS, CALLBACK_TYPE_DATA_DISCONNECTED, CALLBACK_TYPE_TRADE_DISCONNECTED, \
    CALLBACK_TYPE_INIT,BarLikeDict2, ObjectLikeDict

from bw.csdk.cpp_sdk import py_bwi_now_plus

from bw.enum import MODE_BACKTEST, MODE_LIVE
from bw.model import DictLikeExecRpt, DictLikeOrder, DictLikeIndicator, DictLikeParameter, DictLikeAccountStatus, \
    DictLikeConnectionStatus, DictLikeError
from bw.model.storage import Context, context, BarWaitgroupInfo, BarSubInfo

from bw.yy.data import Tick, Bar, Quote
from bw.yy.account import ExecRpt, Order, Cash, Position, AccountStatus
from bw.yy.performance import Indicator
# from bw.yy.rtconf import Parameters

from bw.utils import bwsdklogger, beijing_tzinfo, timestamp2bj_datetime,timestamp2datetime,\
    DictLikeObject,ObjectLikeDict


def init_callback(data):
    context.bar_data_set.clear()  # 清空之前的
    if context.init_fun is not None:
        context.init_fun(context)


def tick_callback_new(data):
    tick = Tick(data)
    tick.FromFmt(data)
    if len(tick.quotes) < 5:
        for _ in range(len(tick.quotes), 5):
            zero_val = {'bid_p': 0, 'bid_v': 0, 'ask_p': 0, 'ask_v': 0}
            tick.quotes.append(zero_val)

    ticknew = {
        'quotes': tick.quotes,
        'symbol': tick.symbol,
        'created_at': timestamp2bj_datetime(tick.created_at),
        'price': tick.price,
        'open': tick.open,
        'high': tick.high,
        'low': tick.low,
        'cum_volume': tick.cum_volume,
        'cum_amount': tick.cum_amount,
        'cum_position': tick.cum_position,
        'last_amount': tick.last_amount,
        'last_volume': tick.last_volume,
        'trade_type': tick.trade_type,
        'receive_local_time': time.time(),  # 收到时的本地时间秒数
    }
    ticknn = ObjectLikeDict(ticknew)
    # print(ticknn)
    tick_callback(ticknn)


def tick_callback(data):
    tick = data  # type: ObjectLikeDict
    symbol = tick['symbol']
    # print(symbol)
    if symbol not in context.tick_sub_symbols:
        bwsdklogger.debug("tick data symbol=%s 不在订阅列表里, 跳过不处理", symbol)
        return

    if symbol not in context.tick_data_cache:
        bwsdklogger.debug("tick data's symbol= %s 在context.tick_data_cache key不存在, 加个key, deque长度为:%d", symbol,
                          context.max_tick_data_count)
        context.tick_data_cache[symbol] = collections.deque(maxlen=context.max_tick_data_count)

    context.tick_data_cache[symbol].appendleft(tick)
    if context.on_tick_fun is not None:
        context.on_tick_fun(context, tick)


# 回测模式下前一个eob的时间
pre_eob_in_backtest = None  # type: datetime.datetime
# 回测模式且wait_group下的bar集合. 以 frequency 作为 key
bars_in_waitgroup_backtest = collections.defaultdict(list)  # type: Dict[Text, List[BarLikeDict2]]
# 实时模式且wait_group下的bar集合  以 frequency 作为 一级key, eob做为二级key
bars_in_waitgroup_live = dict()  # type:  Dict[Text, Dict[datetime.datetime, List[BarLikeDict2]]]


def bar_callback_new(data):
    # print('---------------------------bar _call back new')
    bar = Bar(data)
    bar.FromFmt(data)
    barnew = {
        'symbol': bar.symbol,
        'eob': timestamp2bj_datetime(bar.eob),
        'bob': timestamp2bj_datetime(bar.bob),
        'open': float(bar.open),
        'close': float(bar.close),
        'high': float(bar.high),
        'low': float(bar.low),
        'volume': bar.volume,
        'amount': bar.amount,
        'pre_close': bar.pre_close,
        'position': bar.position,
        'frequency': bar.frequency,
        'receive_local_time': time.time(),  # 收到时的本地时间秒数
    }
    # print(barnew)
    # t = 
    barnn = ObjectLikeDict(barnew)
    # print('&'*28,barnn['symbol'],barnn.data)
    bar_callback(barnn)
    pass


def bar_callback(databar):
    # print('-------------------------------bar-call_back')
    bar =databar
    # print(bar)
    global pre_eob_in_backtest, bars_in_waitgroup_backtest, bars_in_waitgroup_live
    symbol, frequency = bar['symbol'], bar['frequency']  # type: Text, Text
    # print(symbol,frequency)
    if BarSubInfo(symbol, frequency) not in context.bar_sub_infos:
        bwsdklogger.debug("bar data symbol=%s frequency=%s 不在订阅列表里, 跳过不处理", symbol, frequency)
        # print('--------------',symbol,frequency)
        # print('juran')
        return
    
    k = symbol + "_" + frequency

    # wait_group = True的情况下, 就先不要放入, 不然第一个symbol得到的数据跟别的symbol的数据对不齐
    if not context.has_wait_group:
        context.bar_data_cache[k].appendleft(bar)

    if context.on_bar_fun is None:
        return

    # 没有wait_group的情况, 那就直接发了
    if not context.has_wait_group:
        context.on_bar_fun(context, [bar, ])
        return

    # wait_group = True, 但是股票不在waitgroup的列表里时, 直接发了.
    # 在调用完 on_bar_fun 后, 在把数据放入到bar_data_cache里
    barwaitgroupinfo = context.bar_waitgroup_frequency2Info.get(frequency, BarWaitgroupInfo(frequency, 0))
    if not barwaitgroupinfo.is_symbol_in(symbol):
        bwsdklogger.debug('wait_group = True, 但是股票不在waitgroup的列表里时, 直接发了, symbol=%s, frequency=%s', symbol, frequency)
        context.on_bar_fun(context, [bar, ])
        context._add_bar2bar_data_cache(k, bar)
        return

    eob = bar['eob']  # type: datetime.datetime

    if context.mode == MODE_BACKTEST:  # 处理回测模式下, wait_group = True
        # 在回测模式下, 数据都是按顺序组织好的, 所以可以认为到下一个时间点时, 就把所有的数据统一放出来就好了
        if pre_eob_in_backtest is None:
            context._temporary_now = context.now #datetime.datetime.fromtimestamp(context.now/1000).replace(tzinfo=beijing_tzinfo)
            pre_eob_in_backtest = eob
            bars_in_waitgroup_backtest[frequency].append(bar)
            context._add_bar2bar_data_cache(k, bar)
            return

        if pre_eob_in_backtest == eob:
            bars_in_waitgroup_backtest[frequency].append(bar)
            context._add_bar2bar_data_cache(k, bar)
            return

        if pre_eob_in_backtest < eob:  # 说明是下一个时间点了
            for bs in six.itervalues(bars_in_waitgroup_backtest):
                context.on_bar_fun(context, bs)

            context._add_bar2bar_data_cache(k, bar)

            pre_eob_in_backtest = eob
            context._temporary_now = context.now #  datetime.datetime.fromtimestamp(context.now/1000).replace(tzinfo=beijing_tzinfo) 
            #datetime.datetime.fromtimestamp(context.now).replace(tzinfo=beijing_tzinfo)
            bars_in_waitgroup_backtest.clear()
            bars_in_waitgroup_backtest[frequency].append(bar)
            return

        return

    if context.mode == MODE_LIVE:  # 处理实时模式下, wait_group = True
        
        bwsdklogger.warning("实时模式下暂时不支持,数据并没有运行")
        if frequency not in bars_in_waitgroup_live:
            bars_in_waitgroup_live[frequency] = dict()

        # 以eob做为key值, bar做为value值. 二级dict
        eob_bar_dict = bars_in_waitgroup_live[frequency]  # type: Dict[datetime.datetime, List[BarLikeDict2]]
        if eob not in eob_bar_dict:
            eob_bar_dict[eob] = [bar]
        else:
            eob_bar_dict[eob].append(bar)

        # 检查一下是否全部都到了. 到了的话触发一下
        if len(barwaitgroupinfo) == len(eob_bar_dict[eob]):
            bwsdklogger.debug("实时模式下, wait_group的bar都到齐了, 触发on_bar. eob=%s", eob)
            context.bar_data_cache[k].appendleft(bar)
            context.on_bar_fun(context, eob_bar_dict[eob])
            del eob_bar_dict[eob]
        else:
            context.bar_data_cache[k].appendleft(bar)

        return


def schedule_callback(data):
    # python 3 传过来的是bytes 类型， 转成str
    if isinstance(data, bytes):
        data = bytes.decode(data)
    # print('-'*100,data)
    schedule_func = context.inside_schedules.get(data)
    if not schedule_func:
        # print('schedule_callback---------none----call')
        return
    schedule_func(context)


def _or_not_none(a, b):
    # type: (Any, Any) -> bool
    """
    两个中有一个不为None
    """
    return a is not None or b is not None


def excerpt_callback(data):
    """data indicator"""
    if context.on_execution_report_fun is not None:
        excerpt = ExecRpt()
        excerpt.FromFmt(data)
        context.on_execution_report_fun(context, excerpt)


def order_callback(data):
    if context.on_order_status_fun is not None:
        order = Order()
        order.FromFmt(data)
        context.on_order_status_fun(context, order)


def indicator_callback(data):
    if context.on_backtest_finished_fun is not None:
        indicator = Indicator()
        indicator.FromFmt(data)
        context.on_backtest_finished_fun(context, indicator)
        return


def cash_callback(data):
    cash = Cash(data)
    account_id = cash['account_id']
    accounts = context.accounts
    accounts[account_id].cash = cash


def position_callback(data):
    position = Position()
    position.FromFmt(data)
    symbol = position['symbol']
    side = position['side']
    account_id = position['account_id']
    accounts = context.accounts
    position_key = '{}.{}'.format(symbol, side)
    accounts[account_id].inside_positions[position_key] = position

    if not position.get('volume'):
        if accounts[account_id].inside_positions.get(position_key):
            return accounts[account_id].inside_positions.pop(position_key)


def parameters_callback(data):
    if context.on_parameter_fun is not None:
        context.on_parameter_fun(context, data)


def default_err_callback(ctx, code, info):
    # type: (Context, Text, Text) -> NoReturn
    if code in ('81299', '81298'):
        bwsdklogger.warning(
            '行情重连中..., error code=%s, info=%s. 可用on_error事件处理', code, info
        )
    else:
        bwsdklogger.warning(
            '发生错误, 调用默认的处理函数, error code=%s, info=%s.  你可以在策略里自定义on_error函数接管它. 类似于on_tick',
            code, info
        )


def err_callback(data):
    """
    遇到错误时回调, 错误代码跟错误信息的对应关系参考
    """
    if context.on_error_fun is None:
        context.on_error_fun = default_err_callback

    try:
        data_unicode = data.decode('utf8')
        sparr = data_unicode.split('|', 1)
        if len(sparr) == 1:
            code, info = "code解析不出来", sparr[0]
        else:
            code, info = sparr
        if context.on_error_fun is not None:
            context.on_error_fun(context, code, info)
    except Exception as e:
        bwsdklogger.exception("字符编码解析错误", e)
        if context.on_error_fun is not None:
            context.on_error_fun(context, "81011", data)


# 已超时触发过的eob集合, 原则上是触发过的, 即可后面在收到数据也不再次触发
already_fire_timeout_eobs = set()  # type: Set[datetime.datetime]


def timer_callback(data):
    global bars_in_waitgroup_live, already_fire_timeout_eobs
    if (context.on_bar_fun is not None) and context.has_wait_group and context.is_live_model():
        # 这里处理实时模式下wait_group=true时, on_bar超时触发
        # 比较逻辑是: 取本地时间, 然后跟相同的eob的bars里的第1个bar的 receive_local_time (接收到时的本地时间) 相比
        cur_now_s = time.time()
        must_del_keys = []
        for frequency, eob_tick_dict in six.iteritems(bars_in_waitgroup_live):
            barwaitgroupinfo = context.bar_waitgroup_frequency2Info.get(frequency, None)
            if barwaitgroupinfo is not None:
                timeout_seconds = barwaitgroupinfo.timeout_seconds
                for eob_time in list(six.iterkeys(eob_tick_dict)):
                    first_bar = eob_tick_dict[eob_time][0]  # 这个eob下的收到的第1个bar
                    delta_second = cur_now_s - first_bar['receive_local_time']  # type: float
                    if delta_second >= timeout_seconds:
                        if eob_time in already_fire_timeout_eobs:
                            bwsdklogger.debug(
                                'frequency=%s eob=%s timeout_seconds=%d, 已超时触发过, 后面又收到数据, 不进行触发',
                                frequency, eob_time
                            )
                            del eob_tick_dict[eob_time]
                            continue

                        bwsdklogger.info(
                            "frequency=%s eob=%s timeout_seconds=%d 已超时了超时秒数=%s, 触发on_bar",
                            frequency, eob_time, timeout_seconds, delta_second
                        )
                        context.on_bar_fun(context, eob_tick_dict[eob_time])
                        del eob_tick_dict[eob_time]
                        already_fire_timeout_eobs.add(eob_time)
            else:
                # 说明有些 frequency 已经退订了
                bwsdklogger.debug("frequency =%s 已全部退订", frequency)
                must_del_keys.append(frequency)

        if must_del_keys:
            for k in must_del_keys:
                del bars_in_waitgroup_live[k]
        return


def backtest_finish_callback(data):
    global pre_eob_in_backtest, bars_in_waitgroup_backtest
    # 在回测结束前, 把之前累积的bar给放出来
    if bars_in_waitgroup_backtest:
        for bs in six.itervalues(bars_in_waitgroup_backtest):
            context.on_bar_fun(context, bs)

    pre_eob_in_backtest = None
    bars_in_waitgroup_backtest = collections.defaultdict(list)
    context._temporary_now = None
    context.bar_data_set.clear()  # 清空之前的
    context.bar_data_cache.clear()
    context.tick_data_cache.clear()
    context.max_tick_data_count = 1
    context.max_bar_data_count = 1


def stop_callback(data):
    if context.on_shutdown_fun is not None:
        context.on_shutdown_fun(context)

    from bw.api import stop
    # print("!~~~~~~~~~~~!停止策略!~~~~~~~~~~~!")
    stop()


def trade_connected_callback():
    bwsdklogger.debug("连接交易服务成功")
    if context.on_trade_data_connected_fun is not None:
        context.on_trade_data_connected_fun(context)


def data_connected_callback():
    bwsdklogger.debug("连接行情服务成功")
    if context.on_market_data_connected_fun is not None:
        context.on_market_data_connected_fun(context)


def account_status_callback(data):
    if context.on_account_status_fun is not None:
        account_status = AccountStatus()
        account_status.FromFmt(data)

        account_status_dict = DictLikeAccountStatus()
        account_status_dict['account_id'] = account_status.account_id
        account_status_dict['account_name'] = account_status.account_name

        status_dict = DictLikeConnectionStatus()
        account_status_dict['status'] = status_dict
        if account_status.status is not None:
            status_dict['state'] = account_status.status.state
            error_dict = DictLikeError()
            status_dict['error'] = error_dict
            if account_status.status.error is not None:
                error_dict['code'] = account_status.status.error.code
                error_dict['type'] = account_status.status.error.type
                error_dict['info'] = account_status.status.error.info

        context.on_account_status_fun(context, account_status_dict)


def data_disconnected_callback():
    if context.on_market_data_disconnected_fun is not None:
        context.on_market_data_disconnected_fun(context)


def trade_disconnected_callback():
    if context.on_trade_data_disconnected_fun is not None:
        context.on_trade_data_disconnected_fun(context)


def callback_controller(msg_type, data):
    """
    回调任务控制器
    """
    try:
        # print('&'*20,msg_type)
        # python 3 传过来的是bytes 类型， 转成str
        if isinstance(msg_type, bytes):
            msg_type = bytes.decode(msg_type)

        # sprint('now','&'*20,msg_type)

        if msg_type == CALLBACK_TYPE_TICK:
            # print('-'*20,'tick lai le ')
            return tick_callback_new(data)

        elif msg_type == CALLBACK_TYPE_BAR:
            # print('-'*20,'bar lai le ')
            return bar_callback_new(data)

        elif msg_type == CALLBACK_TYPE_INIT:
            return init_callback(data)

        elif msg_type == CALLBACK_TYPE_SCHEDULE:
            # print('-'*20,'lai le ')
            return schedule_callback(data)

        elif msg_type == CALLBACK_TYPE_ERROR:
            return err_callback(data)

        elif msg_type == CALLBACK_TYPE_TIMER:
            # print('-'*20,'CALLBACK_TYPE_TIMER lai le ')
            return timer_callback(data)

        elif msg_type == CALLBACK_TYPE_EXECRPT:
            return excerpt_callback(data)

        elif msg_type == CALLBACK_TYPE_ORDER:
            return order_callback(data)

        elif msg_type == CALLBACK_TYPE_INDICATOR:
            # print('*'*20,'now in')
            return indicator_callback(data)

        elif msg_type == CALLBACK_TYPE_CASH:
            return cash_callback(data)

        elif msg_type == CALLBACK_TYPE_POSITION:
            return position_callback(data)

        elif msg_type == CALLBACK_TYPE_PARAMETERS:
            return parameters_callback(data)

        elif msg_type == CALLBACK_TYPE_BACKTEST_FINISH:
            return backtest_finish_callback(data)

        elif msg_type == CALLBACK_TYPE_STOP:
            return stop_callback(data)

        elif msg_type == CALLBACK_TYPE_TRADE_CONNECTED:
            return trade_connected_callback()

        elif msg_type == CALLBACK_TYPE_TRADE_DISCONNECTED:
            return trade_disconnected_callback()

        elif msg_type == CALLBACK_TYPE_DATA_CONNECTED:
            return data_connected_callback()

        elif msg_type == CALLBACK_TYPE_DATA_DISCONNECTED:
            return data_disconnected_callback()

        elif msg_type == CALLBACK_TYPE_ACCOUNTSTATUS:
            return account_status_callback(data)

        bwsdklogger.warn("没有处理消息:%s的处理函数", msg_type)

    except SystemExit:
        bwsdklogger.debug("callback_controller^^--------------SystemExit--------------^^")
        from bw.api import stop
        stop()

    except BaseException as e:
        bwsdklogger.exception("^^--------------遇到exception--------------^^")
        from bw.api import stop
        stop()
