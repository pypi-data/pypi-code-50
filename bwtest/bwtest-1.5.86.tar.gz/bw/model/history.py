# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

# import grpc
import pandas as pd

from bw.constant import HISTORY_ADDR
from bw.csdk.cpp_sdk import py_bwi_get_serv_addr
from bw.enum import ADJUST_NONE,ADJUST_PREV,ADJUST_POST
from bw.model.storage import context

from bw.yy.data import *

from bw.utils import standard_fields,timestamp2bj_datetime,to_datetime_bjtzinfo

from bw.csdk.cpp_sdk import py_bwi_history_ticks, py_bwi_history_bars_n,py_bwi_get_trading_dates,py_bwi_history_bars,py_bwi_history_bars2,py_bwi_history_ticks_n

import datetime 

from bw.model.fundamental import FundamentalApi
fundamentalapi = FundamentalApi()

MAX_MESSAGE_LENGTH = 1024 * 1024 * 128

class HistoryApi(object):
    def __init__(self):
        self.addr = None

    def _init_addr(self):
        addr = py_bwi_get_serv_addr(HISTORY_ADDR)
        if not addr:
            raise EnvironmentError("获取不到数据服务地址")

        if not self.addr:
            self.addr = addr

    def reset_addr(self):
        self.addr = None

    def get_history_bars(self, symbol, frequency, start_time, end_time,
                         fields=None,
                         adjust=ADJUST_PREV, adjust_end_time='', df=False):
                        
        
        cdatas = py_bwi_history_bars(symbol,frequency,start_time, end_time ,adjust)

        if cdatas is None:
            return None
        datas = []
        for item in cdatas:
            bar = Bar(item)
            bar.FromFmt(item)
            barnew = {
                'symbol': bar.symbol,
                'eob': timestamp2bj_datetime(bar.eob),
                'bob': timestamp2bj_datetime(bar.bob),
                'open': bar.open,
                'close': bar.close,
                'high': bar.high,
                'low': bar.low,
                'volume': bar.volume,
                'amount': bar.amount,
                'pre_close': bar.pre_close,
                'position': bar.position,
                'frequency': bar.frequency,
                # 'receive_local_time': time.time(),  # 收到时的本地时间秒数
            }
            datas.append(barnew)
            pass
        
        # print("cdata------->",datas)

        fields_str, fields_list = standard_fields(fields, letter_upper=False)
        if not fields_list:
            datas = datas if not df else pd.DataFrame(datas)
            return datas
        else:
            result = []
            for data in datas:
                info = {}
                for field in fields_list:
                    info[field] = data.get(field)
                result.append(info)

            result = result if not df else pd.DataFrame(result)
            return result
        return cdatas


    def get_history_bars2(self, symbol, frequency, start_time, end_time,
                         fields=None,
                         adjust=ADJUST_PREV, adjust_end_time='', df=False):
                        
        
        cdatas = py_bwi_history_bars2(symbol,frequency,start_time, end_time ,adjust)

        if cdatas is None:
            return None
        datas = []
        for item in cdatas:
            bar = Bar(item)
            bar.FromFmt(item)
            barnew = {
                'symbol': bar.symbol,
                'eob': timestamp2bj_datetime(bar.eob),
                'bob': timestamp2bj_datetime(bar.bob),
                'open': bar.open,
                'close': bar.close,
                'high': bar.high,
                'low': bar.low,
                'volume': bar.volume,
                'amount': bar.amount,
                'pre_close': bar.pre_close,
                'position': bar.position,
                'frequency': bar.frequency,
                # 'receive_local_time': time.time(),  # 收到时的本地时间秒数
            }
            datas.append(barnew)
            pass
        
        # print("cdata------->",datas)

        fields_str, fields_list = standard_fields(fields, letter_upper=False)
        if not fields_list:
            datas = datas if not df else pd.DataFrame(datas)
            return datas
        else:
            result = []
            for data in datas:
                info = {}
                for field in fields_list:
                    info[field] = data.get(field)
                result.append(info)

            result = result if not df else pd.DataFrame(result)
            return result
        return cdatas


    def get_history_ticks(self, symbols, start_time, end_time, fields=None,
                          skip_suspended=True, fill_missing=None,
                          adjust=ADJUST_NONE, adjust_end_time='', df=False):
        
   
        cdata =py_bwi_history_ticks(symbols,start_time,end_time, adjust, adjust_end_time, skip_suspended, fill_missing)

        datas = []
        for item in cdatas:
            tick = Tick()
            tick.FromFmt(item)
            if len(tick.quotes) < 5:
                for _ in range(len(tick.quotes), 5):
                    zero_val = {'bid_p': 0, 'bid_v': 0, 'ask_p': 0, 'ask_v': 0}
                    tick.quotes.append(zero_val)

            ticknew = {
                'quotes': quotes,
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
            datas.append(ticknew)
            pass
        
        fields_str, fields_list = standard_fields(fields, letter_upper=False)
        if not fields_list:
            datas = datas if not df else pd.DataFrame(datas)
            return datas
        else:
            result = []
            for data in datas:
                info = {}
                for field in fields_list:
                    info[field] = data.get(field)
                result.append(info)

            result = result if not df else pd.DataFrame(result)
            return result
        return cdatas

    # KLINE N py_bwi_history_bars_n
    def get_history_n_bars3(self, symbol, frequency, count, end_time= datetime.datetime.now(),
                           fields=None,
                           adjust=ADJUST_PREV,  fill_missing=None,df=False):
 
        start_back_with = 0
        nowtime = to_datetime_bjtzinfo (datetime.datetime.now() ) # to_datetime_bjtzinfo(end_time)
        endtime = to_datetime_bjtzinfo(end_time)
        
        codelist = symbol.split('.')

        # print('-'*20,codelist,'==',endtime.strftime("%Y-%m-%d"),nowtime.strftime("%Y-%m-%d"))
        
        trading_day_ls = fundamentalapi.get_trading_dates(codelist[0],endtime.strftime("%Y-%m-%d"),nowtime.strftime("%Y-%m-%d"))
        
        start_back_with =  len(trading_day_ls) -1 if len(trading_day_ls)>0 else 0

        # print(start_back_with,'-'*60,nowtime,end_time)

        cdatas = py_bwi_history_bars_n(symbol,frequency,count,start_back_with,adjust)
        
        datas = []
        for item in cdatas:
            bar = Bar(item)
            bar.FromFmt(item)
            # print(bar.bob)
            barnew = {
                'symbol': bar.symbol,
                'eob': timestamp2bj_datetime(bar.eob),
                'bob': timestamp2bj_datetime(bar.bob),
                'open': bar.open,
                'close': bar.close,
                'high': bar.high,
                'low': bar.low,
                'volume': bar.volume,
                'amount': bar.amount,
                'pre_close': bar.pre_close,
                'position': bar.position,
                'frequency': bar.frequency,
                # 'receive_local_time': time.time(),  # 收到时的本地时间秒数
            }
            datas.append(barnew)
            pass
        
        # print('over construct!!')
        # print(fields)

        
        fields_str, fields_list = standard_fields(fields, letter_upper=False)
        
        # print('over standard_fields!!', fields_str,fields_list)
        if not fields_list:
            datas = datas if not df else pd.DataFrame(datas)
            return datas
        else:
            result = []
            for data in datas:
                info = {}
                for field in fields_list:
                    info[field] = data.get(field)
                result.append(info)

            result = result if not df else pd.DataFrame(result)
            return result
        return cdatas

    
    
    #KLINE DATE  by N py_bwi_history_bars2
    def get_history_n_bars2(self, symbol, frequency, count, end_time= datetime.datetime.now(),
                           fields=None,
                           adjust=ADJUST_PREV,  fill_missing=None,df=False):
                           
        start_back_with = 0
        nowtime = to_datetime_bjtzinfo (datetime.datetime.now() ) # to_datetime_bjtzinfo(end_time)
        endtime = to_datetime_bjtzinfo(end_time)
        
        codelist = symbol.split('.')

        year_plus = datetime.timedelta(days=int(365*(count+365)/245))
        # print('year---plus ',year_plus,count)
        begtime = endtime - year_plus
        # print('------begtime----endtime',begtime,' ',endtime)
        # print('-'*20,codelist,'==',endtime.strftime("%Y-%m-%d"),nowtime.strftime("%Y-%m-%d"))
        
        trading_day_ls = fundamentalapi.get_trading_dates(codelist[0],begtime.strftime("%Y-%m-%d"),endtime.strftime("%Y-%m-%d"))
        lentradingdays = len(trading_day_ls)
        # print('len trading_day_ls:',lentradingdays)
        if trading_day_ls is None:
            return []
        time_start = begtime.strftime("%Y-%m-%d")
        if lentradingdays > int(count) :
            time_start = trading_day_ls[-count]
            # print('----seg time: ',time_start)
            # trading_day_ls_new = fundamentalapi.get_trading_dates(codelist[0],time_start,endtime.strftime("%Y-%m-%d"))
            # print(len(trading_day_ls_new))
        else:
            print('get_history_n_bars2 : count error occured')

        # print(start_back_with,'-'*60,nowtime,end_time)

        cdatas = py_bwi_history_bars2(symbol,frequency,time_start, endtime.strftime("%Y-%m-%d") ,adjust)
        
        datas = []
        for item in cdatas:
            bar = Bar(item)
            bar.FromFmt(item)
            # print(bar.bob)
            barnew = {
                'symbol': bar.symbol,
                'eob': timestamp2bj_datetime(bar.eob),
                'bob': timestamp2bj_datetime(bar.bob),
                'open': bar.open,
                'close': bar.close,
                'high': bar.high,
                'low': bar.low,
                'volume': bar.volume,
                'amount': bar.amount,
                'pre_close': bar.pre_close,
                'position': bar.position,
                'frequency': bar.frequency,
                # 'receive_local_time': time.time(),  # 收到时的本地时间秒数
            }
            datas.append(barnew)
            pass
        
        # print('over construct!!')
        # print(fields)

        
        fields_str, fields_list = standard_fields(fields, letter_upper=False)
        
        # print('over standard_fields!!', fields_str,fields_list)
        if not fields_list:
            datas = datas if not df else pd.DataFrame(datas)
            return datas
        else:
            result = []
            for data in datas:
                info = {}
                for field in fields_list:
                    info[field] = data.get(field)
                result.append(info)

            result = result if not df else pd.DataFrame(result)
            return result
        return cdatas

    
    #KLINE BY DATE py_bwi_history_bars
    def get_history_n_bars(self, symbol, frequency, count, end_time= datetime.datetime.now(),
                           fields=None,
                           adjust=ADJUST_PREV,  fill_missing=None,df=False):
 
        start_back_with = 0
        nowtime = to_datetime_bjtzinfo (datetime.datetime.now() ) # to_datetime_bjtzinfo(end_time)
        endtime = to_datetime_bjtzinfo(end_time)
        
        codelist = symbol.split('.')

        year_plus = datetime.timedelta(days=int(365*(count+365)/245))
        # print('year---plus ',year_plus,count)
        begtime = endtime - year_plus
        # print('------begtime----endtime',begtime,' ',endtime)
        # print('-'*20,codelist,'==',begtime,endtime.strftime("%Y-%m-%d"),nowtime.strftime("%Y-%m-%d"))
        
        trading_day_ls = fundamentalapi.get_trading_dates(codelist[0],begtime.strftime("%Y-%m-%d"),endtime.strftime("%Y-%m-%d"))
        lentradingdays = len(trading_day_ls)
        # print('len trading_day_ls:', lentradingdays)
        if trading_day_ls is None:
            return []
        time_start = begtime.strftime("%Y-%m-%d")
        if lentradingdays > int(count) :
            time_start = trading_day_ls[-count]
            # print('----seg time: ',time_start)
            trading_day_ls_new = fundamentalapi.get_trading_dates(codelist[0],time_start,endtime.strftime("%Y-%m-%d"))
            # print(len(trading_day_ls_new))
        else:
            print('get_history_n_bars count error occured')

        # print(start_back_with,'-'*60,nowtime,end_time)
        # print(symbol,frequency,time_start, endtime.strftime("%Y-%m-%d") ,adjust)
        cdatas = py_bwi_history_bars(symbol,frequency,time_start, endtime.strftime("%Y-%m-%d") ,adjust)
        # print(cdatas)
        
        datas = []
        for item in cdatas:
            bar = Bar(item)
            bar.FromFmt(item)
            # print(bar.bob)
            barnew = {
                'symbol': bar.symbol,
                'eob': timestamp2bj_datetime(bar.eob),
                'bob': timestamp2bj_datetime(bar.bob),
                'open': bar.open,
                'close': bar.close,
                'high': bar.high,
                'low': bar.low,
                'volume': bar.volume,
                'amount': bar.amount,
                'pre_close': bar.pre_close,
                'position': bar.position,
                'frequency': bar.frequency,
                # 'receive_local_time': time.time(),  # 收到时的本地时间秒数
            }
            datas.append(barnew)
            pass
        
        # print('over construct!!')
        # print(fields)

        
        fields_str, fields_list = standard_fields(fields, letter_upper=False)
        
        # print('over standard_fields!!', fields_str,fields_list)
        if not fields_list:
            datas = datas if not df else pd.DataFrame(datas)
            return datas
        else:
            result = []
            for data in datas:
                info = {}
                for field in fields_list:
                    info[field] = data.get(field)
                result.append(info)

            result = result if not df else pd.DataFrame(result)
            return result
        return cdatas

    

    def get_history_n_ticks(self, symbol, count, end_time=None, fields=None,
                            skip_suspended=None,
                            fill_missing=None, adjust=ADJUST_NONE,
                            adjust_end_time='', df=False):
        
        cdata =py_bwi_history_ticks_n(symbols, n, end_time,adjust, adjust_end_time,  skip_suspended, fill_missing)
        datas = []
        for item in cdatas:
            tick = Tick()
            tick.FromFmt(item)
            if len(tick.quotes) < 5:
                for _ in range(len(tick.quotes), 5):
                    zero_val = {'bid_p': 0, 'bid_v': 0, 'ask_p': 0, 'ask_v': 0}
                    tick.quotes.append(zero_val)

            ticknew = {
                'quotes': quotes,
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
            datas.append(ticknew)
            pass
        
        fields_str, fields_list = standard_fields(fields, letter_upper=False)
        if not fields_list:
            datas = datas if not df else pd.DataFrame(datas)
            return datas
        else:
            result = []
            for data in datas:
                info = {}
                for field in fields_list:
                    info[field] = data.get(field)
                result.append(info)

            result = result if not df else pd.DataFrame(result)
            return result
        return cdatas

        