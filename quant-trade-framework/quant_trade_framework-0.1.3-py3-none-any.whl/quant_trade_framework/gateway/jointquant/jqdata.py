# encoding: UTF-8
from datetime import datetime, timedelta
import jqdatasdk as jq
from pandas import DataFrame
import pandas as pd
from quant_trade_framework.core import setting
from quant_trade_framework.data.database import initialize
from quant_trade_framework.core.object import BarData
from quant_trade_framework.common.constant import Constant
from quant_trade_framework.common.logConfig import Logger

logger = Logger.module_logger("JqDataCore")
class JqDataCore:
    gateway = 'JQData'
    exchange = 'JQData'
    jquser = "17745021310"
    jqpassword = "021310"
    barFields = ['date', 'open', 'high', 'low', 'close', 'volume']
    priceFields = ['open', 'high', 'low', 'close', 'volume']
    symbol = ''
    jq.auth(jquser, jqpassword)

    @staticmethod
    def get_benchmark_price(end_datetime:datetime,frequency:str,price_type:str):
        """
        获取上证50基准价格
        :param end_datetime: datetime
        :param frequency:'Xd','Xm', 'daily'(等同于'1d'),
        'minute'(等同于'1m'), X是一个正整数
        :param price_type: str,price type,'open', 'close',
         'high', 'low', 'volume', 'money'
        :return: float
        """
        result = 0
        df = jq.get_price("000016.XSHG",
                         count=1,
                         end_date=end_datetime,
                         frequency=frequency,
                         fq=None)
        pd.to_datetime(df.iloc[:,0],unit='s')
        for ix, row in df.iterrows():
            result = row[price_type]
        return result

    @staticmethod
    def get_bars(symbol:str,count: int,end_datetime: datetime, unit: str,fields=['date', 'open', 'close', 'high',
                                 'low', 'volume']):
        """
        获取上证50基准价格
        :param end_datetime: datetime
        :param frequency:'Xd','Xm', 'daily'(等同于'1d'),
        'minute'(等同于'1m'), X是一个正整数
        :param price_type: str,price type,'open', 'close',
         'high', 'low', 'volume', 'money'
        :return: float
        """
        df = jq.get_bars(security=symbol,
                         count=count,
                         unit=unit,
                         fields=['date', 'open', 'close', 'high',
                                 'low', 'volume'],
                          end_dt=end_datetime)
        results = []
        if df.size > 0:
            for index, row in df.iterrows():
                result = BarData()
                result.close_price = row['close']
                result.high_price = row['high']
                result.low_price = row['low']
                result.open_price = row['open']
                result.volume = row['volume']
                if unit == Constant.KLINE_INTERVAL_1DAY:
                    result.datetime = datetime(row['date'].year,row['date'].month,row['date'].day,23,59,00)
                else:
                    result.datetime = row['date']
                result.interval = unit
                results.append(result)
        return results

    @staticmethod
    def get_bar(symbol: str, end_datetime: datetime, unit: str):
        """
        获取上证50基准价格
        :param end_datetime: datetime
        :param frequency:'Xd','Xm', 'daily'(等同于'1d'),
        'minute'(等同于'1m'), X是一个正整数
        :param price_type: str,price type,'open', 'close',
         'high', 'low', 'volume', 'money'
        :return: float
        """
        df = jq.get_bars(security=symbol,
                         count=1,
                         unit=unit,
                         fields=['date', 'open', 'close', 'high',
                                 'low', 'volume'],
                         end_dt=end_datetime)
        results = BarData()
        if df.size > 0:
            for index, row in df.iterrows():
                results.close_price = row['close']
                results.high_price = row['high']
                results.low_price = row['low']
                results.open_price = row['open']
                results.volume = row['volume']
                results.datetime = row['date']
                results.interval = unit
        return results

    @staticmethod
    def get_price_by_span(symbol: str, start_datetime: datetime, end_datetime: datetime, unit: str):
        """
        获取上证50基准价格
        :param end_datetime: datetime
        :param frequency:'Xd','Xm', 'daily'(等同于'1d'),
        'minute'(等同于'1m'), X是一个正整数
        :param price_type: str,price type,'open', 'close',
         'high', 'low', 'volume', 'money'
        :return: float
        """
        df = jq.get_price(security=symbol,
                          start_date=start_datetime,
                          end_date=end_datetime,
                          unit=unit,
                          fields=['date', 'open', 'close', 'high',
                                  'low', 'volume'])
        results = []
        if df.size > 0:
            for index, row in df.iterrows():
                result = BarData()
                result.close_price = row['close']
                result.high_price = row['high']
                result.low_price = row['low']
                result.open_price = row['open']
                result.volume = row['volume']
                result.datetime = row['date']
                result.interval = unit
                results.append(result)
        return results

    @staticmethod
    def get_price(symbol: str, end_datetime: datetime, unit: str):
        """
        获取上证50基准价格
        :param end_datetime: datetime
        :param frequency:'Xd','Xm', 'daily'(等同于'1d'),
        'minute'(等同于'1m'), X是一个正整数
        :param price_type: str,price type,'open', 'close',
         'high', 'low', 'volume', 'money'
        :return: float
        """
        df = jq.get_price(security=symbol,
                         count=1,
                         unit=unit,
                         fields=['date', 'open', 'close', 'high',
                                 'low', 'volume'],
                         end_date=end_datetime)
        results = BarData()
        if df.size > 0:
            for index, row in df.iterrows():
                results.close_price = row['close']
                results.high_price = row['high']
                results.low_price = row['low']
                results.open_price = row['open']
                results.volume = row['volume']
                results.datetime = row['date']
                results.interval = unit
        return results


    @staticmethod
    def save_to_mongodb(data, symbol, inteval):
        database_manager = initialize.init(setting.SETTINGS)
        # insert into database
        database_manager.save_bar_data(symbol, data, str(inteval).lower())

    @staticmethod
    def bar_data_get_and_storage(symbol:str,start_datetime: datetime,end_datetime: datetime, frequency: str):
        result = end_datetime - start_datetime
        bars_count = result.days
        if frequency == Constant.KLINE_INTERVAL_60MINUTE:
            bars_count = bars_count * 24
        results = JqDataCore.get_bars(symbol=symbol,count=bars_count,end_datetime=end_datetime,unit=frequency)
        if len(results) > 0:
            logger.info(str(len(results)) + " records is waiting to store")
            JqDataCore.save_to_mongodb(results, symbol, frequency)

    @staticmethod
    def logout(self):
        if jq.is_auth():
            jq.logout()
        return

    @staticmethod
    def get_all_indexes():
        print(jq.get_all_securities(types=['index'], date=None))

# if __name__ == '__main__':
#     now = datetime.now()
#     temp = now + timedelta(days=-400)
#     JqDataCore.get_all_indexes()
    # print(JqDataCore.get_benchmark_price(temp,Constant.KLINE_INTERVAL_1DAY,"close"))
    # JqDataCore.bar_data_get_and_storage('M9999.XDCE',temp,now,Constant.KLINE_INTERVAL_1DAY)
    # temp.getTradeDays("2020-01-01","2020-06-01")
#     print(temp.get_api_counts())
#     temp.sdkTest()
#     symbols = temp.get_future_contracts("M")
#     # print(symbols)
#     symbols = ["M2005.XDCE"]
#     temp.setSymbol(symbols)
#     temp.getSymbolBarByTimeSpan(
#         '2019-05-31 11:30:00',
#         '2019-11-19 15:30:00',
#         '1m', True)
#     # temp.setSymbol('JD2001.XDCE')
#     # temp.getSymbolBar(
#     #     10,
#     #     '2019-11-18 09:30:00',
#     #     '1m', True)