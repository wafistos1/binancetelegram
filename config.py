# Important Bot Config
BOT_TOKEN = '5465308407:AAHZZYEfm6YczTIJM6ZeVtTzSCyj4rNv0RY'  # TODO Here is the token for bot binancewafistosBot
BINANCE_API_KEY = 'fCF5lwxphBnGxnwaIEIzC6uNdGrqU1lSyf9e6SSzQus96VjGmcGPBqrjKefjQq9I'
BINANCE_API_SECRET = 'VG4M2Q09GThCwhWxIZNGo5mkz7oXQJl2P42DgZVhT0gTeUlsW4ut8Af33NpUrXfg'
# BOT_NAME = 'MemberShip Bot'
# TRX_ADDRESS = 'TEJDUc8o9SittC81w4HuNXLV3TUbFZCXnh'
# BASE_URL = 'https://membot9.mybotpersonal.xyz/'


# Bot Buttons
PORTFOLIO_BTN = 'Portfolio'
BOT_CONFIG_BTN = 'Bot Configuration'
OPTIMIZED_CONFIG_BTN = 'Optimized Configs'
AUTO_TRADING = 'Auto Trading'


BACK = '↩️ Back'
MAIN_MENU = '↖️ Main Menu'
STRATEGIES = 'Strategies/General'
# STRATEGIES = 'Strategies'
STOP = 'Stop'
AUTO_TRADING_FILTERS = 'Auto Trading Filters'

MAX_TRADE = 'Max Trades'
BLACK_LIST_SYMBOLES = 'Blacklist Symbols'

DEFAULT_STOP = 'Default Stop'
STOP_LOSS_TIME = 'Stop Loss Time'

ENTRY_STRATEGY = 'Entry Strategy'
TAKE_PROFIT_STRATEGY = 'Take Profit Strategy'
AMOUNT_PER_TRADE = 'Amount per Trade'
CLOSE_TRADE_ON_TAKE_PROFIT = 'Close Trade on Profit'
FIRST_ENTRY_GRACE_PERCENTAGE = 'First Entry Grace Percentage'

PERCENTAGE = 'Percentage'
FIXED_USD_AMOUNT = 'Fixed USD Amount'

ADD_NEW_STRATEGY = 'Add Strategy'
AMOUNT_PER_TRADE_STATE = 'state Amount per Trade state'
FINAL_STATE = 'final_state'
PERCENTAGE_STATE = 'STATE PERCENTAGE'
FIX_USD_STATE = 'STATE FIX USD AMOUNT'
DELETE_STRATEGY = 'Delete stratgy owner'
UPDATE_STRATEGY = 'Update stratgy owner'
SECOND_UPDATE_STRATEGY = 'real_update_stratgy_owner'
SECOND_UPDATE = 'second'
# Start Messages
TRADING_MESSAGE_START = '''
<strong>Trading Panel </strong> \n\n
Welcome {}
Auto Trading Status: {}

Plz Choose an option

'''

BOT_CONFIG_START = f'''

<strong>{BOT_CONFIG_BTN}: </strong> \nChoose an option

'''

AUTO_TRADING_START = f'''
<strong>{AUTO_TRADING}:        </strong> 

Status: {None}

'''

PORTFOLIO_START = f'''
<strong> {PORTFOLIO_BTN} : </strong> \nTotal: 0.23434 BTC / 511.22 USD
My-Binance(0.23434 BTC / 511.22 USD)

'''

OPTIMISED_CONFIG_START = '''
<strong> Optimized Configs: </strong> \nOwner strategy List
Click on to Display strategy details

'''

STRATEGIES_START = f'''
<strong> {STRATEGIES}: </strong> \nChoose an option

'''

MAX_TRADE_START = f'''
<strong> {AUTO_TRADING_FILTERS} > {MAX_TRADE} </strong> \nChoose an option

'''

BLACK_LIST_SYMBOLES_START = f'''
<strong> {AUTO_TRADING_FILTERS} > {BLACK_LIST_SYMBOLES} </strong> \nChoose an option

'''

STOP_START = f'''
<strong>{STOP}:        </strong> \nStatus:    

'''

DEFAULT_STOP_START = f'''
<strong>{STOP} > {DEFAULT_STOP}      </strong> \nStatus:    

'''

STOP_LOSS_TIME_START = f'''
<strong>{STOP} > {STOP_LOSS_TIME}      </strong> \nStatus:    

'''


ENTRY_STRATEGY_START = f'''
<strong>{STRATEGIES} > {ENTRY_STRATEGY}      </strong> \nStatus:    

'''


TAKE_PROFIT_STRATEGY_START = f'''
<strong>{STRATEGIES} > {TAKE_PROFIT_STRATEGY}      </strong> \nStatus:    

'''

AMOUNT_PER_TRADE_START = f'''
<strong>{STRATEGIES} > {AMOUNT_PER_TRADE}      </strong> \nStatus:    

'''
CLOSE_TRADE_ON_TAKE_PROFIT_START = f'''
<strong>{STRATEGIES} > {CLOSE_TRADE_ON_TAKE_PROFIT}      </strong> \nStatus:    

'''
FIRST_ENTRY_GRACE_PERCENTAGE_START = f'''
<strong>{STRATEGIES} > {FIRST_ENTRY_GRACE_PERCENTAGE}      </strong> \nStatus:    

'''

PERCENTAGE_START = f'''
<strong>{STRATEGIES} > {AMOUNT_PER_TRADE} > {PERCENTAGE}      </strong> \nStatus:    

'''
FIXED_USD_AMOUNT_START = f'''
<strong>{STRATEGIES} > {AMOUNT_PER_TRADE} > {FIXED_USD_AMOUNT}      </strong> \nStatus:    

'''

FINAL_STATE_START = '''
<strong>Summary of strategy details</strong> \n:    
click on Yes to accept on no to return to the menu
NAME: {}\n
Entry Strategy: {}\n
Take Profit: {}\n
Close Trade on TP: {}\n
Stop loss Time: {}\n
Percentage: {}\n
Fix Amount USD: {}\n

'''

AMOUNT_PER_TRADE_STATE_START = f'''
<strong> CHOOSE ONE </strong> \n
:    

'''