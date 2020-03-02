# -*- coding: utf-8 -*-


class CoinPair:
    """ 币对处理类 """

    def __init__(self, trade_coin='', base_coin=''):
        self.trade_coin = trade_coin.upper()
        self.base_coin = base_coin.upper()

    def formatted(self, sep='/'):
        """获取格式化的币对

        Parameters
        ----------
        sep : str, optional
            分割符, by default '/'
        """
        return "{}{}{}".format(self.trade_coin, sep, self.base_coin)

    @property
    def estimated_value_of_base_coin(self):
        """ 以粗略的价格估算本位币价格 """
        base_coin = self.base_coin.upper()
        if base_coin in ['USDT', 'USD']:
            return 1
        if base_coin in ['ETH']:
            return 200
        if base_coin in ['BTC']:
            return 9000

        # default
        return 1
