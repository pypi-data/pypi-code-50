import copy
from linkkt_e2e_handlers.allocation import AllocationHandler
from random import sample
import uuid
from contextlib import ContextDecorator
from typing import Dict, List, Optional

import maya
import pandas as pd
from crayons import yellow, green, cyan, red
from cytoolz import keyfilter
from jamboree import DBHandler, Jamboree, JamboreeNew
from jamboree.handlers.default import TimeHandler
from jamboree.handlers.default import MultiDataManagement
from jamboree.handlers.default.data import DataHandler
from loguru import logger


from linkkt_e2e_handlers.utils.slippage import RandomUniformSlippageModel
from linkkt_e2e_handlers.utils.trades.trade import Trade
from linkkt_e2e_handlers.utils.trades.trade_type import TradeType
from linkkt_e2e_handlers.data import PriceGenerator
from linkkt_e2e_handlers.properties import MetaProperty
from linkkt_e2e_handlers.schemas import SchemaHolder



def create_data_item(category:str, subcategory:dict, name:str):
    dset = {
        "name": name,
        "subcategories": subcategory,
        "category": category
    }
    return dset

def price_gen_func():
    asset_list = ["BTC", "ATL", "TRX", "ETH", "BCH", "XRP"]
    episodes = [uuid.uuid4().hex for x in range(10)]
    price_gen = PriceGenerator()
    price_gen.episodes = episodes
    price_gen.assets = asset_list
    price_gen.starting_min = 200
    price_gen.starting_max=500
    price_gen.is_varied=True
    price_gen.length=3000
    price_gen.generate()
    return price_gen




def omit(blacklist, d):
    return keyfilter(lambda k: k not in blacklist, d)


class timecontext(ContextDecorator):
    def __enter__(self):
        self.start = maya.now()._epoch
        return self

    def __exit__(self, *exc):
        self.end = maya.now()._epoch
        delta = self.end - self.start
        print(f"It took {delta}ms")
        return False

"""
    NOTE: Will remove soon. Going through a concept.
"""


class SampleExchange(DBHandler):
    def __init__(self) -> None:
        super().__init__()
        self.entity = "sample_portfolio"
        self.required = {
            "episode": str,
            "user_id": str,
            "exchange": str,
            "live": bool
        }
        self._time:TimeHandler = TimeHandler()
        self._data:MultiDataManagement = MultiDataManagement()
        self._property:MetaProperty = MetaProperty()
        self._allocator: Optional[AllocationHandler] = AllocationHandler()


    def metaprop(self, _alt={}):
        self._property.dbhand = self
        return self._property.prop(_alt)


    @property
    def allocator(self):
        """ Allocation stuff for"""
        if self._allocator is None:
            raise NotImplementedError("Add allocator")
        
        user_id = self['user_id']
        exchange = self['exchange']
        episode = self['episode']
        live = self['live']

        self._allocator["episode"] = episode
        self._allocator["user_id"] = user_id
        self._allocator["exchange"] = exchange
        self._allocator["live"] = live
        self._allocator.processor = self.processor
        return self._allocator




    @property
    def time(self):
        self._time.processor = self.processor
        self._time["live"] = self["live"]
        self._time["episode"] = self["episode"]
        return self._time
    



    @property
    def pricing(self):
        user_id = self['user_id']
        exchange = self['exchange']
        episode = self['episode']
        live = self['live']

        self._data['set_name'] = f"{user_id}-{exchange}-{episode}-{live}"
        self._data.episode = episode
        self._data.live = live
        self._data.processor = self.processor
        return self._data


    def add_pricing(self, name, subcategories={}):
        # This can only be under the category market
        category = "markets"
        combined_dict = {
            "name": name,
            "subcategories": subcategories,
            "category": category
        }
        # print(combined_dict)
        self.pricing.add_multiple_data_sources([combined_dict])


    def remove_pricing(self):
        """ Will add code into Jamboree directly ... """
        pass
    

    def rebalance(self, rebalancing_frame:pd.DataFrame):
        self.allocator.new_step_test(rebalancing_frame)
        

    def step(self):
        all_data = self.pricing.step()
        return all_data

    def pre_portfolio(self, data:dict):
        data_keys = list(data.keys())
        first_item = [x.split(":")[0] for x in data_keys]
        empty = pd.DataFrame()
        latest_price_dict = {}
        for index, first in enumerate(first_item):
            dk = data_keys[index]
            d1 = data[dk]
            empty[str(first)] = d1['close']
            latest_price_dict[first] = d1['close'].iloc[-1]
        return empty, latest_price_dict
    
    
    def singular_price(self, data:dict):
        """
            Get the latest price for each currency. Use to update all of the the other price informations
        """
        data_keys = list(data.keys())
        first_item = [x.split(":")[0] for x in data_keys]
        latest_price_dict = {}
        for index, first in enumerate(first_item):
            dk = data_keys[index]
            d1 = data[dk]
            latest_price_dict[first] = d1['close'].iloc[-1]
        return latest_price_dict


    def test(self):
        """
            A test function to see if we can do everything we need to: 
                - Get the price data for mutiple currencies
                - Send the price data into two places to get a response
        """
        self.time.head = maya.now().add(weeks=25)._epoch
        self.time.change_stepsize(microseconds=0, days=1, hours=0)
        self.time.change_lookback(microseconds=0, weeks=25, hours=0)
        self.pricing.sync()
        data = self.step()
        portfolio_frame, singular_price_dict = self.pre_portfolio(data)
        self.rebalance(portfolio_frame)
        
        print(
            red(singular_price_dict, bold=True)
        )
    


    def reset(self):
        self.time.reset()
        self.pricing.reset()
        self.allocator.reset()

def get_base_datahandler():
    datahandler = DataHandler()
    datahandler["category"] = "markets"
    datahandler["subcategories"] = {
        "market": "stock",
        "country": "US",
        "sector": "faaaaake"
    }
    return datahandler


def main():
    """ Should run through everything returning zero right now"""
    processor = JamboreeNew()
    sample_exchange = SampleExchange()
    prices = price_gen_func()
    assets = list(prices.asset_bars.keys())
    
    main_episode = uuid.uuid4().hex
    user_id = uuid.uuid4().hex
    exchange = "fake_exchange"


    sample_exchange.processor = processor
    sample_exchange["episode"] = main_episode
    sample_exchange["user_id"] = user_id
    sample_exchange["exchange"] = exchange
    sample_exchange["live"] = False
    sample_exchange.reset()

    dh = get_base_datahandler()
    dh.processor = processor
    dh['category'] = "markets"
    dh["subcategories"]["episode"] = main_episode
    
    for asset in assets:
        dh["name"] = asset
        data = prices.asset_bars[asset]
        dh.reset()

        dh.store_time_df(data, is_bar=True)
    sample_exchange.add_pricing(assets[0], dh["subcategories"])
    sample_exchange.add_pricing(assets[1], dh["subcategories"])
    sample_exchange.test()


    # print(items)
    # episode_id = uuid.uuid4().hex
    # user_id = uuid.uuid4().hex
    # portfolio_handler = PortfolioHandler()

    # portfolio_handler.limit = 1000
    # portfolio_handler.event = jambo
    # portfolio_handler.processor = processor
    # portfolio_handler['episode'] = episode_id
    # portfolio_handler['user_id'] = user_id
    # portfolio_handler['exchange'] = "binance"
    # portfolio_handler['live'] = False
    # portfolio_handler.reset()
    # for _ in range(1000):
    #     logger.info(yellow(portfolio_handler.time.head))
    

if __name__ == "__main__":
    main()
