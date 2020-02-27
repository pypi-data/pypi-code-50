# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.gdax import gdax


class coinbaseprime (gdax):

    def describe(self):
        return self.deep_extend(super(coinbaseprime, self).describe(), {
            'id': 'coinbaseprime',
            'name': 'Coinbase Prime',
            'urls': {
                'test': 'https://api-public.sandbox.prime.coinbase.com',
                'logo': 'https://user-images.githubusercontent.com/1294454/44539184-29f26e00-a70c-11e8-868f-e907fc236a7c.jpg',
                'api': 'https://api.prime.coinbase.com',
                'www': 'https://prime.coinbase.com',
                'doc': 'https://docs.prime.coinbase.com',
                'fees': 'https://support.prime.coinbase.com/customer/en/portal/articles/2945629-fees?b_id=17475',
            },
        })
