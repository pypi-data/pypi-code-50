import os
import sys
import time
from pprint import pprint

import numpy as np
import pandas as pd
# import quandl
import scipy.optimize as sco
from funpicker import Query, QueryTypes
from funtime import Store
from pypfopt import expected_returns, risk_models
from pypfopt.efficient_frontier import EfficientFrontier

MONGO = os.getenv('MONGODB', "localhost")
PORTFOLIO_COLLECTION = os.getenv("PORTFOLIO_COLLECTION", "global")

# from portfolio_server.config import PORTFOLIO_COLLECTION, LOCALMONGO
#Converter

store = Store(MONGO).create_lib(PORTFOLIO_COLLECTION).get_store()
priceStore = store[PORTFOLIO_COLLECTION]


def get_portfolio(portfolio_list):
    general_timeperiod = (60 * 60) * 24 # 25 hours
    coin_dict = {

    }
    for coin in portfolio_list:
        latest = priceStore.query_latest({'type': 'price', 'exchange': "CCCAGG", "period" : "day", "trade": coin, "base" : "USD", "limit": 25})
        latest = list(latest)
        # print(latest)
        if len(latest) != 0:
            # print("it's not zero")
            # Check to see if the price was pulled in the last 18 hours
            most_recent_price = latest[0]

            current_time = time.time()
            time_check = general_timeperiod + most_recent_price['timestamp']
            # print(time_check, current_time)
            if time_check > current_time:
                # Add coin to dict
                # print("The time is totally right")
                coin_dict[coin] = latest
                # print(coin_dict)
                continue
            
        print(coin, " -- Getting Checked")
        fpq = Query().set_crypto(coin).set_fiat("USD").set_exchange("CCCAGG").set_period("day").set_limit(25).get()
        coin_dict[coin] = []
        for item in fpq:
            item['timestamp'] = float(item.pop('time'))
            item['type'] = "price"
            item['period'] = "day"
            item['exchange'] = "CCCAGG"
            item['trade'] = coin
            item['base'] = "USD"
            priceStore.store(item)
            coin_dict[coin].append(item)
        
    return coin_dict


def get_coin_pricing(exchange, base, trade):
    general_timeperiod = (1800) # 1 minute
    coin_dict = {

    }

    latest = priceStore.query({'type': 'price', 'exchange': exchange, "period" : "minute", "trade": trade, "base" : base})
    latest = list(latest)
    if len(latest) > 0:
        time_check = general_timeperiod + latest[0]['timestamp']
        current_time = time.time()
        if time_check > current_time:
            return latest[0]
    fpq = Query().set_crypto(trade).set_fiat(base).set_exchange(exchange).set_period("minute").set_limit(5).get()
    
    if len(fpq) == 0:
        return {
            "type": "price",
            "period": "minute",
            "timestamp": time.time(),
            "trade": trade,
            "base": base,
            "exchange": exchange,
            "close": 0
        }
    
    for item in fpq:
        item['timestamp'] = float(item.pop('time'))
        item['type'] = "price"
        item['period'] = "minute"
        item['exchange'] = exchange
        item['trade'] = trade
        item['base'] = base
        priceStore.store(item)
    
    return fpq[0]

def create_portfolio_price_df(coin_dict):
    portfolio_frame = pd.DataFrame()
    for k, v in coin_dict.items():
        if k is None:
            print("Don't do anything")
            continue
        df = pd.DataFrame(v)
        ts = pd.to_datetime(df['timestamp'], unit='s')
        df.reindex(pd.DatetimeIndex(ts))
        portfolio_frame[k] = df['close'] 
    return portfolio_frame.sort_index()




def portfolio_from_df(df, risk_lvl=0):
    mu = expected_returns.mean_historical_return(df)
    S = risk_models.sample_cov(df)

    # # Optimise for maximal Sharpe ratio
    ef = EfficientFrontier(mu, S, gamma=risk_lvl)
    raw_weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    ef.portfolio_performance(verbose=True)

    return cleaned_weights
