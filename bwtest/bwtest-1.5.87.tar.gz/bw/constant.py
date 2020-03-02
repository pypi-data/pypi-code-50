# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

SUB_ID = 'SUB_ID:{}:{}:{}'  # 订阅股票唯一id  由三部分组成  symbol frequency count
SUB_TAG = 'SUB_TAG:{}:{}'  # 取消订阅股票标签 由两部分组成  symbol frequency

DATA_TYPE_TICK = 'tick'
DATA_TYPE_BAR = 'bar'

"""
c-sdk回调的类型
"""
CALLBACK_TYPE_INIT = 'init'
CALLBACK_TYPE_TICK = 'data.api.Tick'
CALLBACK_TYPE_BAR = 'data.api.Bar'
CALLBACK_TYPE_SCHEDULE = 'schedule'
CALLBACK_TYPE_EXECRPT = 'core.api.ExecRpt'
CALLBACK_TYPE_ORDER = 'core.api.Order'
CALLBACK_TYPE_INDICATOR = 'core.api.Indicator'
CALLBACK_TYPE_CASH = 'core.api.Cash'
CALLBACK_TYPE_POSITION = 'core.api.Position'
CALLBACK_TYPE_PARAMETERS = 'runtime-config'
CALLBACK_TYPE_ERROR = 'error'
CALLBACK_TYPE_TIMER = 'timer'
CALLBACK_TYPE_BACKTEST_FINISH = 'backtest-finished'
CALLBACK_TYPE_STOP = 'stop'

CALLBACK_TYPE_TRADE_CONNECTED = 'td-connected'
CALLBACK_TYPE_TRADE_DISCONNECTED = 'td-disconnected'

CALLBACK_TYPE_DATA_CONNECTED = 'md-connected'
CALLBACK_TYPE_DATA_DISCONNECTED = 'md-disconnected'

CALLBACK_TYPE_ACCOUNTSTATUS = 'core.api.AccountStatus'

TRADE_CONNECTED = 1
DATA_CONNECTED = 2

SCHEDULE_INFO = 'date_rule={date_rule},time_rule={time_rule}'

HISTORY_ADDR = 'bw-history-rpc'
HISTORY_REST_ADDR = 'bw-history-rpcgw'
FUNDAMENTAL_ADDR = 'bw-fundamental-rpc'

CSDK_OPERATE_SUCCESS = 0  # c-sdk 操作成功



class QuoteItemLikeDict2(dict):
    bid_p = ... # type: float
    bid_v = ... # type: int
    ask_p = ... # type: float
    ask_v = ... # type: int


class ObjectLikeDict(dict):
    quotes = ... # type: List[QuoteItemLikeDict2]
    symbol = ... # type: Text
    created_at = ... # type: datetime.datetime
    price = ... # type: float
    open = ... # type: float
    high = ... # type: float
    low = ... # type: float
    cum_volume = ... # type: float
    cum_amount = ... # type: float
    cum_position = ... # type: int
    last_amount = ... # type: float
    last_volume = ... # type: int
    trade_type = ... # type: int
    nanos = ... # type: int
    receive_local_time = ... # type: float


class BarLikeDict2(dict):
    symbol = ... # type: Text
    eob = ... # type: datetime.datetime
    bob = ... # type: datetime.datetime
    open = ... # type: float
    close = ... # type: float
    high = ... # type: float
    low = ... # type: float
    volume = ... # type: float
    amount = ... # type: float
    pre_close = ... # type: float
    position = ... # type: int
    frequency = ... # type: Text
    receive_local_time = ... # type: float

