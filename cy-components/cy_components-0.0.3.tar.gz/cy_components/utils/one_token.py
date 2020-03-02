import json
import requests
import random
import pandas as pd
from .coin_pair import CoinPair
# from ..common.enum import TimeFrame
# from ..common.defs import COL_CANDLE_BEGIN_TIME


class OneToken:

    def __init__(self, cfgs=[]):
        """根据配置初始化

        Parameters
        ----------
        cfgs : list, optional
            TODO, by default []
        """
        self.configs = cfgs

    @property
    def exchange_name_mapping_dict(self):
        """OneToken 交易所名称映射 """
        return {
            "Binance": "binance",
            "HuobiPro": "huobip",
        }

    def fetch_candle_data(self, exchange_name, coin_pair: CoinPair, timeframe: TimeFrame, limit=200, since=0):
        """Fetching"""
        headers = {'ot-key': random.choice(self.configs)['key']}
        contract = '{}/{}'.format(self.exchange_name_mapping_dict[exchange_name], coin_pair.pair(sep='.').lower())
        base_url = 'https://hist-quote.1tokentrade.cn/candles'
        since /= 1000  # seconds
        until = since + limit * timeframe.time_interval(res_unit='s')
        k_line_url = f'{base_url}?since={since}&until={until}&contract={contract}&duration={timeframe.value}&format=json'

        candle_res = requests.get(k_line_url, headers=headers)
        candle_res.raise_for_status()

        print(candle_res.headers)
        data = candle_res.json()

        def rename_key(x):
            """back to milliseconds"""
            x[COL_CANDLE_BEGIN_TIME] = x.pop('timestamp') * 1000
            return x

        replaced_list = [rename_key(x) for x in data]
        return replaced_list
