# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

from datetime import date as Date, datetime as Datetime

# import grpc
import six
# from google.protobuf.timestamp_yy2 import int
from six import string_types
from typing import List, Dict, Text, Any, Union

from bw import utils
from bw.constant import FUNDAMENTAL_ADDR
from bw.csdk.cpp_sdk import py_bwi_get_serv_addr
from bw.model.storage import context


# from bw.yy.data_yy2 import Instrument, InstrumentInfo, ContinuousContract, Dividend

from bw.csdk.cpp_sdk import py_bwi_current,py_bwi_log, py_bwi_strerror, \
    py_bwi_run, py_bwi_set_serv_addr,\
     py_bwi_init, py_bwi_poll, py_bwi_get_c_version, py_bwi_set_apitoken,\
    py_bwi_get_sector,py_bwi_get_trading_dates,py_bwi_get_next_trading_date,\
        py_bwi_get_previous_trading_date,py_bwi_get_fundamentals,\
            py_bwi_get_industry,py_bwi_get_constituents


from bw.utils import str_lowerstrip, load_to_list

BwDate = Union[Text, Datetime, Date]  # 自定义bw里可表示时间的类型
TextNone = Union[Text, None]  # 可表示str或者None类型

MAX_MESSAGE_LENGTH = 1024 * 1024 * 128



def get_sec_type_str(sec_types):
    """把int类型的sectype转为字符串的sectype, 不能转换则返回None"""
    d = {
        1: 'stock',
        2: 'bond',
        3: 'fund',
        4: 'warrant',
        5: 'index',
        6:'futures',# 股指
        7:'stock_kc',
        20:'plate',
        21:'concept',

        '1': 'stock',
        '2': 'bond',
        '3': 'fund',
        '4': 'warrant',
        '5': 'index',
        '6':'futures',# 股指
        '7':'stock_kc',
        '20':'plate',
        '21':'concept',

        'stock':'stock',
        'bond':'bond',
        'fund':'fund',
        'warrant':'warrant',
        'index':'index',
        'futures':'futures',
        'stock_kc':'stock_kc',
        'plate':'plate',
        'concept':'concept',
    }
    result = []
    for sec_type in sec_types:
        if isinstance(sec_type, six.string_types):
            sec_type = sec_type.strip().lower()
        if sec_type in d:
            result.append(d.get(sec_type))

    return result


class FundamentalApi(object):
    def __init__(self):
        self.addr = None

    def _init_addr(self):
        # new_addr = py_bwi_get_serv_addr(FUNDAMENTAL_ADDR)
        # if not new_addr:
        #     raise EnvironmentError("获取不到基本面服务地址")

        # if not self.addr:
        #     self.addr = new_addr
        pass

    def reset_addr(self):
        # self.addr = None
        pass
    #support seperate industry indicate
    def get_fundamentals(self,symbols,  collection ,field,start_date, 
    end_date,limit=1000,  table="SHSZADB"):
        """
        查询财务以及相关数据，详细见文档说明
        """
        

        if isinstance(symbols, string_types):
            symbols = [s.strip() for s in symbols.split(',') if s.strip()]
            symbols = ','.join(symbols)
        
        result = py_bwi_get_fundamentals(symbols,  collection ,field,start_date, end_date,limit,  table)
        # print('-'*100,result)
        return result

    def get_instruments(self, symbols=None, exchanges=None, sec_types=None, names=None, skip_suspended=True,
                        skip_st=True, fields=None):
        """
        查询最新交易标的信息,有基本数据及最新日频数据
        """
        # self._init_addr()
        
        instrument_fields = {
            'symbol', 'sec_level', 'is_suspended', 'multiplier', 'margin_ratio',
            'settle_price',
            'position', 'pre_close', 'upper_limit', 'lower_limit', 'adj_factor',
            'created_at', 'trade_date'
        }

        info_fields = {
            'sec_type', 'exchange', 'sec_id', 'sec_name', 'sec_abbr',
            'price_tick','listed_date', 'delisted_date'
        }

        all_fields = instrument_fields.union(info_fields)

        if isinstance(symbols, string_types):
            symbols = [s for s in map(str_lowerstrip, symbols.split(',')) if s]
        if not symbols:
            symbols = []

        if isinstance(exchanges, string_types):
            exchanges = [utils.to_exchange(s) for s in exchanges.split(',') if utils.to_exchange(s)]
        if not exchanges:
            exchanges = []

        if isinstance(sec_types, six.string_types):
            sec_types = [it.strip() for it in sec_types.split(',') if it.strip()]

        if isinstance(sec_types, int):
            sec_types = [sec_types]

        if isinstance(sec_types, list):
            sec_types = get_sec_type_str(sec_types)

        if not sec_types:
            sec_types = []

        if isinstance(names, string_types):
            names = [s for s in names.split(',') if s]
        if not names:
            names = []

        if not fields:
            filter_fields = all_fields
        elif isinstance(fields, string_types):
            filter_fields = {f for f in map(str_lowerstrip, fields.split(','))
                             if f in all_fields}
        else:
            filter_fields = {f for f in map(str_lowerstrip, fields) if
                             f in all_fields}

        if 'trade_date' in filter_fields:
            filter_fields.add('created_at')

        if not filter_fields:
            return []

        
        instrument_copy_field = filter_fields & instrument_fields
        info_copy_field = filter_fields & info_fields

        for ins in resp.data:  # type: Instrument
            row = dict()

            created_at_val = row.get('created_at', None)
            if isinstance(created_at_val, Datetime):
                row['trade_date'] = utils.utc_datetime2beijing_datetime(created_at_val)
                row.pop('created_at')

            listed_date_val = row.get('listed_date', None)
            if isinstance(listed_date_val, Datetime):
                row['listed_date'] = utils.utc_datetime2beijing_datetime(listed_date_val)

            delisted_date_val = row.get('delisted_date', None)
            if isinstance(delisted_date_val, Datetime):
                row['delisted_date'] = utils.utc_datetime2beijing_datetime(delisted_date_val)

            result.append(row)
        return result

    def get_history_instruments(self, symbols, fields=None, start_date=None, end_date=None):
        """
        返回指定的symbols的标的日指标数据
        """
        # self._init_addr()
        symbols = load_to_list(symbols)
        start_date = utils.to_datestr(start_date)
        end_date = utils.to_datestr(end_date)

        if not start_date:
            start_date = ''
        if not end_date:
            end_date = ''

        result=[]
        for info in result:
            created_at_val = info.get('created_at', None)
            if isinstance(created_at_val, Datetime):
                info['trade_date'] = utils.utc_datetime2beijing_datetime(created_at_val)
                info.pop('created_at')
        return result

    def get_instrumentinfos(self, symbols=None, exchanges=None, sec_types=None, names=None, fields=None):
        """
        查询交易标的基本信息
        如果没有数据的话,返回空列表. 有的话, 返回list[dict]这样的列表. 其中 listed_date, delisted_date 为 datetime 类型
        @:param fields: 可以是 'symbol, sec_type' 这样的字符串, 也可以是 ['symbol', 'sec_type'] 这样的字符list
        """
        # self._init_addr()

        if isinstance(symbols, string_types):
            symbols = [s for s in symbols.split(',') if s]
        if not symbols:
            symbols = []

        all_fields = {
            'symbol', 'sec_type', 'exchange', 'sec_id', 'sec_name', 'sec_abbr', 'price_tick', 'listed_date',
            'delisted_date'
        }

        if not fields:
            filter_fields = all_fields
        elif isinstance(fields, string_types):
            filter_fields = {f for f in map(str_lowerstrip, fields.split(',')) if f in all_fields}
        else:
            filter_fields = [f for f in map(str_lowerstrip, fields) if f in all_fields]

        if not filter_fields:
            return []

        if isinstance(exchanges, string_types):
            exchanges = [utils.to_exchange(s) for s in exchanges.split(',') if utils.to_exchange(s)]
        if not exchanges:
            exchanges = []

        if isinstance(sec_types, six.string_types):
            sec_types = [it.strip() for it in sec_types.split(',') if it.strip()]

        if isinstance(sec_types, int):
            sec_types = [sec_types]

        if isinstance(sec_types, list):
            sec_types = get_sec_type_str(sec_types)

        if not sec_types:
            sec_types = []

        if isinstance(names, string_types):
            names = [s for s in names.split(',') if s]
        if not names:
            names = []

        result = []
        for ins in resp.data:  # type: InstrumentInfo
            row = dict()
            
            listed_date_val = row.get('listed_date', None)
            if isinstance(listed_date_val, Datetime):
                row['listed_date'] = utils.utc_datetime2beijing_datetime(listed_date_val)

            delisted_date_val = row.get('delisted_date', None)
            if isinstance(delisted_date_val, Datetime):
                row['delisted_date'] = utils.utc_datetime2beijing_datetime(delisted_date_val)

            result.append(row)

        return result

    # def get_history_constituents(self, index, start_date=None, end_date=None):
    #     # type: (TextNone, BwDate, BwDate) -> List[Dict[Text, Any]]
    #     """
    #     查询指数历史成分股
    #     返回的list每项是个字典,包含的key值有:
    #     trade_date: 交易日期(datetime类型)
    #     constituents: 一个字典. 每个股票的sybol做为key值, weight做为value值
    #     """
    #     self._init_addr()

    #     start_date = utils.to_datestr(start_date)
    #     end_date = utils.to_datestr(end_date)

    #     if not start_date:
    #         start_date = Date.today()
    #     else:
    #         start_date = Datetime.strptime(start_date, '%Y-%m-%d').date()

    #     if not end_date:
    #         end_date = Date.today()
    #     else:
    #         end_date = Datetime.strptime(end_date, '%Y-%m-%d').date()
    #     return [
    #         {'trade_date': utils.utc_datetime2beijing_datetime(item.created_at.ToDatetime()),
    #          'constituents': dict(item.constituents)}
    #         for item in resp.data
    #     ]

    def get_constituents(self, index, fields=None, df=False):
        """
        查询指数最新成分股. 指定 fields = 'symbol, name'
        返回的list每项是个字典,包含的key值有:
        symbol 股票symbol
        
        如果不指定 fields, 则返回的list每项是symbol字符串
        """
        # self._init_addr()

        all_fields = ['symbol', 'name']
        if not fields:
            filter_fields = {'symbol'}
        elif isinstance(fields, string_types):
            filter_fields = {f for f in map(str_lowerstrip, fields.split(',')) if f in all_fields}
        else:
            filter_fields = {f for f in map(str_lowerstrip, fields) if f in all_fields}

        resp = py_bwi_get_constituents(index)
        if len(resp) > 0:
            filter_fields = list(filter_fields)
            if len(filter_fields) == 1 and filter_fields[0] == 'symbol':
                if not df:
                    return [k['symbol'] for k in resp]
                else:
                    return resp
            else:
                return resp
        else:
            return []

    def get_plates(self, ty):
        """
        查询板块股票列表  0 hy gn dy  1 hy 2 gn 3 dy 
        返回的list每项是个字典,包含的key值有:
        symbol 股票symbol
        """
        rsp = py_bwi_get_sector(ty)
        return rsp

    def get_industry(self, code):
        """
        查询行业股票列表
        """
        if not code:
            return []
        rsp = py_bwi_get_industry(code)
      
        return rsp

    def get_concept(self, code):
        """
        查询概念股票列表
        """
        if not code:
            return []
        rsp = py_bwi_get_industry(code)
      
        return rsp

    def get_trading_dates(self, exchange, start_date, end_date):
        # type: (Text, BwDate, BwDate) -> List[Text]
        """
        查询交易日列表
        如果指定的市场不存在, 返回空列表. 有值的话,返回 yyyy-mm-dd 格式的列表
        """

        exchange = utils.to_exchange(exchange)
        sdate = utils.to_datestr(start_date)
        edate = utils.to_datestr(end_date)
        if not exchange:
            return []
        if not sdate:
            return []
        if not end_date:
            edate = Datetime.now().strftime('%Y-%m-%d')
        # print(exchange,start_date,end_date)
        resp =  py_bwi_get_trading_dates(exchange,sdate,edate)
        # print('-'*20,resp)
        return resp

    def get_previous_trading_date(self, exchange, date):
        # type: (Text, BwDate) -> TextNone
        """
        返回指定日期的上一个交易日
        @:param exchange: 交易市场
        @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
        @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
        """
        exchange = utils.to_exchange(exchange)
        date_str = utils.to_datestr(date)
        if not exchange or not date_str:
            return None
        resp =  py_bwi_get_previous_trading_date(exchange,date)
        return resp

    def get_next_trading_date(self, exchange, date):
        # type: (Text, BwDate) -> TextNone
        """
        返回指定日期的下一个交易日
        @:param exchange: 交易市场
        @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
        @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
        """

        exchange = utils.to_exchange(exchange)
        date_str = utils.to_datestr(date)
        if not date_str or not exchange:
            return None
        resp =  py_bwi_get_next_trading_date(exchange,date)
        return resp

    #not support
    def get_dividend(self, symbol, start_date, end_date=None):
        # type: (Text, BwDate, BwDate) -> List[Dict[Text, Any]]
        """
        查询分红送配
        """

        if not symbol or not start_date:
            return []
        sym_tmp = symbol.split('.')  # List[Text]
        sym_tmp[0] = sym_tmp[0].upper()
        symbol = '.'.join(sym_tmp)

        if not end_date:
            end_date = Datetime.now().strftime('%Y-%m-%d')
        start_date = utils.to_datestr(start_date)
        end_date = utils.to_datestr(end_date)

        resp =[]
        result = []
        fields = ['symbol', 'cash_div', 'share_div_ratio', 'share_trans_ratio', 'allotment_ratio', 'allotment_price',
                  'created_at']
        for divi in resp.data:  # type: Dividend
            row = dict()
            created_at_val = row.get('created_at', None)
            if isinstance(created_at_val, Datetime):
                row['created_at'] = utils.utc_datetime2beijing_datetime(created_at_val)
            result.append(row)
        return result
    #not support
    def get_continuous_contracts(self, csymbol, start_date=None, end_date=None):
        # type: (Text, BwDate, BwDate) -> List[Dict[Text, Any]]

        start_date = utils.to_datestr(start_date)
        end_date = utils.to_datestr(end_date)

        resp =[]

        result = []
        for cc in resp.data:  # type: ContinuousContract
            row = {'symbol': cc.symbol, 'trade_date': utils.utc_datetime2beijing_datetime(cc.created_at.ToDatetime())}
            result.append(row)
        return result
    #not support
    def get_fundamentals_n(self, table, symbols, end_date, fields=None, filter=None, order_by=None, count=1):
        """
        查询基本面财务数据,每个股票在end_date的前n条
        """

        end_date = utils.to_datestr(end_date)

        if isinstance(symbols, string_types):
            symbols = [s.strip() for s in symbols.split(',') if s.strip()]

        # resp = GetFundamentalsNReq(table=table, end_date=end_date, fields=fields,
        #                           symbols=','.join(symbols), filter=filter,
        #                           order_by=order_by, count=count)

        resp=[] 
        result = []
        for item in resp.data:  # type: GetFundamentalsRsp.Fundamental
            r = {
                'symbol': item.symbol,
                'pub_date': utils.utc_datetime2beijing_datetime(item.pub_date.ToDatetime()),
                'end_date': utils.utc_datetime2beijing_datetime(item.end_date.ToDatetime()),
            }
            r.update(item.fields)
            result.append(r)

        return result
