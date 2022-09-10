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
    # Place on order
    print(avg_price)
    # order = client.create_order(
    #     symbol='BNBBTC',
    #     side=SIDE_BUY,
    #     type=ORDER_TYPE_LIMIT,
    #     timeInForce=TIME_IN_FORCE_GTC,
    #     quantity=100,
    #     price='0.00001'
    #     )
    # order = client.order_limit_buy(
    #     symbol='BNBBTC',
    #     quantity=100,
    #     price='0.00001')

    # order = client.order_limit_sell(
    #     symbol='BNBBTC',
    #     quantity=100,
    #     price='0.00001')


if __name__ == "__main__":
    main()