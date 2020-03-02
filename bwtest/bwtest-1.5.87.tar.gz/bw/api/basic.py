# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals

import collections
import os
import sys
from importlib import import_module
from optparse import OptionParser

import six
from typing import Text, List, Dict, NoReturn, Any

import time


from datetime import date, datetime, timedelta, tzinfo

from bw.__version__ import __version__
from bw.callback import callback_controller
from bw.constant import DATA_TYPE_TICK, SCHEDULE_INFO

from bw.yy.data import Tick, Bar, Quote,Trade,Timestamp

from bw.csdk.cpp_sdk import py_bwi_current, py_bwi_schedule, py_bwi_set_data_callback, py_bwi_set_strategy_id, \
    py_bwi_set_mode, py_bwi_set_backtest_config, py_bwi_subscribe, py_bwi_set_token, py_bwi_unsubscribe, \
    py_bwi_log, py_bwi_strerror, py_bwi_set_user_token,py_bwi_set_pipe,py_bwi_set_srv_cache,\
    py_bwi_run, py_bwi_set_serv_addr, py_bwi_init, py_bwi_poll, py_bwi_get_c_version, py_bwi_set_apitoken,\
        py_bwi_set_cache

from bw.enum import MODE_UNKNOWN, ADJUST_NONE, MODE_BACKTEST, MODE_LIVE, ADJUST_POST, ADJUST_PREV
from bw.model.storage import context, BarSubInfo, BarWaitgroupInfo


from bw.utils import load_to_list, load_to_second, BwSymbols, bwsdklogger,\
timestamp2bj_datetime,timestamp2datetime

running = True


def _unsubscribe_all():
    context.bar_sub_infos.clear()
    context.tick_sub_symbols.clear()
    context.bar_waitgroup_frequency2Info.clear()
    context.bar_data_cache.clear()
    context.tick_data_cache.clear()
    context.max_tick_data_count = 1
    context.max_bar_data_count = 1


def set_token(usr,pwd):
    # type: (Text) ->NoReturn
    """
    设置用户的token，用于身份认证
    """
    py_bwi_set_token(usr,pwd)
    context.token = str('bearer {}'.format(usr))

def set_srv_cache(m):
    # type: (Text) ->NoReturn
    py_bwi_set_srv_cache(m)


def get_version():
    # type: () ->Text
    return __version__


def subscribe(symbols, frequency='1d', count=1, wait_group=False, wait_group_timeout='10s', unsubscribe_previous=False):
    # type:(BwSymbols, Text, int, bool, Text, bool) ->NoReturn
    """
    订阅行情，可以指定symbol， 数据滑窗大小，以及是否需要等待全部代码的数据到齐再触发事件。
    wait_group: 是否等待全部相同频度订阅的symbol到齐再触发on_bar事件。
    一个 frequency, 只能有一个 wait_group_timeout 也就是说如果后面调用该函数时, 
    相同的frequency, 但是 wait_group_timeout 不同,则 wait_group_timeout 被忽略.
    同时要注意, 一个symbol与frequency组合, 只能有一种wait_group, 即wait_group要么为true, 要么为false
    """
    # frequency = adjust_frequency(frequency)

    symbols = load_to_list(symbols)

    symbols_str = ','.join(symbols)
    py_bwi_subscribe(symbols_str, frequency, unsubscribe_previous)

    # print('*'*23,symbols_str,frequency)

    if unsubscribe_previous:
        _unsubscribe_all()

    if frequency == DATA_TYPE_TICK:
        if context.max_tick_data_count < count:
            context.max_tick_data_count = count
        for sy in symbols:
            context.tick_data_cache[sy] = collections.deque(maxlen=count)
            context.tick_sub_symbols.add(sy)
        return

    # 处理订阅bar的情况
    context._set_onbar_waitgroup_timeout_check()
    wait_group_timeoutint = load_to_second(wait_group_timeout)
    if context.max_bar_data_count < count:
        context.max_bar_data_count = count
    for sy in symbols:
        context.bar_data_cache["{}_{}".format(sy, frequency)] = collections.deque(maxlen=count)
        barsubinfo = BarSubInfo(sy, frequency)
        if barsubinfo not in context.bar_sub_infos:
            context.bar_sub_infos.add(barsubinfo)
            if wait_group:
                if frequency not in context.bar_waitgroup_frequency2Info:
                    context.bar_waitgroup_frequency2Info[frequency] = BarWaitgroupInfo(frequency, wait_group_timeoutint)
                context.bar_waitgroup_frequency2Info[frequency].add_one_symbol(sy)
        else:
            bwsdklogger.debug("symbol=%s frequency=%s 已订阅过", sy, frequency)
            continue


def unsubscribe(symbols, frequency='1d'):
    # type: (BwSymbols, Text) ->NoReturn
    """
    unsubscribe - 取消行情订阅

    取消行情订阅，默认取消所有已订阅行情
    """
    symbols = load_to_list(symbols)
    symbols_str = ','.join(symbols)
    # frequency = adjust_frequency(frequency)

    status = py_bwi_unsubscribe(symbols_str, frequency)

    if symbols_str == '*':
        _unsubscribe_all()
        return

    if frequency == DATA_TYPE_TICK:
        for sy in symbols:
            if sy in list(six.iterkeys(context.tick_data_cache)):
                del context.tick_data_cache[sy]
                context.tick_sub_symbols.remove(sy)
        return

    # 处理bar的退订
    for sy in symbols:
        k = sy + "_" + frequency
        if k in list(six.iterkeys(context.bar_data_cache)):
            del context.bar_data_cache[k]
            context.bar_sub_infos.remove(BarSubInfo(sy, frequency))
            barwaitgroupinfo = context.bar_waitgroup_frequency2Info.get(frequency, None)
            if barwaitgroupinfo:
                barwaitgroupinfo.remove_one_symbol(sy)

    # 处理已全部退订的 frequency
    for frequency in list(six.iterkeys(context.bar_waitgroup_frequency2Info)):
        if len(context.bar_waitgroup_frequency2Info[frequency]) == 0:
            bwsdklogger.debug('frequency=%s 已全部取消订阅', frequency)
            del context.bar_waitgroup_frequency2Info[frequency]


def current(symbols, fields=''):
    # type: (BwSymbols, Text) -> List[Any]
    """
    查询当前行情快照，返回tick数据
    """
    symbols = load_to_list(symbols)
    fields = load_to_list(fields)

    symbols_str = ','.join(symbols)
    fields_str = ','.join(fields)
    ticklist =[]
    data = py_bwi_current(symbols_str)

    if data is None:
        return []
    else:
        for item in data:
            tick = Tick(item) 
            tick.FromFmt(item) # 格式化成timestamp
            
            # print("*"*70,'current:',tick.created_at)
            # print (timestamp2bj_datetime(Timestamp(tick.created_at)))

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
            ticknn = {}
            # print("*"*21,'current:',fields)
            for k,v in ticknew.items():
                # print(k,v)
                if len(fields)>0:
                    if k in fields:
                        ticknn[k] = v
                else:
                    # print(fields)
                    ticknn[k] = v
                pass
            # print(ticknn)
            ticklist.append(ticknn)
    
    return ticklist


def get_strerror(error_code):
    # type: (int) -> Text
    return py_bwi_strerror(error_code)

def set_cache(cmode):
    return py_bwi_set_cache(cmode)

def schedule(schedule_func, date_rule, time_rule):
    # type: (Any, Text, Text) ->NoReturn
    """
    定时任务. 这里的schedule_func 要求只能有一个context参数的函数
    """
    from datetime import datetime
    d = datetime.strptime(time_rule, '%H:%M:%S')
    time_rule = d.strftime("%H:%M:%S")
    # print(time_rule)
    

    schemdule_info = SCHEDULE_INFO.format(date_rule=date_rule, time_rule=time_rule)
    context.inside_schedules[schemdule_info] = schedule_func
    # print(context.inside_schedules)
    py_bwi_schedule(date_rule, time_rule)


def _all_not_none(a, b):
    # type: (Any, Any) -> bool
    """
    全部都不为None
    """
    return a is not None and b is not None


def run(strategy_id='', filename='', mode=MODE_UNKNOWN, usr='',
        # pwd='',
        backtest_start_time='',
        backtest_end_time='',
        backtest_initial_cash=1000000,
        # backtest_transaction_ratio=1,
        backtest_commission_ratio=0,
        backtest_slippage_ratio=0,
        backtest_adjust=ADJUST_PREV,
        backtest_check_cache=1,
        serv_addr='',
        ptoken='',
        ppipe='',
        pticket=''):
    # type: (Text, Text, int, Text, Text, Text, float, float, float, float, int, int, Text) ->NoReturn
    """
    执行策略
    """
    # print('filename in first:',filename)
    parser = OptionParser()
    parser.add_option("--strategy_id", action="store",
                      dest="strategy_id",
                      default=strategy_id,
                      help="策略id")

    parser.add_option("--filename", action="store",
                      dest="filename",
                      default=filename,
                      help="策略文件名称")

    parser.add_option("--mode", action="store",
                      dest="mode",
                      default=mode,
                      help="策略模式选择")

    parser.add_option("--usr", action="store",
                      dest="usr",
                      default=usr,
                      help="用户usr")

    # parser.add_option("--pwd", action="store",
    #                   dest="pwd",
    #                   default=pwd,
    #                   help="用户pwd")

    parser.add_option("--backtest_start_time", action="store",
                      dest="backtest_start_time",
                      default=backtest_start_time,
                      help="回测开始时间")

    parser.add_option("--backtest_end_time", action="store",
                      dest="backtest_end_time",
                      default=backtest_end_time,
                      help="回测结束时间")

    parser.add_option("--backtest_initial_cash", action="store",
                      dest="backtest_initial_cash",
                      default=backtest_initial_cash,
                      help="回测初始资金")

    # parser.add_option("--backtest_transaction_ratio", action="store",
    #                   dest="backtest_transaction_ratio",
    #                   default=backtest_transaction_ratio,
    #                   help="回测交易费率")

    parser.add_option("--backtest_commission_ratio", action="store",
                      dest="backtest_commission_ratio",
                      default=backtest_commission_ratio,
                      help="回测成交比率")

    parser.add_option("--backtest_slippage_ratio", action="store",
                      dest="backtest_slippage_ratio",
                      default=backtest_slippage_ratio,
                      help="回测滑点费率--暂无")

    parser.add_option("--backtest_adjust", action="store",
                      dest="backtest_adjust",
                      default=backtest_adjust,
                      help="回测复权模式")

    parser.add_option("--backtest_check_cache", action="store",
                      dest="backtest_check_cache",
                      default=backtest_check_cache,
                      help="回测是否使用缓存")

    parser.add_option("--serv_addr", action="store",
                      dest="serv_addr",
                      default=serv_addr,
                      help="终端地址")
    
    parser.add_option("--server", action="store",
                      dest="server",
                      default=serv_addr,
                      help="终端地址")
    
    parser.add_option("--token", action="store",
                      dest="token",
                      default=ptoken,
                      help="verifytoken accountid")

    parser.add_option("--pipe", action="store",
                      dest="pipe",
                      default=ppipe,
                      help="servnet")

    parser.add_option("--ticket", action="store",
                      dest="ticket",
                      default=pticket,
                      help="usertoken")

    (options, args) = parser.parse_args()
    # print('%'*50,options,'%'*50)
    strategy_id = options.strategy_id
    pipe = options.pipe
    tickx = options.ticket
    filename = options.filename
    mode = int(options.mode)
    if mode not in (MODE_UNKNOWN, MODE_LIVE, MODE_BACKTEST):
        raise ValueError('模式只能设置成 MODE_UNKNOWN, MODE_LIVE, MODE_BACKTEST 值')

    from decimal import Decimal
    usr = options.usr
    # pwd = options.pwd
    token=options.token
    
    backtest_start_time = options.backtest_start_time
    backtest_end_time = options.backtest_end_time
    backtest_initial_cash = float(options.backtest_initial_cash)
    # backtest_transaction_ratio = float(options.backtest_transaction_ratio)
    backtest_commission_ratio = float(options.backtest_commission_ratio)
    backtest_slippage_ratio = float(options.backtest_slippage_ratio)
    backtest_adjust = int(options.backtest_adjust)
    # print('*'*50)
    # print (backtest_start_time,backtest_end_time,backtest_initial_cash\
    #     ,backtest_commission_ratio,backtest_slippage_ratio,backtest_adjust)
    # print('*'*50)
    if backtest_adjust == 3:
        backtest_adjust = ADJUST_NONE  # 这个修改是为了适合终端之前把 3 认为是 不复权
    if backtest_adjust not in (ADJUST_NONE, ADJUST_POST, ADJUST_PREV):
        raise ValueError('回测复权模式只能设置成 ADJUST_NONE, ADJUST_POST, ADJUST_PREV 值')

    if backtest_initial_cash < 1:
        raise ValueError('回测初始资金不能设置为小于1, 当前值为:{}'.format(backtest_initial_cash))

    # if not 0 <= backtest_transaction_ratio <= 1:
    #     raise ValueError('回测成交比例允许的范围值为 0<=x<=1, 当前值为{}'.format(backtest_transaction_ratio))

    if not 0 <= backtest_commission_ratio <= 0.1:
        raise ValueError('回测手续费比例允许的范围值为 0<=x<=0.1, 当前值为{}'.format(backtest_commission_ratio))

    if not 0 <= backtest_slippage_ratio <= 0.1:
        raise ValueError('回测滑点比例允许的范围值为 0<=x<=0.1, 当前值为{}'.format(backtest_slippage_ratio))

    backtest_check_cache = int(options.backtest_check_cache)
    serv_addr = options.serv_addr
    serv_addr = options.server

    from bw import api

    # 处理用户传入 __file__这个特殊变量的情况
    syspathes = set(s.replace('\\', '/') for s in sys.path)
    commonpaths = [os.path.commonprefix([p, filename]) for p in syspathes]
    commonpaths.sort(key=lambda s: len(s), reverse=True)
    maxcommonpath = commonpaths[0]
    filename = filename.replace(maxcommonpath, '')  # type: str
    if filename.startswith('/'):
        filename = filename[1:]
    if filename.endswith(".py"):
        filename = filename[:-3]
    
    filename = filename.replace("/", ".")
    filename = filename.replace('\\', ".")
    
    fmodule = import_module(filename)

    # print('importmodule ',filename)
    # 把bw.api里的所有的符号都导出到当前策略文件(fmodule)的命令空间, 方便使用
    for name in api.__all__:
        if name not in fmodule.__dict__:
            fmodule.__dict__[name] = getattr(api, name)

    # 服务地址设置
    if serv_addr:
        set_serv_addr(serv_addr)

    set_token(usr,tickx)
    
    py_bwi_set_user_token(token)

    py_bwi_set_pipe(pipe)

    py_bwi_set_serv_addr(serv_addr)

    py_bwi_set_strategy_id(strategy_id)
    # print('strategy_id++++++++++++++++++++++++++++++=====',strategy_id)
    py_bwi_set_mode(mode)
    context.mode = mode
    context.strategy_id = strategy_id

    # 调用户文件的init
    context.inside_file_module = fmodule
    context.on_tick_fun = getattr(fmodule, 'on_tick', None)
    context.on_bar_fun = getattr(fmodule, 'on_bar', None)
    context.init_fun = getattr(fmodule, 'init', None)
    context.on_execution_report_fun = getattr(fmodule, 'on_execution_report', None)
    context.on_order_status_fun = getattr(fmodule, 'on_order_status', None)
    context.on_backtest_finished_fun = getattr(fmodule, 'on_backtest_finished', None)
    
    context.on_error_fun = getattr(fmodule, 'on_error', None)
    context.on_shutdown_fun = getattr(fmodule, 'on_shutdown', None)
    context.on_account_status_fun = getattr(fmodule, 'on_account_status', None)
    context.on_trade_data_connected_fun = getattr(fmodule, 'on_trade_data_connected', None)
    context.on_market_data_connected_fun = getattr(fmodule, 'on_market_data_connected', None)
    context.on_market_data_disconnected_fun = getattr(fmodule, 'on_market_data_disconnected', None)
    context.on_trade_data_disconnected_fun = getattr(fmodule, 'on_trade_data_disconnected', None)

    context.backtest_start_time = backtest_start_time
    context.backtest_end_time = backtest_end_time
    context.adjust_mode = backtest_adjust
    py_bwi_set_data_callback(callback_controller)  # 设置事件处理的回调函数

    splash_msgs = [
        '-' * 40,
        'python sdk version: {}'.format(__version__),
        '>>>'
        'cpp_sdk version: {}'.format(py_bwi_get_c_version()),
        '-' * 40,
    ]

    print(os.linesep.join(splash_msgs))

    if mode == MODE_BACKTEST:
        # beg="2019-06-10 17:20:00"
        # end="2019-07-10 17:30:00"
        # py_bwi_set_backtest_config(beg,end,1000000, 1, 0, 0, 1, 1)
        py_bwi_set_backtest_config(backtest_start_time,
                                   backtest_end_time,
                                   backtest_initial_cash,
                                   backtest_commission_ratio,
                                   backtest_slippage_ratio,
                                   backtest_adjust,
                                   backtest_check_cache
                                   )
        # try:
        return py_bwi_run()
        #     pass
        # except Exception as identifier:
        #     print('run over')
        #     print(identifier)
        #     pass
    else:
        ## set_cache(backtest_check_cache)
        pass

    if py_bwi_init():
        # print('------------eeeeeeeeeeeeeeeeeeeeeeeeee')
        return

    context._set_accounts()

    while running:
        # print('-'*100,'running')
        py_bwi_poll()


def get_parameters():
    # type: () ->List[Dict[Text, Any]]

    return None




def log(level, msg, source):
    # type: (Text, Text, Text) ->NoReturn
    logs = Logs()
    item = logs.data.add()  # type: Log
    item.owner_id = context.strategy_id
    item.source = source
    item.level = level
    item.msg = msg

    req = logs.SerializeToString()
    py_bwi_log(req)


def stop():
    """
    停止策略的运行,用exit(2)退出
    """
    # print("&"*79,"stop")
    global running
    running = False
    import platform
    if platform.system()=='Windows':
        # print(platform.system())
        sys.exit(2)

#not in use
def set_serv_addr(addr):
    # type: (Text) -> NoReturn
    """
    设置终端服务地址
    """
    # py_bwi_set_serv_addr(addr)
