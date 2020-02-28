#! coding:utf-8


class TradeConf(object):

    def __init__(self, trade_env):
        if trade_env == 'test':
            self.api_key = ""
            self.api_secret = ""
        elif trade_env == 'product':
            self.api_key = ""
            self.api_secret = ""

