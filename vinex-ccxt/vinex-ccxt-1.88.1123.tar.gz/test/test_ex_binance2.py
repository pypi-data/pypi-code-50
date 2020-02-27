import ccxt
import config
import time
import utils.ccxt_utils as ccxt_utils
from pprint import pprint
###############################
# Public
###############################
# api = ccxt.probit()
# print(api.fetch_ticker('BTC/USDT'))


# ###############################
# # Private
# ###############################
# api = ccxt.probit(config.api_key['probit-midas'])
#
# for i in range(20):
#
#     print(f'>>> Turn {i}:', api.fetch_balance())
#
#     time.sleep(1*60)


# # api.create_order(symbol, 'limit', 'sell', amount, price)
# symbol = 'BTC/USDT'
# amount = 1
# price = 10000
#
# api.create_order(symbol, 'limit', 'sell', amount, price)


# Spot
# api = ccxt.binance2()

# Future
# api = ccxt.binance2({'options': { 'defaultType': 'futures' }})

# Margin
api_key = config.api_key['j-v-test']

api = ccxt.binance2({
    'apiKey': api_key['apiKey'],
    'secret': api_key['secret'],
    'options': { 'defaultType': 'margins' },
    # 'options': { 'defaultType': 'futures' },
})

# 1. Get Markets
# markets = api.fetch_markets()
# print(f'Markets: {len(markets)}\n{markets[0]}')

# print(api.fetch_ticker('BTC/USDT')['last'])


# 2. Get My Balances
# balance = api.fetch_balance()
# print(balance)
# print(balance['free'])
# print(balance['used'])

# pprint(ccxt_utils.fetch_balance(api))


# # 3. Get All Orders
# orders = api.fetch_orders('ETH/USDT')
# print(orders)

# # 4. Get Open Orders
orders = api.fetch_open_orders('BNB/USDT')
pprint(orders)

# print(len(api.fetch_orders('BNB/USDT')))
# print(len(api.fetch_open_orders('BNB/USDT')))
# print(len(api.fetch_closed_orders('BNB/USDT')))


# # 5. Get Order Detail
# order = api.fetch_order(id='351640418', symbol='BNB/USDT')
# print(order)


# 6. Get My Trades
# trades = api.fetch_my_trades(symbol='BNB/USDT')
# pprint(trades[-1])


# 7. Create Order
# Order Type: Limit
# order = api.create_order(symbol='BNB/USDT', type='limit', side='sell', amount=1, price=60)

# Order Type: Market
# order = api.create_order(symbol='BNB/USDT', type='market', side='sell', amount=1)

# Order Type: Stop Limit
# - STOP_LOSS_LIMIT
# - TAKE_PROFIT_LIMIT
# order = self.instance.create_order(symbol, type, side,  amount, limit_price, params)
# order = api.create_order(symbol='BNB/USDT', type='take_profit_limit', side='sell', amount=1, price=60, params={'stopPrice': 50})
# order = api.create_order(symbol='BNB/USDT', type='stop_loss_limit', side='sell', amount=1, price=10, params={'stopPrice': 11})


# Order Type: OCO
# order = api.create_order(symbol='BNB/USDT', type='stop_loss_limit', side='sell', amount=1, price=10, params={'stopPrice': 11})
#
# print(order)



# # 8. Cancel Order
# result = api.cancel_order(id='352590726', symbol='BNB/USDT')
# print(result)



