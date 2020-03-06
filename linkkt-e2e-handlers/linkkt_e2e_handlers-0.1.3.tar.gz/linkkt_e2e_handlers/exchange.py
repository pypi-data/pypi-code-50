import copy
import random
import uuid
from contextlib import ContextDecorator
from typing import Dict, List, Optional
import numpy as np
import maya
import pandas as pd
from crayons import red, blue, green, yellow, magenta, cyan, white
from cytoolz import keyfilter
from jamboree import DBHandler, Jamboree, JamboreeNew
from jamboree.handlers.default import TimeHandler
from jamboree.handlers.default import MultiDataManagement
from jamboree.handlers.default.data import DataHandler
from loguru import logger


from linkkt_e2e_handlers.allocation import AllocationHandler
from linkkt_e2e_handlers.utils.slippage import RandomUniformSlippageModel
from linkkt_e2e_handlers.utils.trades.trade import Trade, DynamicTrade
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

    def __init__(self, color="white"):
        self._color = color

    def get_color(self, color):
        return {
            "white": white,
            "blue": blue,
            "yellow": yellow,
            "red": red,
            "green": green,
            "magenta": magenta,
            "cyan": cyan
        }[color]

    def __enter__(self):
        self.start = maya.now()._epoch
        return self

    def __exit__(self, *exc):
        self.end = maya.now()._epoch
        delta = self.end - self.start
        craycray = self.get_color(self._color)
        print(craycray(f"It took {delta}ms"))
        return False

"""
Note: Will remove soon. Going through a concept.
"""

class PortfolioHandler(DBHandler):
    """Abstract handler that we use to keep track of portfolio information.
    """

    def __init__(self, base_instrument="USD", start_balance=10000, limit=100, lazy_load=False):
        super().__init__()
        # TODO: Lazy load should be replaced with the parameters `pre_load` and `just_in_time`
        self._base_instrument = base_instrument
        self.start_balance = start_balance
        self.entity = "portfolio"
        self.required = {
            "episode": str,
            "user_id": str,
            "exchange": str,
            "live": bool
        }


        # TODO: Cut down on the object initiation.
        # NOTE: We can initiate the object once then change the rest of the variables multiple times
        self._time:TimeHandler = TimeHandler()
        self._data:MultiDataManagement = MultiDataManagement()
        self._property:MetaProperty = MetaProperty()
        self._allocator: Optional[AllocationHandler] = AllocationHandler()
        

        self._balance = 0
        self._limit = limit
        self._category = "market"
        self._subcategories = {}
        self._schema = SchemaHolder()

        
        # Store a list of the portfolio & performance states 

        self._slippage_model = RandomUniformSlippageModel() # TODO: Need to replace
        self._instrument_precision = 8
        self._commission_percent = 0.3
        self._base_precision = 2


        self._min_trade_amount = 0.000001
        self._max_trade_amount = 1000000
        self._min_trade_price = 0.00000001
        self._max_trade_price = 100000000



        # Placeholder variables
        self.placeholders = {}
        self.latest_prices = {}
        # Determines if the object has loaded the important varviables
        self.has_updated = False

        
        
        
    # -------------------------------------------------------------------
    # --------------------- Properties & Setters ------------------------
    # -------------------------------------------------------------------
    @property
    def is_live(self) -> bool:
        lively = self['live']
        episode = self['episode']
        if episode == "live" and lively == True:
            return True
        return False
    

    @property
    def current_time(self):
        """ 
            # Current Time
            ---
            Get the current time for the portfolio.

            Gets the time from the price/dataset. If the datasource is live it should get the current price and use that. 
        """
        # TODO: Add live logic
            # If episode and live are both live, return maya.now()._epoch
        return self.time.head

    @property
    def limit(self):
        return self._limit
    
    @limit.setter
    def limit(self, limit):
        self._limit = limit


    @property
    def holdings(self):
        """ Get the holdings for the user """
        if self.has_updated:
            return self.placeholders.get("holdings", [])
        _holdings = self.load_holdings()
        filtration_list = ['user_id', 'episode', 'type', 'detail', 'exchange', 'live', 'timestamp', 'event_id']
        holdings = map(lambda x: omit(filtration_list, x), _holdings)
        return list(holdings)


    @property
    def performance(self):
        """ Get the performance of the user/exchange"""
        if self.has_updated == True:
            return self.placeholders.get("portfolio", {})
        performance = self.load_performance()
        if isinstance(performance, dict):
            performance = [performance]
        
        filtration_list = ['user_id', "episode", 'type', 'detail', 'exchange', 'live', 'timestamp', 'event_id']
        
        performance_filtered = list(map(lambda x: omit(filtration_list, x), performance))
        return performance_filtered


    @property
    def portfolio(self):
        """ Get the latest portfolio of the user/exchange"""
        if self.has_updated:
            return self.placeholders.get("portfolio", {})
        portfolio = self.latest_portfolio()
        filtered_portfolio = omit(['user_id', 'episode', 'type', 'timestamp', 'event_id'], portfolio) 
        return filtered_portfolio
            
    @property
    def portfolio_history(self):
        """ Get the latest portfolio of the user/exchange"""
        if self.has_updated:
            return self.placeholders.get("portfolio_history", [])
        portfolio = self.load_portfolio()
        filtration_list = ['user_id', 'episode', 'type', 'timestamp', 'exchange', 'live', 'event_id']
        filtered_portfolio = list(map(lambda x: omit(filtration_list, x), portfolio))
        return filtered_portfolio


    @property
    def balance(self) -> float:
        if self.has_updated:
            return self.placeholders.get("balance", 0.0)
        latest_balance = self.latest_performance()
        return float(latest_balance.get('balance', 0.0))
        

    @property
    def trades(self) -> List[Dict]:
        """ Get all of the trades for this user"""
        trades = self.load_trades()
        if isinstance(trades, dict):
            trades = [trades]
        filtration_list = ["episode", "exchange", "user_id", "type", "detail", "timestamp", "live", 'event_id']
        trades_filtered = map(lambda x: omit(filtration_list, x), trades)
        return list(trades_filtered)

    
    @property
    def net_worth(self) -> float:
        net_worth = self.balance
        portfolio = self.portfolio
        if not portfolio:
            return net_worth


        portfolio_filtered = omit(['user_id', 'episode', 'type', 'time', 'timestamp', 'exchange', 'live', 'event_id'], portfolio)

        for symbol, amount in portfolio_filtered.items():
            if symbol == self._base_instrument:
                continue

            # print(f"{red(amount)}-{green(symbol)}")
            current_price = self.current_price(symbol=symbol)
            net_worth += current_price * amount

        return net_worth

    @property
    def pricing(self):
        """ 
            NOTE:
                - We determine the user's portfolio using this dataset.
                - Since it has a name heavily tailored to the
                - We position what we want the user to have using this pricing indicator 
        """
        if self._data is None:
            raise NotImplementedError("Pricing handler not found")
        user_id = self['user_id']
        exchange = self['exchange']
        episode = self['episode']
        live = self['live']

        self._data['set_name'] = f"{user_id}-{exchange}-{episode}-{live}"
        self._data.episode = episode
        self._data.live = live
        self._data.processor = self.processor
        return self._data


    @property
    def allocation(self):
        allocator = self.allocator.allocation
        return allocator

    @property
    def allocator(self):
        """ Allocation stuff for"""
        if self._allocator is None:
            raise AttributeError("Allocator handler not found")
        
        user_id = self['user_id']
        exchange = self['exchange']
        episode = self['episode']
        live = self['live']

        self._allocator["episode"] = episode
        self._allocator["user_id"] = user_id
        self._allocator["exchange"] = exchange
        self._allocator["live"] = live
        self._allocator.processor = self.processor
        self._allocator.time = self.time
        return self._allocator

    @property
    def profit_loss_percent(self) -> float:
        """
            Calculate the percentage change in net worth since the last reset.
            Returns:
                The percentage change in net worth since the last reset.
        """
        return float(self.net_worth / self.start_balance) * 100
    # Use to get counts inside of the database


    @property
    def time(self) -> 'TimeHandler':
        self._time.processor = self.processor
        self._time["live"] = self["live"]
        self._time["episode"] = self["episode"]
        return self._time


    def get_count(self) -> int:
        count = self.count()
        return count


    def performance_count(self) -> int:
        alt = {"detail": "performance"}
        count = self.count(alt)
        return count

    
    def holdings_count(self) -> int:
        alt = {"detail": "holdings"}
        count = self.count(alt)
        return count


    # ----------------------------------------
    # -------------- Querying ----------------
    # ----------------------------------------


    def latest_portfolio(self):
        if self.is_live == True:
            last_state = self.last(ar="absolute")
            return last_state
        last_state = self.last(ar="relative")
        return last_state

    def latest_performance(self):
        alt = {"detail": "performance"}
        if self.is_live == True:
            last_state = self.last(alt=alt, ar="absolute")
            return last_state
        last_state = self.last(alt=alt, ar="relative")
        return last_state


    def load_performance(self):
        alt = {"detail": "performance"}
        
        if self.is_live == True:
            performance = self.many(self.limit, alt=alt, ar="absolute")
        else:
            performance = self.many(self.limit, alt=alt, ar="relative")
        
        if isinstance(performance, dict):
            return [performance]
        return performance
    
    
    def load_portfolio(self):
        if self.is_live == True:
            portfolio = self.many(self.limit, ar="absolute")
        else:
            portfolio = self.many(self.limit, ar="relative")
        if isinstance(portfolio, dict):
            return [portfolio]
        return portfolio
    

    def load_trades(self):
        alt = {"detail": "trade"}
        if self.is_live == True:
            trades = self.many(self.limit, alt=alt, ar="absolute")
        else:
            trades = self.many(self.limit, alt=alt, ar="relative")
        if isinstance(trades, dict):
            return [trades]
        return trades
    

    def load_holdings(self):
        alt = {"detail": "holdings"}
        if self.is_live == True:
            _holdings = self.many(self.limit, alt=alt, ar="absolute")
        else:
            _holdings = self.many(self.limit, alt=alt, ar="relative")
        if isinstance(_holdings, dict):
            return [_holdings]
        return _holdings


    def load_placeholders(self):
        if self.has_updated == False:
            self.placeholders['portfolio'] = self.portfolio
            self.placeholders['balance'] = float(self.balance)
            self.placeholders['holdings'] = self.holdings
            self.placeholders['portfolio_history'] = self.portfolio_history
            self.placeholders['performance'] = self.performance
            self.has_updated = True


    def current_price(self, symbol="BTC"):
        return self.latest_prices.get(symbol, 0.0)

    # ----------------------------------------
    # ---------------- Saving ----------------
    # ----------------------------------------

    def save_portfolio(self, data):
        """ Save portfolio """
        _data = copy.copy(self._query)
        _data.update(data)
        _data['type'] = self.entity
        _data['time'] = self.current_time
        _data['timestamp'] = maya.now()._epoch
        for key, value in _data.items():
            if isinstance(value, np.float64):
                _data[key] = float(value)
        self.save(_data)

    def save_performance(self, data) -> None:
        """ Save performance information """
        alt = {"detail": "performance"}
        _data = copy.copy(self._query)
        _data.update(data)
        _data.update(alt)
        _data['type'] = self.entity
        _data['time'] = self.current_time
        _data['timestamp'] = maya.now()._epoch
        for key, value in _data.items():
            if isinstance(value, np.float64):
                _data[key] = float(value)
        self.save(_data, alt=alt)

    

    def save_trade(self, data):
        alt = {"detail": "trade"}

        _data = copy.copy(self._query)
        _data.update(data)
        _data.update(alt)

        _data['type'] = self.entity
        _data['time'] = self.current_time
        _data['timestamp'] = maya.now()._epoch
        # _data['amount'] = float(_data.get("amount", 0.0))
        # print(f"{yellow(data)} --- {cyan(type(_data['timestamp']))}")
        for key, value in _data.items():
            if isinstance(value, np.float64):
                _data[key] = float(value)
        self.save(_data, alt=alt)


    def save_holdings(self, data, timestamp=maya.now()._epoch):
        alt = {"detail": "holdings"}

        _data = copy.copy(self._query)
        _data.update(data)
        _data.update(alt)

        _data['type'] = self.entity
        _data['time'] = self.current_time
        _data['timestamp'] = maya.now()._epoch
        
        for key, value in _data.items():
            if isinstance(value, np.float64):
                _data[key] = float(value)
            
        self.save(_data, alt=alt)
    




    # ----------------------------------------
    # ------------ Operations ----------------
    # ----------------------------------------    

    
    def _update_account(self, _trade:Trade):
        """ Updates the portfolio exchange account. """
        # TODO: Add timestamp to trade
        
        if self._is_valid_trade(_trade):
            self._make_trade(_trade)

        current_balance = float(self.balance)
        portfolio = self.portfolio
        portfolio[self._base_instrument] = current_balance


        latest_performance = {
            'net_worth': self.net_worth,
            'balance': current_balance
        }

        self.save_performance(latest_performance)
        self.save_portfolio(portfolio)
        self._update_holdings()
    
    def _update_account_no_order(self):
        """ Updates the portfolio exchange account. """
        # TODO: Add timestamp to trade
        balance = float(self.balance)
        current_balance = float(balance)
        portfolio = self.portfolio
        portfolio[self._base_instrument] = current_balance


        latest_performance = {
            'net_worth': self.net_worth,
            'balance': current_balance
        }

        self.save_performance(latest_performance)
        self.save_portfolio(self.portfolio)
        self._update_holdings()


    def _update_holdings(self):
        """ Duplication of net_worth code"""
        holdings = {}
        portfolio = self.portfolio
        if not portfolio:
            return 


        portfolio_filtered = omit(['user_id', 'episode', 'type', 'time', 'timestamp', 'exchange', 'live', 'event_id'], portfolio)

        """
                "exchange": "superhotfyre",
                "episode": "335f32a64a4a4812b8373a65782e7801",
                "user_id": "10",
                "type": "portfolio",
                "detail": "trade",
                "live": false,
                "symbol": "ABC",
                "trade_type": 1,
                "amount": 1,
                "price": 792.64,
                "time": 1579585984.351019,
                "timestamp": 1577778784.3788486

        """


        portfolio_items = portfolio_filtered.items()
        for symbol, amount in portfolio_items:
            if symbol == self._base_instrument:
                holdings[symbol] = amount
                continue
            

            current_price = self.current_price(symbol=symbol)
            total = current_price * amount
            holdings[symbol] = total

        self.save_holdings(holdings, timestamp=self.current_time)

    def _make_trade(self, trade:Trade):
        """ Trades on the account then updates it"""

        
        if not trade.is_hold:
            """ TODO: We'll need to save this in two places to make it work IRL"""
            self.save_trade({
                'symbol': trade.symbol,
                'trade_type': trade.trade_type.value,
                'amount': trade.amount,
                'price': trade.price
            })
        
        if trade.is_buy:
            self.placeholders['balance'] -= float((trade.amount * trade.price))
            self.placeholders['portfolio'][trade.symbol] = self.placeholders['portfolio'].get(trade.symbol, 0) + trade.amount
        elif trade.is_sell:
            self.placeholders['balance'] += float((trade.amount * trade.price))
            self.placeholders['portfolio'][trade.symbol] = self.placeholders['portfolio'].get(trade.symbol, 0) - trade.amount
        
        


    def _is_valid_trade(self, _trade:Trade) -> bool:
        
        if _trade.is_buy and self.placeholders['balance'] < _trade.amount * _trade.price:
            logger.error("Not enough to buy")
            return False
        elif _trade.is_sell and self.placeholders['portfolio'].get(_trade.symbol, 0) < _trade.amount:
            logger.error("Not enough to sell")
            return False
        

        is_both = _trade.amount >= self._min_trade_amount and _trade.amount <= self._max_trade_amount

        # if is_both: logger.success("Both conditions succeeded")
        return is_both


    def execute_pct_trade(self, trade:Trade) -> Trade:
        self.load_placeholders()

        # current_price = self.current_price(symbol=trade.symbol)
        # commission = self._commission_percent / 100
        filled_trade = trade.copy()
        

        # if filled_trade.is_hold or not self._is_valid_trade(filled_trade):
        #     filled_trade.amount = 0



        # if filled_trade.is_buy:
        #     price_adjustment = (1 + commission)
        #     filled_trade.price = round(current_price * price_adjustment, self._base_precision)
        #     filled_trade.amount = round((filled_trade.price * filled_trade.amount) / filled_trade.price,
        #                                 self._instrument_precision)
        # elif filled_trade.is_sell:
        #     price_adjustment = (1 - commission)
        #     filled_trade.price = round(current_price * price_adjustment, self._base_precision)
        #     filled_trade.amount = round(filled_trade.amount, self._instrument_precision)

        # if not filled_trade.is_hold:
        #     filled_trade = self._slippage_model.fill_order(filled_trade, current_price)
        

        # self._update_account(filled_trade)
        return filled_trade


    def execute_trade(self, trade:Trade) -> Trade:
        self.load_placeholders()

        current_price = self.current_price(symbol=trade.symbol)
        commission = self._commission_percent / 100
        filled_trade = trade.copy()
        

        if filled_trade.is_hold or not self._is_valid_trade(filled_trade):
            filled_trade.amount = 0



        if filled_trade.is_buy:
            price_adjustment = (1 + commission)
            filled_trade.price = round(current_price * price_adjustment, self._base_precision)
            filled_trade.amount = round((filled_trade.price * filled_trade.amount) / filled_trade.price,
                                        self._instrument_precision)
        elif filled_trade.is_sell:
            price_adjustment = (1 - commission)
            filled_trade.price = round(current_price * price_adjustment, self._base_precision)
            filled_trade.amount = round(filled_trade.amount, self._instrument_precision)

        if not filled_trade.is_hold:
            filled_trade = self._slippage_model.fill_order(filled_trade, current_price)
        

        self._update_account(filled_trade)
        return filled_trade

    def instrument_balance(self, symbol: str):
        """ Get the balance for the instrument """
        portfolio = self.latest_portfolio()
        
        if symbol in portfolio.keys():
            return portfolio[symbol]
        return 0.0

    

    
    # -------------------------------------------------------
    # ------------------ Reset Conditions -------------------
    # -------------------------------------------------------
    



    def _reset_portfolio(self):
        count = self.get_count()
        if count == 0:
            self.save_portfolio({f"{self._base_instrument}": float(self.start_balance), "time": self.current_time})

    def _reset_performance(self):
        """ Reset the performance inside of a given exchange """
        count = self.performance_count()
        if count == 0:
            self.save_performance({
                    "balance": float(self.start_balance), 
                    "net_worth": float(self.start_balance), 
                    "time": self.current_time
                }
            )
    
    def _reset_holdings(self):
        """ Reset the holdings inside of a given exchange """
        count = self.holdings_count()
        if count == 0:
            self.save_holdings({f"{self._base_instrument}": float(self.start_balance), "time": self.current_time})

    def _reset_price(self):
        """ Resets the price. If it's a backtest or simulation, we'll pull information into place so we can backtest. """
        self.pricing.reset()
    
    def _reset_allocation(self):
        self.allocator.reset()

    def _reset_time(self):
        self.time.reset()


    def add_asset(self, name, subcategories={}):
        """This can only be under the category market"""
        category = "markets"
        combined_dict = {
            "name": name,
            "category": category,
            "subcategories": subcategories
        }
        self.pricing.add_multiple_data_sources([combined_dict])


    def remove_asset(self, name, subcategories={}):
        """
            Remove assets from the user. 
            It doesn't add if it doesn't exist.
        """
        pass

    def reset(self):
        """ Determines if we're re-initiating """
        logger.warning("Resetting everything")
        self._reset_price()
        self._reset_time()
        self._reset_allocation()


        """ Portfolio specific resets """
        self._reset_performance()
        self._reset_portfolio()
        self._reset_holdings()
        logger.success("Successfully reset all core handlers and variables")

    
    def price_preprocessing(self, data:dict):
        data_keys = list(data.keys())
        first_item = [x.split(":")[0] for x in data_keys]
        portfolio = pd.DataFrame()
        latest_price_dict = {}
        for index, first in enumerate(first_item):
            dk = data_keys[index]
            d1 = data[dk]
            portfolio[str(first)] = d1['close']
            latest_price_dict[first] = d1['close'].iloc[-1]
        return portfolio, latest_price_dict


    def step(self, trade=None) -> dict:

        self.load_placeholders()
        self.pricing.sync()
        
        final_dict = {'obs': {}, 'done': False}
        prices_information = self.pricing.step()

        portfolio_batch, price_dict = self.price_preprocessing(prices_information)
        self.latest_prices = price_dict
        
        # Set the price inside of the main dict for preprocessing
        self.allocator.new_step(portfolio_batch)

        logger.debug(self.latest_prices)
        if trade is not None:
            if isinstance(trade, DynamicTrade):
                net_worth = self.net_worth
                portfolio = self.portfolio
                price = self.current_price(symbol=trade.symbol)

                dynamic_trade = copy.copy(trade)

                amount = float(portfolio.get(trade.symbol, 0.0)) # how many of this given asset do we have
                
                dynamic_trade.amount = float(amount)
                dynamic_trade.price = (float(price) + 0.00000000000001)
                dynamic_trade.net_worth = float(net_worth)

                trade = dynamic_trade.calculate_trade()
                if isinstance(trade.amount, np.float64):
                    trade.amount = float(trade.amount)
                
            if isinstance(trade, Trade):
                self.execute_trade(trade)
            else:
                self._update_account_no_order()
            self.execute_trade(trade)    
        else:
            self._update_account_no_order()
        final_dict['done'] = (not self.pricing.is_next)
        # we'd put all of the portfolio information here by asset. 
        final_dict['obs']["portfolio"] = {}
        # get percentages
        self.clear_cache()
        return final_dict
    

    def step_with_time(self, trade:Trade=None) -> dict:
        self.load_placeholders()
        self.time.step()
        final_dict = {'obs': {}, 'done': False}

        prices_information = self.pricing.step()
        portfolio_batch, price_dict = self.price_preprocessing(prices_information)
        balance = {self._base_instrument: self.balance}
        self.latest_prices = {**price_dict, **balance}
        # Set the price inside of the main dict for preprocessing
        self.allocator.step(portfolio_batch)
        if trade is not None:
            self.execute_trade(trade)
        else:
            self._update_account_no_order()
        final_dict['done'] = (not self.pricing.is_next)
        # we'd put all of the portfolio information here by asset. 
        final_dict['obs']["portfolio"] = {}
        # get percentages
        return final_dict
    
    def clear_cache(self):
        self.placeholders = {}
        self.has_updated = False

    def render(self):
        """ Get the information necessary to give a report for the user. """
        performance = self.performance
        holdings = self.holdings
        allocation = self.allocation
        portfolio_history = self.portfolio_history

        performance_frame = pd.DataFrame(performance)
        holdings_frame = pd.DataFrame(holdings)
        portfolio_frame = pd.DataFrame(portfolio_history)
        print(yellow("Perfomance", bold=True))
        print(performance_frame.tail(3))

        print(cyan("Holdings", bold=True))
        print(holdings_frame.tail(3))

        print(magenta("Portfolio", bold=True))
        print(portfolio_frame.tail(3))
        print(allocation)



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
    main_episode = uuid.uuid4().hex
    user_id = uuid.uuid4().hex
    exchange_name = "fake_exchange"


    portfolio_hand = PortfolioHandler()
    portfolio_hand.processor = processor
    portfolio_hand['exchange'] = exchange_name
    portfolio_hand['user_id'] = user_id
    portfolio_hand['episode'] = main_episode
    portfolio_hand['live'] = False

    portfolio_hand.reset()
    

    # sample_exchange = SampleExchange()
    prices = price_gen_func()
    assets = list(prices.asset_bars.keys())

    dh = get_base_datahandler()
    dh.processor = processor
    dh['category'] = "markets"
    dh["subcategories"]["episode"] = main_episode
    
    for asset in assets:
        dh["name"] = asset
        data = prices.asset_bars[asset]
        dh.reset()
        print(red(data))
        dh.store_time_df(data, is_bar=True)
    
    portfolio_hand.time.head = maya.now().add(weeks=25)._epoch
    portfolio_hand.time.change_stepsize(microseconds=0, days=1, hours=0)
    portfolio_hand.time.change_lookback(microseconds=0, weeks=25, hours=0)
    portfolio_hand.add_asset(assets[0], dh["subcategories"])
    portfolio_hand.add_asset(assets[1], dh["subcategories"])
    portfolio_hand.add_asset(assets[2], dh["subcategories"])
    for _ in range(100):
        # Should update the time seperately
        if random.uniform(0, 1) < 0.1:
            symbol = random.choice([assets[0], assets[1], assets[2]])
            logger.warning(symbol)
            trade_type = random.choice([TradeType.LIMIT_BUY, TradeType.LIMIT_SELL])
            dynamic_trade = DynamicTrade(symbol, trade_type)
            dynamic_trade.percentage = random.normalvariate(0.3, 0.06)
            portfolio_hand.step(dynamic_trade)
        else:
            portfolio_hand.step()
        portfolio_hand.time.step()
    portfolio_hand.render()
    

if __name__ == "__main__":
    main()
