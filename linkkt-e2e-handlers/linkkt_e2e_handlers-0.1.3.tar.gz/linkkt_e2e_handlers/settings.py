""" 
    Create a price handler. Used to do all price commands that run throughout the application.
    This price handler should use lists, as it will be faster to handle.
"""


from uuid import uuid1
from jamboree import Jamboree, DBHandler
from typing import Dict, Any, List


# NOTE: I'm probably going to have to separate everything here from

class SettingsHandler(DBHandler):
    """ Use this handler to manage the settings for things like data collection. """
    def __init__(self, limit=500):
        super().__init__()
        self.entity = "settings"
        self.required = {
            "organization": str,
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

    @limit.setter
    def limit(self, _limit):
        self._limit = _limit


    @property
    def tiingo_key(self):
        latest_key = self.latest_key("tiingo")
        return latest_key.get("key", "")

    @tiingo_key.setter
    def tiingo_key(self, _tiingo_key:str):
        self.save_key_information("tiingo", _tiingo_key, "")


    @property
    def main_tiingo_assets(self):
        """ Get the assets we're monitoring """
        api_name = "tiingo"
        exchange = "main"
        market = "us_stock"
        latest = self.latest_monitored_assets(api_name, exchange, market)
        return latest.get("assets", [])
    
    @main_tiingo_assets.setter
    def main_tiingo_assets(self, _assets):
        api_name = "tiingo"
        exchange = "main"
        market = "us_stock"

        if isinstance(_assets, str):
            self.add_asset(api_name, exchange, market, _assets)
        elif isinstance(_assets, list):
            self.add_assets(api_name, exchange, market, _assets)

    """ 
        ----------------------------------------------------------------------------------
        ------------------------------- Accessor Functions -------------------------------
        ----------------------------------------------------------------------------------
    """
    
    

    def latest_key(self, name):
        alt = {"detail": "key_info", "name": name}
        last_state = self.last(alt)
        last_state = last_state or {"key": "", "secret": "", "info": {}}
        return last_state

    
    def latest_monitored_assets(self, api_name:str, exchange:str, market:str):
        alt = {"detail": "assets", "api": api_name, "exchange": exchange, "market": market}
        latest = self.last(alt=alt)
        return latest

    """ 
        ----------------------------------------------------------------------------------
        ------------------------------- Counting Functions -------------------------------
        ----------------------------------------------------------------------------------
    """
    

    def complex_asset_count(self, api_name:str, exchange:str, market:str):
        alt = {"detail": "assets", "api": api_name, "exchange": exchange, "market": market}
        count = self.count(alt=alt)
        return count
    

    """ 
        --------------------------------------------------------------------------------
        ------------------------------- Saving Functions -------------------------------
        --------------------------------------------------------------------------------
    """

    def save_key_information(self, name:str, key:str, secret:str, info:Dict[str, Any]={}):
        alt = {"detail": "key_info", "name": name}
        monitored = {
            "key": key,
            "secret": secret,
            "info": info
        }
        self.save(monitored, alt=alt)


    def add_assets(self, api_name:str, exchange:str, market:str, assets:List[str]):
        """ Add a list of assets to monitor. Used for tracking multiple assets inside of a portfolio. """
        if len(assets) == 0:
            return
        
        latest = self.latest_monitored_assets(api_name, exchange, market)
        asset_list = latest.get("assets", [])
        for asset in assets:
            if asset not in asset_list:
                asset_list.append(asset)
        self.save_monitored_assets(api_name, exchange, market, asset_list)


    def add_asset(self, api_name:str, exchange:str, market:str, asset_name:str):
        """ Add an asset that will be monitored in an exchange"""
        if asset_name == "":
            return
        latest = self.latest_monitored_assets(api_name, exchange, market)
        asset_list = latest.get("assets", [])
        asset_list.append(asset_name)
        asset_list = list(set(asset_list))
        self.save_monitored_assets(api_name, exchange, market, asset_list)


    def save_monitored_assets(self, api_name:str, exchange:str, market:str, assets:list):
        """ Save monitored assets """
        alt = {"detail": "assets", "api": api_name, "exchange": exchange, "market": market}
        monitored = {
            "assets": assets
        }
        self.save(monitored, alt=alt)

    def _reset_tiingo_main(self):
        api_name = "tiingo"
        exchange = "main"
        market = "us_stock"

        if self.complex_asset_count(api_name, exchange, market) == 0:
            self.add_assets(api_name, exchange, market, [])

    def reset(self):
        """ No idea what goes here. But it should reset something."""

def main():
    setting_handler = SettingsHandler()
    jam = Jamboree()
    setting_handler['organization'] = "linkkt"
    setting_handler['live'] = False
    setting_handler.event = jam
    setting_handler.reset()
    setting_handler.tiingo_key = uuid1().hex
    # setting_handler.main_tiingo_assets = ["AAPL", "MSFT"]
    print(setting_handler.tiingo_key)
    print(setting_handler.main_tiingo_assets)


if __name__ == "__main__":
    main()