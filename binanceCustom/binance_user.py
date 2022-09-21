from binance import Client
from binance.enums import *
import pandas as pd 

api_key = 'gqbq6rfwD8fVDbaF3rW8eshP32X58gjyYnkjOp1QIN1e02AZ6AWUnM5NGkUFKLzH'
api_secret = 'JdqRK073aBIGPsbDCf1yLUE4wXXz1W74PzhowqjiTugKI2PqTGDIfJY1dI7JZyFy'

def main():
    client = Client(api_key, api_secret)

    res = client.get_exchange_info()
    #Get all orders
    orders = client.get_all_orders(symbol='BNBBTC', limit=10)
    prices = client.get_all_tickers()
    avg_price = client.get_avg_price(symbol='BNBBTC')
    info = client.get_symbol_info('BTCUSDT')
    # Place on order
    print(info['filters'][2]['minQty'])
    
    # for price in prices:
    #     print(price['symbol'])
    # order = client.create_order(
    #     symbol='BTC',
    #     side=SIDE_BUY,
    #     type=ORDER_TYPE_LIMIT,
    #     timeInForce=TIME_IN_FORCE_GTC,
    #     quantity=100,
    #     price='0.00001'
    #     )
    # order = client.order_limit_buy(
    #     symbol='BTCUSDT',
    #     quantity=10,
    #     price='0.00001')

    # order = client.order_limit_sell(
    #     symbol='BTCUSDT',
    #     quantity=10,
    #     price='0.00001')

    order = client.create_test_order(
    symbol='BTCUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=0.0001000,
    price='10')
    print(order)

if __name__ == "__main__":
    main()