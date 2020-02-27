# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange
import math
from ccxt.base.errors import ExchangeError


class coinmarketcap (Exchange):

    def describe(self):
        return self.deep_extend(super(coinmarketcap, self).describe(), {
            'id': 'coinmarketcap',
            'name': 'CoinMarketCap',
            'rateLimit': 10000,
            'version': 'v1',
            'countries': ['US'],
            'has': {
                'CORS': True,
                'privateAPI': False,
                'createOrder': False,
                'createMarketOrder': False,
                'createLimitOrder': False,
                'cancelOrder': False,
                'editOrder': False,
                'fetchBalance': False,
                'fetchOrderBook': False,
                'fetchL2OrderBook': False,
                'fetchOHLCV': False,
                'fetchTrades': False,
                'fetchTickers': True,
                'fetchCurrencies': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/28244244-9be6312a-69ed-11e7-99c1-7c1797275265.jpg',
                'api': {
                    'public': 'https://api.coinmarketcap.com',
                    'files': 'https://files.coinmarketcap.com',
                    'charts': 'https://graph.coinmarketcap.com',
                },
                'www': 'https://coinmarketcap.com',
                'doc': 'https://coinmarketcap.com/api',
            },
            'requiredCredentials': {
                'apiKey': False,
                'secret': False,
            },
            'api': {
                'files': {
                    'get': [
                        'generated/stats/global.json',
                    ],
                },
                'graphs': {
                    'get': [
                        'currencies/{name}/',
                    ],
                },
                'public': {
                    'get': [
                        'ticker/',
                        'ticker/{id}/',
                        'global/',
                    ],
                },
            },
            'currencyCodes': [
                'AUD',
                'BRL',
                'CAD',
                'CHF',
                'CNY',
                'EUR',
                'GBP',
                'HKD',
                'IDR',
                'INR',
                'JPY',
                'KRW',
                'MXN',
                'RUB',
                'USD',
                'BTC',
                'ETH',
                'LTC',
            ],
        })

    async def fetch_order_book(self, symbol, limit=None, params={}):
        raise ExchangeError('Fetching order books is not supported by the API of ' + self.id)

    def currency_code(self, base, name):
        currencies = {
            'ACChain': 'ACChain',
            'AdCoin': 'AdCoin',
            'BatCoin': 'BatCoin',
            'Bitgem': 'Bitgem',
            'BlazeCoin': 'BlazeCoin',
            'BlockCAT': 'BlockCAT',
            'Blocktrade Token': 'Blocktrade Token',
            'Catcoin': 'Catcoin',
            'CanYaCoin': 'CanYaCoin',  # conflict with CAN(Content and AD Network)
            'Comet': 'Comet',  # conflict with CMT(CyberMiles)
            'CPChain': 'CPChain',
            'CrowdCoin': 'CrowdCoin',  # conflict with CRC CryCash
            'Cubits': 'Cubits',  # conflict with QBT(Qbao)
            'DAO.Casino': 'DAO.Casino',  # conflict with BET(BetaCoin)
            'E-Dinar Coin': 'E-Dinar Coin',  # conflict with EDR Endor Protocol and EDRCoin
            'EDRcoin': 'EDRcoin',  # conflict with EDR Endor Protocol and E-Dinar Coin
            'ENTCash': 'ENTCash',  # conflict with ENT(Eternity)
            'FairGame': 'FairGame',
            'Fabric Token': 'Fabric Token',
            'GET Protocol': 'GET Protocol',
            'Global Tour Coin': 'Global Tour Coin',  # conflict with GTC(Game.com)
            'GuccioneCoin': 'GuccioneCoin',  # conflict with GCC(Global Cryptocurrency)
            'HarmonyCoin': 'HarmonyCoin',  # conflict with HMC(Hi Mutual Society)
            'Harvest Masternode Coin': 'Harvest Masternode Coin',  # conflict with HC(HyperCash)
            'HOT Token': 'HOT Token',
            'Hydro Protocol': 'Hydro Protocol',  # conflict with HOT(Holo)
            'Huncoin': 'Huncoin',  # conflict with HNC(Helleniccoin)
            'iCoin': 'iCoin',
            'Infinity Economics': 'Infinity Economics',  # conflict with XIN(Mixin)
            'KingN Coin': 'KingN Coin',  # conflict with KNC(Kyber Network)
            'LiteBitcoin': 'LiteBitcoin',  # conflict with LBTC(LightningBitcoin)
            'Maggie': 'Maggie',
            'IOTA': 'IOTA',  # a special case, most exchanges list it as IOTA, therefore we change just the Coinmarketcap instead of changing them all
            'NetCoin': 'NetCoin',
            'PCHAIN': 'PCHAIN',  # conflict with PAI(Project Pai)
            'Polcoin': 'Polcoin',
            'PutinCoin': 'PutinCoin',  # conflict with PUT(Profile Utility Token)
            'Rcoin': 'Rcoin',  # conflict with RCN(Ripio Credit Network)
        }
        return self.safe_value(currencies, name, base)

    async def fetch_markets(self, params={}):
        request = {
            'limit': 0,
        }
        response = await self.publicGetTicker(self.extend(request, params))
        result = []
        for i in range(0, len(response)):
            market = response[i]
            currencies = self.currencyCodes
            for j in range(0, len(currencies)):
                quote = currencies[j]
                quoteId = quote.lower()
                baseId = market['id']
                base = self.currency_code(market['symbol'], market['name'])
                symbol = base + '/' + quote
                id = baseId + '/' + quoteId
                result.append({
                    'id': id,
                    'symbol': symbol,
                    'base': base,
                    'quote': quote,
                    'baseId': baseId,
                    'quoteId': quoteId,
                    'info': market,
                })
        return result

    async def fetch_global(self, currency='USD'):
        await self.load_markets()
        request = {}
        if currency:
            request['convert'] = currency
        return await self.publicGetGlobal(request)

    def parse_ticker(self, ticker, market=None):
        timestamp = self.safe_timestamp(ticker, 'last_updated')
        if timestamp is None:
            timestamp = self.milliseconds()
        change = self.safe_float(ticker, 'percent_change_24h')
        last = None
        symbol = None
        volume = None
        if market is not None:
            symbol = market['symbol']
            priceKey = 'price_' + market['quoteId']
            last = self.safe_float(ticker, priceKey)
            volumeKey = '24h_volume_' + market['quoteId']
            volume = self.safe_float(ticker, volumeKey)
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': None,
            'low': None,
            'bid': None,
            'bidVolume': None,
            'ask': None,
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': change,
            'average': None,
            'baseVolume': None,
            'quoteVolume': volume,
            'info': ticker,
        }

    async def fetch_tickers(self, currency='USD', params={}):
        await self.load_markets()
        request = {
            'limit': 10000,
        }
        if currency:
            request['convert'] = currency
        response = await self.publicGetTicker(self.extend(request, params))
        result = {}
        for t in range(0, len(response)):
            ticker = response[t]
            currencyId = currency.lower()
            id = ticker['id'] + '/' + currencyId
            symbol = id
            market = None
            if id in self.markets_by_id:
                market = self.markets_by_id[id]
                symbol = market['symbol']
            result[symbol] = self.parse_ticker(ticker, market)
        return result

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'convert': market['quote'],
            'id': market['baseId'],
        }
        response = await self.publicGetTickerId(self.extend(request, params))
        ticker = response[0]
        return self.parse_ticker(ticker, market)

    async def fetch_currencies(self, params={}):
        request = {
            'limit': 0,
        }
        response = await self.publicGetTicker(self.extend(request, params))
        result = {}
        for i in range(0, len(response)):
            currency = response[i]
            id = self.safe_string(currency, 'symbol')
            name = self.safe_string(currency, 'name')
            # todo: will need to rethink the fees
            # to add support for multiple withdrawal/deposit methods and
            # differentiated fees for each particular method
            precision = 8  # default precision, todo: fix "magic constants"
            code = self.currency_code(id, name)
            result[code] = {
                'id': id,
                'code': code,
                'info': currency,
                'name': name,
                'active': True,
                'fee': None,  # todo: redesign
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': math.pow(10, -precision),
                        'max': math.pow(10, precision),
                    },
                    'price': {
                        'min': math.pow(10, -precision),
                        'max': math.pow(10, precision),
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                    'withdraw': {
                        'min': None,
                        'max': None,
                    },
                },
            }
        return result

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api] + '/' + self.version + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if query:
            url += '?' + self.urlencode(query)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    async def request(self, path, api='public', method='GET', params={}, headers=None, body=None):
        response = await self.fetch2(path, api, method, params, headers, body)
        if 'error' in response:
            if response['error']:
                raise ExchangeError(self.id + ' ' + self.json(response))
        return response
