from telebot import TeleBot, types
from telebot.handler_backends import State, StatesGroup

from database.create_model import CloseTradeOnTakeProfit, EntryStrategy, FixedUsdAmount, StopLossTimeout, TakeProfitStrategy
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
    Users,
    Memberships,
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
    save_strategy,
    )
from commands.command import return_markup1
from telebot.callback_data import CallbackData, CallbackDataFilter
class strategyState(StatesGroup):
    
    name_strategy = State()
    entry_strategy  = State()
    take_profit_strategy = State()
    stop_loss_strategy = State()
    close_trade_strategy = State()
    amount_per_trade_percentage_strategy  = State()
    amount_per_trade_fix_strategy  = State()
    final = State()

data = {}



products_factory = CallbackData('product_id', prefix='products')


def return_markup_state(table, back_btn):
    table_numbers = return_table_value(table)
    print('Table max trade: ', table_numbers)
    markup = types.InlineKeyboardMarkup()
    lis_btn = []
    for i, t in enumerate(table_numbers):
        t = str(t)
        btnt = types.InlineKeyboardButton(text=t, callback_data=f'state-{back_btn}-{t}')
        # btnt = types.InlineKeyboardButton(text='toto', callback_data=f'toto')
        lis_btn.append(btnt)
        if i % 2 :
            markup.add(lis_btn[0], lis_btn[1])
            lis_btn.clear()
        elif i == len(table_numbers)-1:
                markup.add(btnt)
                lis_btn.clear()
    return markup


def Create_strategy_state(message: types.CallbackQuery, bot: TeleBot):
    bot.set_state(user_id=message.from_user.id, state=strategyState.name_strategy, chat_id=message.message.chat.id)
    bot.send_message(message.message.chat.id, 
                     '<b> 💹 Welcome to the Creation Section of Strategy 💹</b>\n\n<b>Plz Enter Strategy Name\n\n</b>', 
                     parse_mode='HTML')
 

def Strategy_name_state(message: types.CallbackQuery, bot : TeleBot): # Name
    
    markup = return_markup_state(Entry_strategy, config.ENTRY_STRATEGY)
    global data
    data['name'] = message.text
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #     data['name'] = message.text
    # text = '\n- '.join(list_entry_strategy)
    # bot.set_state(user_id=message.from_user.id, state=strategyState.entry_strategy, chat_id=message.chat.id)
    print('MEs id: ',message.text)
    # print('MEs id: ', message.message_id,)
    print('User id: ', message.from_user.id)
    print('Chat id: ', message.chat.id)
    bot.send_message(
        chat_id=message.chat.id,
        text='Please choose ENTRY STRATEGY',#{text}', 
        parse_mode='HTML',
        reply_markup=markup,

                 )


def Entry_strategy_state(message: types.CallbackQuery, bot : TeleBot): #  First entry grace
    print('Entry State')
    # with bot.retrieve_data(user_id=message.from_user.id, chat_id=message) as data:
    global data
    data['entry_strategy'] = message.data.split('-')[2]
        # print("message entry: ", entry_strategy)
        # data['entry_strategy'] = entry_strategy
    markup = return_markup_state(Take_profit_strategy, config.TAKE_PROFIT_STRATEGY)
    # entry_strategy = message.data.split('-')[2]
    print('User id name: ', data['name'])
    print('Chat id strategy: ', data['entry_strategy'])
    
    # bot.set_state(user_id=message.from_user.id, state=strategyState.take_profit_strategy, chat_id=message.chat.id)

    bot.send_message(
        chat_id=message.message.chat.id,
        text= f'<b>Enter  TAKE PROFIT</b>',#\n{text1}', 
        parse_mode='HTML',
        reply_markup=markup,
                 )

def Take_profit_state(message: types.Message, bot : TeleBot): #  Take profit
    markup = return_markup_state(Stop_loss_timeout, config.STOP_LOSS_TIME)
    take_profit = message.data.split('-')[2]
    global data
    data['take_profit'] = take_profit
    # with bot.retrieve_data(message.from_user.id, message.message.chat.id) as data:
    #     data['take_profit'] = take_profit
    bot.send_message(
        chat_id=message.message.chat.id,
        text= f'<b>Enter  STOP LOSS</b>',#\n{text1}', 
        parse_mode='HTML',
        reply_markup=markup,
                 )


def Stop_loss_strategy_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    markup = return_markup_state(Close_trade_on_take_profit, config.CLOSE_TRADE_ON_TAKE_PROFIT)
    stop_loss = message.data.split('-')[2]
    global data
    data['stop_loss'] = stop_loss
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #     data['stop_loss'] = stop_loss
    bot.send_message(
        chat_id=message.message.chat.id,
        text= f'<b>Enter  CLOSE TRADE</b>',#\n{text1}', 
        parse_mode='HTML',
        reply_markup=markup,
                 )
    
   
def Close_trade_strategy_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Percentage', callback_data=f'{config.AMOUNT_PER_TRADE_STATE}-percentage',)
    btn2 = types.InlineKeyboardButton(text='Fix USD', callback_data=f'{config.AMOUNT_PER_TRADE_STATE}-fix_usd')
    markup.add(btn1, btn2)
    close_trade = message.data.split('-')[2]
    global data
    data['close_trade'] = close_trade
    
    bot.send_message(
        chat_id=message.message.chat.id,
        text= config.AMOUNT_PER_TRADE_STATE_START,#\n{text1}', 
        parse_mode='HTML',
        reply_markup=markup,
                 )


def Amount_per_trade_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    
    result = message.data.split('-')[1]
    if result == 'percentage':
        markup = return_markup_state(Percentage, config.PERCENTAGE_STATE) 
        bot.send_message(
            chat_id=message.message.chat.id,
            text= f'<b>Enter  FIX USD</b>',#\n{text1}', 
            parse_mode='HTML',
            reply_markup=markup,
                    )
    else:
        markup = return_markup_state(Fixed_usd_amount, config.FIX_USD_STATE)
        bot.send_message(
        chat_id=message.message.chat.id,
        text= f'<b>Enter  PERCENTAGE</b>',#\n{text1}', 
        parse_mode='HTML',
        reply_markup=markup,
                 )


def Amount_per_trade_strategy_percentage_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    print('amount per percentage')
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Yes', callback_data=f'{config.FINAL_STATE}-yes',)
    btn2 = types.InlineKeyboardButton(text='NO', callback_data=f'{config.FINAL_STATE}-no')
    markup.add(btn1, btn2)
    percetage = message.data.split('-')[2]
    global data
    data['fix_usd'] = 'None'
    data['percentage'] = percetage
    name = data['name']
    entry_strategy = data['entry_strategy']
    take_profit = data['take_profit']
    close_trade = data['close_trade']
    stop_loss = data['stop_loss']
    amount_per_trade_percentage = data['percentage']
    amount_per_trade_fix = 'None'
    bot.send_message(
        chat_id=message.message.chat.id,
        text= config.FINAL_STATE_START.format(name, entry_strategy, take_profit, close_trade, stop_loss, amount_per_trade_percentage, amount_per_trade_fix),#\n{text1}', 
        parse_mode='HTML',
        reply_markup=markup,
                 )


def Amount_per_trade_strategy_fix_usd_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    print('amount per fix')
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Yes', callback_data=f'{config.FINAL_STATE}-yes',)
    btn2 = types.InlineKeyboardButton(text='NO', callback_data=f'{config.FINAL_STATE}-no')
    markup.add(btn1, btn2)
    fix_usd = message.data.split('-')[2]
    global data
    data['fix_usd'] = fix_usd
    name = data['name']
    data['percentage'] = 'None'
    entry_strategy = data['entry_strategy']
    take_profit = data['take_profit']
    close_trade = data['close_trade']
    stop_loss = data['stop_loss']
    amount_per_trade_percentage = 'None'
    amount_per_trade_fix = data['fix_usd']
    bot.send_message(
        chat_id=message.message.chat.id,
        text= config.FINAL_STATE_START.format(name, entry_strategy, take_profit, close_trade, stop_loss, amount_per_trade_percentage, amount_per_trade_fix),#\n{text1}', 
        parse_mode='HTML',
        reply_markup=markup,
                 )
    
    
def Strategy_final_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    print('result: ', message.data.split('-')[1])
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton(text=config.OPTIMIZED_CONFIG_BTN, callback_data=config.OPTIMIZED_CONFIG_BTN)
    # bot.set_state(user_id=message.from_user.id, state=strategyState.name_strategy, chat_id=message.chat.id)
    markup.add(btn2)
    global data
    if 'yes' in message.data.split('-')[1]:
        name = data['name']
        entry_strategy = data['entry_strategy']
        take_profit = data['take_profit']
        close_trade = data['close_trade']
        stop_loss = data['stop_loss']
        amount_per_trade_percentage = data['percentage']
        amount_per_trade_fix = data['fix_usd']
            
        print('name:', name,
              'entry strategy: ', entry_strategy,
            'take profit:', take_profit,
            'close trade:', close_trade,
            'amount per trade percentage:', amount_per_trade_percentage, 
            'amount_per_trade_fix:' , amount_per_trade_fix)
        save_strategy(name, 
                      entry_strategy, 
                      take_profit,
                      close_trade, 
                      stop_loss, 
                      amount_per_trade_percentage, 
                      amount_per_trade_fix,
                      1)
        data = {}
        bot.send_message(message.message.chat.id, 
                        '<b> Congrulation Final strategy</b>', 
                        parse_mode='HTML', 
                        reply_markup=markup)
    else:
        
        data = {}
        bot.send_message(message.message.chat.id, 
                        '<b> Return Menu without Save </b>', 
                        parse_mode='HTML',
                        reply_markup=markup
                         )

