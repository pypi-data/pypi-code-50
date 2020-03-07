# -*-coding:utf-8 -*-

# @Time    : 2020/2/26 20:30
# @File    : base.py
# @User    : yangchuan
# @Desc    : local database source
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
from quant_trade_framework.common.redisConfig import RuntimeConfig
from quant_trade_framework.core.object import BarData
from quant_trade_framework.common.logConfig import Logger
from quant_trade_framework.common.constant import Interval

logger = Logger.module_logger("system")
class QuantData:
    @staticmethod
    def get_bars(symbol:str,
                 exchange:str,
                 start_datetime:datetime,
                 end_datetime:datetime,
                 inteval:str = "1d",
                 counts:int=0):
        """

        :param symbol:
        :param exchange:
        :param start_datetime:
        :param end_datetime:
        :param inteval:
        :param counts:
        :return:
        """
        if not symbol or symbol == "" or \
                not exchange or exchange == "" or \
                type(end_datetime) != datetime:
            return None

        col = symbol + "-" + inteval
        results = []
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[exchange]
            collection = db[col]
            if counts ==0 :
                count = collection.count_documents({"date": {"$lt": end_datetime,"$gt":start_datetime}})
                if count > 0:
                    cursor = collection.find({"date": {"$lt": end_datetime,
                                                                 "$gt": start_datetime}}).sort([('date', -1)])
                    for item in cursor:
                        result = BarData()
                        result.close_price = item['close']
                        result.high_price = item['max']
                        result.low_price = item['min']
                        result.open_price = item['open']
                        result.volume = item['volume']
                        result.datetime = item['date']
                        result.interval = inteval
                        results.append(result)
            else:
                count = collection.count_documents({"date": {"$lt": end_datetime}})
                if count > 0:
                    cursor = collection.find({"date": {"$lt": end_datetime}}).sort([('date', -1)]).limit(counts)
                    for item in cursor:
                        result = BarData()
                        result.close_price = item['close']
                        result.high_price = item['max']
                        result.low_price = item['min']
                        result.open_price = item['open']
                        result.volume = item['volume']
                        result.datetime = item['date']
                        result.interval = inteval
                        results.append(result)

        except BaseException as e:
            logger.error(str(e))

        results.reverse()
        return results

    @staticmethod
    def get_bar(symbol: str,
                exchange: str,
                start_datetime: datetime,
                end_datetime: datetime,
                interval: str = "1d"):
        """
        get latest symbol price
        :param symbol:
        :return: float
        """
        if not symbol or symbol == "" or \
                not exchange or exchange == "" or \
                type(start_datetime) != datetime or \
                type(end_datetime) != datetime:
            return None

        col = symbol + "-" + interval
        results = None
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[exchange]
            collection = db[col]
            count = collection.count_documents({"date": {"$lte": end_datetime, "$gt": start_datetime}})
            if count > 0:
                cursor = collection.find({"date": {"$lte": end_datetime,
                                                   "$gt": start_datetime}}).sort([('date', -1)]).limit(1)
                for item in cursor:
                    results = BarData()
                    results.close_price = item['close']
                    results.high_price = item['max']
                    results.low_price = item['min']
                    results.open_price = item['open']
                    results.volume = item['volume']
                    results.datetime = item['date']
                    results.interval = interval

        except BaseException as e:
            logger.error(str(e))
        return results

# if __name__ == '__main__':
#     re = QuantData.get_bars(symbol="000001.XSHE", exchange="quant",
#                             start_datetime=datetime.strptime("2020-01-01 14:00:00","%Y-%m-%d %H:%M:%S"),
#                             end_datetime=datetime.strptime("2020-02-01 14:00:00","%Y-%m-%d %H:%M:%S"))
#     print(re)