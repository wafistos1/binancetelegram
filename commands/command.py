from telebot import TeleBot, types
# from database.create_model import return_table_value, select_user, status_auto_trading, update_auto_trading
from database.data_pony import  (
    Amount_trade, 
    Entry_strategy,
    Fixed_usd_amount,
    Take_profit_strategy,
    First_entry_grace_percentage,
    Take_profit_strategy,
    Close_trade_on_take_profit,
    Blacklist_symbols,
    Max_trades,
    Stop_loss_timeout,
    Default_stop_loss,
    Binance,
    User,
    Owner,
    Strategy_user,
    Strategy_owner,
    Percentage,
    )

import config
import logging
from database.data_pony import (
    check_user,
    return_auto_trading, 
    return_table_value,
    return_owner_strat,
    list_owner_strat,
    )



# @bot.message_handler(commands=['start', 'help'])
def return_markup(table, back_btn):
    table_numbers = return_table_value(table)
    print('Table max trade: ', table_numbers)
    markup = types.InlineKeyboardMarkup()
    lis_btn = []
    for i, t in enumerate(table_numbers):
        t = str(t)
        btnt = types.InlineKeyboardButton(text=t, callback_data=f'{back_btn}-{t}')
        lis_btn.append(btnt)
        if i % 2 :
            markup.add(lis_btn[0], lis_btn[1])
            lis_btn.clear()
        elif i == len(table_numbers)-1:
                markup.add(btnt)
                lis_btn.clear()
    return markup

def return_markup1(table, back_btn, user_id, owner_id):
    table_numbers = list_owner_strat(table, user_id, owner_id)
    print('Table max trade: ', table_numbers)
    markup = types.InlineKeyboardMarkup()
    lis_btn = []
    for i, t in enumerate(table_numbers):
        t = str(t)
        btnt = types.InlineKeyboardButton(text=t, callback_data=f'owner_strat-{back_btn}--{t}')
        lis_btn.append(btnt)
        if i % 2 :
            markup.add(lis_btn[0], lis_btn[1])
            lis_btn.clear()
        elif i == len(table_numbers)-1:
                markup.add(btnt)
                lis_btn.clear()
    return markup

def _start(message, bot):
    print(message.data)
    user_id = 3
    owner_id = 2
    
    
    
    try:
        message_return = message.data.split('-')[1]
        print(message_return)
        if message_return == 'On_autotrading':
            print('Change status auto trading On')
            user = return_auto_trading(user_id, change='True' )
            
        else:
            user = return_auto_trading(user_id, change='False' )
    except:
        pass
    user_name, status = check_user(user_id, owner_id)
    # user = select_user(User, user_id, owner_id)
    # auto_trading_status = status_auto_trading(user_id)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.PORTFOLIO_BTN, callback_data=config.PORTFOLIO_BTN)
    btn2 = types.InlineKeyboardButton(text=config.OPTIMIZED_CONFIG_BTN, callback_data=config.OPTIMIZED_CONFIG_BTN)
    btn3 = types.InlineKeyboardButton(text=config.BOT_CONFIG_BTN, callback_data= config.BOT_CONFIG_BTN)
    btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING, callback_data=config.AUTO_TRADING)

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    # ge_text()
    bot.edit_message_text(chat_id=message.from_user.id,
                            message_id=message.message.message_id,
                            text=config.TRADING_MESSAGE_START.format(user_name, status), 
                            parse_mode='HTML',
                            reply_markup=markup
                            )


def optimised_config(message: types.Message, bot : TeleBot):
    print('optimised_config')
    
    owner_id = 2
    user_id = 3
    # data = return_owner_strat(Strategy_owner, owner_id, user_id)
    # name = data['name']
    # take_profit = data['take_profit']
    # first_entry_grace = data['first_entry_grace']
    # entry_strategy = data['entry_strategy']
    
    markup = return_markup1(Strategy_owner, config.STRATEGIES, 3, 2)
    
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.MAIN_MENU)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.OPTIMISED_CONFIG_START,
                          parse_mode='HTML',
                          reply_markup=markup
                          )


def auto_trading(message: types.CallbackQuery, bot : TeleBot):
    print('auto_trading')
    owner_id = 2
    user_id = 3
    user_name, status = check_user(user_id, owner_id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    status = return_auto_trading(3)
    print('Status in auto_trading', type(status))
    if status:
        btn1 = types.InlineKeyboardButton(text='👉On👈', callback_data=f'{config.MAIN_MENU}-On_autotrading',)
        btn2 = types.InlineKeyboardButton(text='Off', callback_data=f'{config.MAIN_MENU}-Off_autotrading',)
    else:
        btn1 = types.InlineKeyboardButton(text='On', callback_data=f'{config.MAIN_MENU}-On_autotrading',)
        btn2 = types.InlineKeyboardButton(text='👉Off👈', callback_data=f'{config.MAIN_MENU}-Off_autotrading',)

    btn4 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)

    markup.add(btn1, btn2)
    markup.add(btn4)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.AUTO_TRADING_START.format(status),
                          parse_mode='HTML',
                          reply_markup=markup
                          )


def bot_configuration(message: types.CallbackQuery, bot : TeleBot): #Todo Done
    print('Bot config.')
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.STRATEGIES, callback_data=config.STRATEGIES)
    # btn2 = types.InlineKeyboardButton(text=config.STRATEGIES, callback_data=config.STRATEGIES)
    btn3 = types.InlineKeyboardButton(text=config.STOP, callback_data=config.STOP)
    btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING_FILTERS, callback_data=config.AUTO_TRADING_FILTERS)
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.BACK)
    btn6 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU)
    markup.add(btn1)
    markup.add(btn3, btn4)
    markup.add(btn6)
    # bot.delete_message(chat_id=message.message.chat.id,message_id=message.message.message_id)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.BOT_CONFIG_START,
                          parse_mode='HTML',
                          reply_markup=markup
                          )


def auto_trading_filters(message: types.CallbackQuery, bot : TeleBot):
    print('auto_trading')
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text=config.MAX_TRADE, callback_data=config.MAX_TRADE,)
    btn2 = types.InlineKeyboardButton(text=config.BLACK_LIST_SYMBOLES, callback_data=config.BLACK_LIST_SYMBOLES,)
    btn3 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.BOT_CONFIG_BTN,)
    btn4 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn2)
    markup.add(btn4, btn3 )
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.AUTO_TRADING_START,
                          parse_mode='HTML',
                          reply_markup=markup
                          )



def portfolio(message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('portfolio')
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.PORTFOLIO_START,
                          parse_mode='HTML',
                          reply_markup=markup
                          )


def max_trade (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('max_trade')
    table_numbers = return_table_value(Max_trades)
    print('Table max trade: ', table_numbers)
    markup = types.InlineKeyboardMarkup()
    lis_btn = []
    for i, t in enumerate(table_numbers):
        t = str(t)
        btnt = types.InlineKeyboardButton(text=t, callback_data=f'{config.AMOUNT_PER_TRADE}-{t}')
        lis_btn.append(btnt)
        if i % 2 :
            markup.add(lis_btn[0], lis_btn[1])
            lis_btn.clear()
        elif i == len(table_numbers)-1:
                markup.add(btnt)
                lis_btn.clear()
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.AUTO_TRADING_FILTERS)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=config.MAX_TRADE_START, parse_mode='HTML', reply_markup=markup)


def black_list_symboles (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('black_list_symboles')
    
    markup = return_markup(Blacklist_symbols, config.AUTO_TRADING_FILTERS)
    
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.AUTO_TRADING_FILTERS)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.BLACK_LIST_SYMBOLES_START,
                          parse_mode='HTML',
                          reply_markup=markup
                          )


def stop(message: types.CallbackQuery, bot : TeleBot):
    print('stop')
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text=config.DEFAULT_STOP, callback_data=config.DEFAULT_STOP,)
    btn2 = types.InlineKeyboardButton(text=config.STOP_LOSS_TIME, callback_data=config.STOP_LOSS_TIME,)
    btn3 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.BOT_CONFIG_BTN,)
    btn4 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn2)
    markup.add(btn4, btn3 )
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.STOP_START,
                          parse_mode='HTML',
                          reply_markup=markup
                          )


def default_stop (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('default_stop')
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.STOP)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.BLACK_LIST_SYMBOLES_START,
                          parse_mode='HTML', reply_markup=markup
                          )
 
    
def stop_loss_time (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('default_stop')
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.STOP)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.BLACK_LIST_SYMBOLES_START,
                          parse_mode='HTML', reply_markup=markup
                          )


def stategy (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('stategy', message.data)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.AMOUNT_PER_TRADE, callback_data=config.AMOUNT_PER_TRADE)
    btn2 = types.InlineKeyboardButton(text=config.ENTRY_STRATEGY, callback_data=config.ENTRY_STRATEGY)
    btn3 = types.InlineKeyboardButton(text=config.TAKE_PROFIT_STRATEGY, callback_data=config.TAKE_PROFIT_STRATEGY)
    btn4 = types.InlineKeyboardButton(text=config.CLOSE_TRADE_ON_TAKE_PROFIT, callback_data=config.CLOSE_TRADE_ON_TAKE_PROFIT)
    btn5 = types.InlineKeyboardButton(text=config.FIRST_ENTRY_GRACE_PERCENTAGE, callback_data=config.FIRST_ENTRY_GRACE_PERCENTAGE)
    
    btn6 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.BOT_CONFIG_BTN)
    btn7 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4, btn5)
    markup.add(btn7, btn6)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.STRATEGIES_START,
                          parse_mode='HTML', reply_markup=markup
                          )
    
    
def entry_strategy (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('entry_strategy', message.data)
    markup = return_markup(Entry_strategy, config.STRATEGIES)
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.STRATEGIES)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.ENTRY_STRATEGY_START,
                          parse_mode='HTML', reply_markup=markup
                          )


def take_profit_strategy (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('take_profit_strategy')
    markup = return_markup(Take_profit_strategy, config.STRATEGIES)
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.STRATEGIES)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.TAKE_PROFIT_STRATEGY_START,
                          parse_mode='HTML', reply_markup=markup
                          )

 
def amount_per_trade (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('amount_per_trade', message.data)
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.PERCENTAGE, callback_data=config.PERCENTAGE)
    btn2 = types.InlineKeyboardButton(text=config.FIXED_USD_AMOUNT, callback_data=config.FIXED_USD_AMOUNT)
    btn3 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.STRATEGIES)
    btn4 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn2)
    markup.add(btn4, btn3)
    
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.AMOUNT_PER_TRADE_START,
                          parse_mode='HTML', reply_markup=markup
                          )


def close_trade_on_take_profit (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('close_trade_on_take_profit')
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.STRATEGIES)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.CLOSE_TRADE_ON_TAKE_PROFIT_START,
                          parse_mode='HTML', reply_markup=markup
                          )


def first_entry_grace_percentage (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('fist_entry_grace_percentage')
    table_numbers = return_table_value(First_entry_grace_percentage)
    print('Table: ', table_numbers)
    markup = return_markup(First_entry_grace_percentage, config.STRATEGIES)
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.STRATEGIES)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.FIRST_ENTRY_GRACE_PERCENTAGE_START,
                          parse_mode='HTML', reply_markup=markup
                          )


def percentage(message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    
    markup = return_markup(Percentage, config.AMOUNT_PER_TRADE)
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.AMOUNT_PER_TRADE)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.PERCENTAGE_START,
                          parse_mode='HTML', reply_markup=markup
                        )


def fixed_usd_amount(message: types.CallbackQuery, bot : TeleBot):  #todo DONE

    print('fixed_usd_amount')
    
    table_numbers = return_table_value(Fixed_usd_amount)
    print('Table: ', table_numbers)
    markup = types.InlineKeyboardMarkup()
    for t in table_numbers:
        btnt = types.InlineKeyboardButton(text=t, callback_data=f'{config.AMOUNT_PER_TRADE}-{t}')
        markup.add(btnt)
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.AMOUNT_PER_TRADE)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.FIXED_USD_AMOUNT_START,
                          parse_mode='HTML', reply_markup=markup
                          )


def display_strategy_owner(message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    
    owner_id = 2
    user_id = 3
    print('Message display: ', message.data)
    strategy_name = message.data.split('--')[-1]
    data = return_owner_strat(strategy_name, owner_id, user_id)
    name = data['name']
    take_profit = data['take_profit']
    first_entry_grace = data['first_entry_grace']
    entry_strategy = data['entry_strategy']
    
    markup = types.InlineKeyboardMarkup()
    
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.OPTIMIZED_CONFIG_BTN)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text= f'''
                          <strong> Strategy Owner: </strong> 
                          \nName: <strong>{name.upper()} </strong>
                          \nTake Profit: <strong>{take_profit.upper()} </strong> 
                          \nFirst Entry Grace: <strong>{first_entry_grace.upper()} </strong> 
                          \nEntry Strategy: <strong>{entry_strategy.upper()} </strong>
                            
                        ''',
                          parse_mode='HTML', reply_markup=markup
                        )