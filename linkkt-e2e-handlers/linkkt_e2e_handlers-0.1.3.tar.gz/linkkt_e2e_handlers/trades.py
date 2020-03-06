""" 
    Create a price handler. Used to do all price commands that run throughout the application.
    This price handler should use lists, as it will be faster to handle.
"""

from jamboree import Jamboree, DBHandler
from crayons import (magenta)


# # TODO: Rethink design here and come back to this.

class TradeHandler(DBHandler):
    def __init__(self, limit=500):
        super().__init__()
        self.entity = "_trades"
        self.required = {
            "episode": str,
            "exchange": str,
            "live": bool
        }
        self._limit = 500
    

    """ 
        ---------------------------------------------------------------------------------
        ----------------------------------- Properties ----------------------------------
        ---------------------------------------------------------------------------------
    """

    @property
    def limit(self):
        return self._limit

    def limit(self, _limit):
        self._limit = _limit


    """ 
        ----------------------------------------------------------------------------------
        ------------------------------- Accessor Functions -------------------------------
        ----------------------------------------------------------------------------------
    """


    def save_trade(self, trade, user_id):
        """ Save trade in 2 ways to make it easy to access those trades later. """
        asset_alt = {}
        user_alt = {}
        exchange_alt = {}
        specified_trade_alt = {} # a way to get specific trade information.
        pass
    
    
    def latest_trade(self):
        return {}



    def latest_trade_by_user(self):
        return {}


    def latest_trade_by_asset(self):
        return {}


    

    

    
    """ 
        ----------------------------------------------------------------------------------
        ------------------------------- Counting Functions -------------------------------
        ----------------------------------------------------------------------------------
    """
    

    def trade_count(self, alt={}) -> int:
        """ Get the number of trades we have active in the given exchange. """
        count = self.count(alt=alt)
        return count
    
    def trade_exchange_count(self, exchange:str):
        alt = {"exchange": exchange}
        count = self.count(alt=alt)
        return count
    
    def trade_user_count(self):
        pass
#     def price_count(self) -> int:
#         count = self.count()
#         return count

#     """ 
#         --------------------------------------------------------------------------------
#         ------------------------------- Saving Functions -------------------------------
#         --------------------------------------------------------------------------------
#     """



#     def add_assets(self, assets:List[str]):
#         """ Add a list of assets to monitor. Used for tracking multiple assets inside of a portfolio. """
#         if len(assets) == 0:
#             return
#         asset_list = self.assets
#         for _ass in assets:
#             asset_list.append(_ass)
        

#         self.save_monitored_assets(asset_list)

#     def add_asset(self, asset_name:str):
#         if asset_name == "":
#             return

#         asset_list = self.assets
#         asset_list.append(asset_name)
#         self.save_monitored_assets(asset_list)

#     def save_monitored_assets(self, assets:list):
#         alt = {"detail": "assets"}
#         monitored = {
#             "assets": assets
#         }
#         self.save(monitored, alt=alt)

#     def save_single_bar(self, bar):
#         self.save(bar)

#     def save_bar_multi_bar(self, name:str, bars:List[Dict]):
#         alt = {"asset": name}
#         if len(bars) == 0:
#             return
        
#         query = copy.copy(self._query)
#         episode = query.get("episode")
#         exchange = query.get("exchange")
#         print(f"Saving bars for {name}-{episode}-{exchange}")
#         self.save_many(bars, alt=alt) # This will yield a flag, because why not?

#     """ 
#         --------------------------------------------------------------------------------
#         ---------------------------------- Misc ----------------------------------------
#         --------------------------------------------------------------------------------
#     """


#     def generate_price_bars(self, name, _type, _len, base_price):
#         price = generate_super_price(base_price, _type, _len)
#         ps = len(price)
#         vol_multiplier = random.uniform(2, 20)
#         open_multiplier = np.absolute(np.random.normal(1, 0.05, size=ps))
#         high_multiplier = np.absolute(np.random.normal(1.12, 0.05, size=ps))
#         low_multiplier =  np.absolute(np.random.normal(0.92, 0.05, size=ps))
#         noise = np.absolute(
#             np.random.normal(1, 0.2, size=ps)
#         )


#         volume = (noise * price) * vol_multiplier
#         _open = price * open_multiplier
#         high = high_multiplier * price
#         _low = low_multiplier * price

#         bars = []
#         current_time = maya.now()._epoch
#         hourly_multiplier = 3600
#         for _ in list(range(ps)).sort(reverse=True):
#             bar = {
#                 "open": float(_open[_]),
#                 "close": float(price[_]),
#                 "high": float(high[_]),
#                 "volume": float(volume[_]),
#                 "low": float(_low[_]),
#                 "time": float(current_time + (_*hourly_multiplier))
#             }
#             bars.append(bar)
#         # # Create a bunch of bars here
#         self.asset_bars[name] = bars




#     def generate(self, starting_min=50, starting_max=2000, is_varied=True, excluded_assets=[]):
#         """ Generate price bars for assets """
#         assets = self.assets
#         if len(assets) == 0:
#             return
        
#         for excluded in excluded_assets:
#             assets.remove(excluded)
        
#         # Generate bars
#         mid_point = ((starting_min + starting_max)/2)
#         std = (mid_point/4)

        
#         dask_tasks = []
#         for asset in assets:
#             base_price = random.normalvariate(mid_point, std)
#             # price_quote = f"Create prices for {asset}, {base_price}"
#             _type = random.choice(["GBM", "HESTON", "MERTON"])
#             dask_task = dask.delayed(self.generate_price_bars)(asset, _type, 4000, base_price)
#             dask_tasks.append(dask_task) 
#         dask.compute(*dask_tasks)
#         for asset in assets:
#             self.save_bar_multi_bar(asset, self.asset_bars[asset])
         
#     def _reset_assets(self):
#         # Set the first asset
#         count = self.asset_count()
#         if count == 0:
#             # Save that we have no new assets
#             self.save_monitored_assets([])



#     """ ---------------------------------------------------------------------------
#         ---------------------------- Live Data Handling---------------------------- 
#         ---------------------------------------------------------------------------
#     """
    
#     def save_live_price(self, data:dict):
#         """ Save the live price"""
#         alt = {}
#         pass


    
#     """ ---------------------------------------------------------------------------
#         ---------------------------- RL-Like Functions ---------------------------- 
#         ---------------------------------------------------------------------------
#     """

#     def step(self):
#         """ """
#         pass
    
#     def get_step(self):
#         """
#             # GET STEP
#             ---
#             Get all of the data for the latest step without pushing it forward.

#             Only works when live is set to false. Should only use it when live is set to false. 
#         """
#         pass

#     def reset(self):
#         """ No idea what goes here. But it should reset something."""
#         self._reset_assets()

# def main():
#     asset_list = ["BTC", "ATL", "TRX", "ETH", "BCH", "XRP", "LTC", "EOS", "ADA", "XMR", "LINK", "HT"]
#     price_handler = PriceHandler()
#     jam = Jamboree()
#     # This live variable locks certain commands, and allows us to query faster. 
#     price_handler['episode'] = uuid.uuid4().hex # set this to live if we're trying to use live prices.
#     price_handler['exchange'] = "binance"
#     price_handler['live'] = False
#     price_handler.event = jam
#     price_handler.add_assets(asset_list)
#     price_handler.reset()
    

#     price_handler.generate()
#     print(price_handler.assets)


# if __name__ == "__main__":
#     main()