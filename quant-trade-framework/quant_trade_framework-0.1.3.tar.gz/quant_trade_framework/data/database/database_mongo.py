from datetime import datetime
from pymongo import MongoClient
from quant_trade_framework.common.constant import Exchange, Interval
from .database import Driver
from quant_trade_framework.common.logConfig import Logger
import pandas as pd

logger = Logger.module_logger("system")
def init(_: Driver, settings: dict):
    database = settings["database.database"]
    host = settings["database.host"]
    port = settings["database.port"]
    username = settings["database.user"]
    password = settings["database.password"]
    type = settings["type"]
    if not username:  # if username == '' or None, skip username
        username = None
        password = None
    return MongoManager(host, port, username,
                           password,type)


class MongoManager:
    def __init__(self,para_host,para_port,
                 para_username,para_password,type):
        """
        constractor method
        :param para_host: str, host name
        :param para_port: int, port
        :param para_username: str, auth username
        :param para_password: str, auth password
        :param type: none
        """
        if type == "btc":
            self.bar_database = "btc"
            self.tick_database = "bars"
        else:
            self.bar_database = "quant"
            self.tick_database = "ticks"
        self.mongo_client = MongoClient(
            host=para_host,
            port=para_port,
            username=para_username,
            password=para_password
        )
        return

    def load_bar_data(
        self,
        symbol: str,
        interval: Interval,
        start: datetime,
        end: datetime
    ):
        """
        query bar data
        :param symbol: str, security name
        :param interval:str, bar data interval
        :param start: str,query start datetime
        :param end:str, query end datetime
        :return: data frame
        """
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[(symbol + "-" + interval)]
            start_datetime_obj = datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
            end_datetime_obj = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
            data = mongo_db_col_obj.find({"date": {"$gte": start_datetime_obj,"$lte":end_datetime_obj}})
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
            logger.info("load_bar_data success")
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def load_tick_data(
            self,
            symbol: str,
            interval: Interval,
            start: datetime,
            end: datetime
    ):
        """
        query tick data
        :param symbol: str, security name
        :param interval:str, bar data interval
        :param start: str,query start datetime
        :param end:str, query end datetime
        :return: data frame
        """
        try:
            mongo_db_obj = self.mongo_client[self.tick_database]
            mongo_db_col_obj = mongo_db_obj[(symbol + "-" + interval)]
            start_datetime_obj = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
            end_datetime_obj = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
            data = mongo_db_col_obj.find({"date": {"$gte": start_datetime_obj, "$lte": end_datetime_obj}})
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
            logger.info("load_tick_data success")
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def save_bar_data(self,symbol:str,df:object,interval:Interval):
        """
        save bar data
        :param symbol:  str, security name
        :param df: data source
        :param interval: str, bar data interval
        :return: none
        """
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[(symbol + "-" + interval)]

            for item in df:
                temp_item = {
                    "date": item.datetime,
                    "close": item.close_price,
                    "high": item.high_price,
                    "low": item.low_price,
                    "open": item.open_price,
                    "volume": item.volume
                }
                mongo_db_col_obj.update_one({"date": item.datetime}, {"$set": temp_item}, upsert=True)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))

    def save_tick_data(self, symbol:str,df:object,interval:Interval):
        """
        save tick data
        :param symbol:  str, security name
        :param df: data source
        :param interval: str, bar data interval
        :return: none
        """
        try:
            mongo_db_obj = self.mongo_client[self.tick_database]
            mongo_db_col_obj = mongo_db_obj[(symbol + "-" + interval)]
            data = df.to_dict(orient='records')
            for item in data:
                mongo_db_col_obj.update_one({"date": item['date']}, {"$set": item}, upsert=True)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))

    def get_newest_bar_data(self, symbol: str, interval:Interval):
        """
        get the latest bar data
        :param symbol:str, security name
        :param interval:str, bar data interval
        :return: dataframe object
        """
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            data = mongo_db_col_obj.find().sort([('date', -1)]).limit(1)
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def get_newest_tick_data(self, symbol: str):
        """
        get the latest tick data
        :param symbol:str, security name
        :return:dataframe object
        """
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            data = mongo_db_col_obj.find().sort([('date', -1)]).limit(1)
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def clean(self, symbol: str):
        """
        clean symbol database
        :param symbol:
        :return:
        """
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            mongo_db_col_obj.remove({})
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))


