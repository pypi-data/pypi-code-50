# coding: utf-8
# Author: 阿财（Rgveda@github）（11652964@qq.com）
# Created date: 2020-02-27
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2018 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Bitfinex api
具体api文档参考:https://docs.bitfinex.com/docs
"""
import requests
import json
import datetime
import time
import pandas as pd
import numpy as np
from requests.exceptions import ConnectTimeout, SSLError, ReadTimeout, ConnectionError
from retrying import retry

from urllib.parse import urljoin

# from QUANTAXIS.QAUtil.QAcrypto import TIMEOUT, ILOVECHINA
TIMEOUT = 10
ILOVECHINA = "同学！！你知道什么叫做科学上网么？ 如果你不知道的话，那么就加油吧！蓝灯，喵帕斯，VPS，阴阳师，v2ray，随便什么来一个！我翻墙我骄傲！"
Bitfinex_base_url = "https://api-pub.bitfinex.com/"

columne_names = [
    'start_time',
    'open',
    'high',
    'low',
    'close',
    'volume',
    'close_time',
    'quote_asset_volume',
    'num_trades',
    'buy_base_asset_volume',
    'buy_quote_asset_volume',
    'Ignore'
]

Bitfinex2QA_FREQUENCY_DICT = {
    "1m": '1min',
    "5m": '5min',
    "15m": '15min',
    "30m": '30min',
    "1h": '60min',
    "1d": 'day',
}


@retry(stop_max_attempt_number=3, wait_random_min=50, wait_random_max=100)
def QA_fetch_bitfinex_symbols():
    url = urljoin(Bitfinex_base_url, "/api/v1/exchangeInfo")
    retries = 1
    datas = list()
    while (retries != 0):
        try:
            req = requests.get(url, timeout=TIMEOUT)
            retries = 0
        except (ConnectTimeout, ConnectionError, SSLError, ReadTimeout):
            retries = retries + 1
            if (retries % 6 == 0):
                print(ILOVECHINA)
            print("Retry /api/v1/exchangeInfo #{}".format(retries - 1))
            time.sleep(0.5)

        if (retries == 0):
            # 成功获取才处理数据，否则继续尝试连接
            body = json.loads(req.content)
            if len(body["symbols"]) == 0:
                return []
            for symbol in body["symbols"]:
                # 只导入上架交易对
                if (symbol['status'] == 'TRADING'):
                    datas.append(symbol)

    return datas


def QA_fetch_bitfinex_kline(symbol, start_time, end_time, frequency):
    """
    Get the latest symbol‘s candlestick data
    """
    market = 'Bitfinex'
    unity_retries = retries = 1
    datas = list()
    start_time *= 1000
    end_time *= 1000
    while start_time < end_time:
        url = urljoin(Bitfinex_base_url, "/api/v1/klines")
        try:
            req = requests.get(
                url,
                params={
                    "symbol": symbol,
                    "interval": frequency,
                    "startTime": int(start_time),
                    "endTime": int(end_time)
                },
                timeout=TIMEOUT
            )
            # 防止频率过快被断连
            time.sleep(0.5)
            retries = 0
        except (ConnectTimeout, ConnectionError, SSLError, ReadTimeout):
            retries = retries + 1
            unity_retries = unity_retries + 1
            if (retries % 6 == 0):
                print(ILOVECHINA)
            print("Retry /api/v1/klines #{}".format(unity_retries))
            time.sleep(0.5)

        if (retries == 0):
            # 成功获取才处理数据，否则继续尝试连接
            klines = json.loads(req.content)
            if len(klines) == 0:
                break
            datas.extend(klines)
            start_time = klines[-1][6]

    if len(datas) == 0:
        return None

    # 归一化数据字段，转换填充必须字段，删除多余字段
    frame = pd.DataFrame(datas, columns=columne_names)
    frame['market'] = market
    frame['symbol'] = symbol
    # UTC时间转换为北京时间
    frame['start_time'] = frame.apply(
        lambda x: int(x['start_time'] / 1000),
        axis=1
    )
    frame['date'] = pd.to_datetime(
        frame['start_time'],
        unit='s'
    ).dt.tz_localize('UTC').dt.tz_convert('Asia/Shanghai')
    frame['date'] = frame['date'].dt.strftime('%Y-%m-%d')
    frame['datetime'] = pd.to_datetime(
        frame['start_time'],
        unit='s'
    ).dt.tz_localize('UTC').dt.tz_convert('Asia/Shanghai')
    frame['datetime'] = frame['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    # GMT+0 String 转换为 UTC Timestamp
    frame['date_stamp'] = pd.to_datetime(frame['date']
                                        ).astype(np.int64) // 10**9
    frame['created_at'] = int(
        time.mktime(datetime.datetime.now().utctimetuple())
    )
    frame['updated_at'] = int(
        time.mktime(datetime.datetime.now().utctimetuple())
    )
    frame.rename(
        {
            'num_trades': 'trade',
            'start_time': 'time_stamp',
            'buy_quote_asset_volume': 'amount'
        },
        axis=1,
        inplace=True
    )
    if (frequency not in ['1day', Bitfinex2QA_FREQUENCY_DICT['1d'], '1d']):
        frame['type'] = Bitfinex2QA_FREQUENCY_DICT[frequency]
    frame.drop(
        ['close_time',
         'quote_asset_volume',
         'buy_base_asset_volume',
         'Ignore'],
        axis=1,
        inplace=True
    )

    return json.loads(frame.to_json(orient='records'))


if __name__ == '__main__':
    # url = urljoin(Bitfinex_base_url, "/api/v1/exchangeInfo")
    # print(url)
    # a = requests.get(url)
    # print(a.content)
    # print(json.loads(a.content))
    import pytz
    from dateutil.tz import *

    tz = pytz.timezone("Asia/Shanghai")
    url = urljoin(Bitfinex_base_url, "/api/v1/klines")
    start = time.mktime(
        datetime.datetime(2018,
                          6,
                          13,
                          tzinfo=tzutc()).timetuple()
    )
    end = time.mktime(
        datetime.datetime(2018,
                          6,
                          14,
                          tzinfo=tzutc()).timetuple()
    )
    print(start * 1000)
    print(end * 1000)
    data = QA_fetch_bitfinex_kline("ETHBTC", start, end, '1d')
    print(len(data))
    print(data[0])
    print(data[-1])
