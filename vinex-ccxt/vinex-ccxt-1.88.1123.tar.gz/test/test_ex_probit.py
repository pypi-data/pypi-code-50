import ccxt
import config


###############################
# Public
###############################
# api = ccxt.probit()
# print(api.fetch_ticker('BTC/USDT'))


###############################
# Private
###############################
api = ccxt.probit(config.api_key['probit-test'])

print(api.fetch_balance())


# # api.create_order(symbol, 'limit', 'sell', amount, price)
# symbol = 'BTC/USDT'
# amount = 1
# price = 10000
#
# api.create_order(symbol, 'limit', 'sell', amount, price)
