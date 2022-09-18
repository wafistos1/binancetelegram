from telebot import TeleBot, types
from telebot.handler_backends import State, StatesGroup
from commands.command import amount_per_trade, close_trade_on_take_profit
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
    )

class strategyState(StatesGroup):
    
    name_strategy = State()
    take_profit_strategy = State()
    first_entry_grace_percentage_strategy = State()
    close_trade_on_take_profit_strategy  = State()
    amount_per_trade_strategy  = State()
    final = State()
    

list_take_profit = [
    'Disable', 'One Target', 'Two Targets', 'Three Targets', 'Fifty On First Traget', 'Skip First'
]

list_first_entry_grace = [
    '0.4', '0.8', '1.2', '1.6', '2.0', '2.4', '2.8', '3.2', '3.6', '4.0'
]

list_close_trade_on_take_profit = [
    'On', 'Off'
]


def Create_strategy_state(message: types.CallbackQuery, bot: TeleBot):
    bot.set_state(user_id=message.from_user.id, state=strategyState.name_strategy, chat_id=message.message.chat.id)
    bot.send_message(message.message.chat.id, '<b> 💹 Welcome to the Creation Section of Strategy 💹</b>\n\n<b>Plz Enter Strategy Name\n\n</b>', parse_mode='HTML')
 


def Strategy_name_state(message: types.Message, bot : TeleBot): # Name
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    text = '\n- '.join(list_take_profit)
    bot.set_state(user_id=message.from_user.id, state=strategyState.take_profit_strategy, chat_id=message.chat.id)
    bot.reply_to(message, f'<b>Please choose an item from this list of take profit</b>\n{text}', parse_mode='HTML')



def Strategy_take_profit_state(message: types.Message, bot : TeleBot): #  Take profit
    text = '\n- '.join(list_first_entry_grace)
    if message.text not in list_take_profit:
        text = '\n- '.join(list_take_profit)
        bot.set_state(user_id=message.from_user.id, state=strategyState.take_profit_strategy, chat_id=message.chat.id)
        bot.reply_to(message, f'<b>Sorry but Please choose Valid item from this list of take profit</b>\{text}', parse_mode='HTML')
        return
    
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['take_profit'] = message.text
    bot.set_state(user_id=message.from_user.id, state=strategyState.first_entry_grace_percentage_strategy, chat_id=message.chat.id)
    bot.reply_to(message, f'<b>Enter  first_entry_grace_percentage_strategy value</b>\n{text}', parse_mode='HTML')

   
def Strategy_first_entry_grace_percentage_strategy_state(message: types.Message, bot : TeleBot): #  First entry grace
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['first_entry'] = message.text
    text = '\n- '.join(list_close_trade_on_take_profit)
    bot.set_state(user_id=message.from_user.id, state=strategyState.close_trade_on_take_profit_strategy, chat_id=message.chat.id)
    bot.reply_to(message, f'<b>Enter  close_trade_on_take_profit_strategy value</b>', parse_mode='HTML')
    
def Strategy_close_trade_on_take_profit_strategy_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['close_trade'] = message.text
    text = ''
    bot.set_state(user_id=message.from_user.id, state=strategyState.amount_per_trade_strategy, chat_id=message.chat.id)
    bot.reply_to(message, f'<b>Enter  amount_per_trade_strategy value</b>\n{text}', parse_mode='HTML')


def Strategy_amount_per_trade_strategy_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['amount_per_trade'] = message.text
    
    bot.set_state(user_id=message.from_user.id, state=strategyState.final, chat_id=message.chat.id)
    bot.reply_to(message, '<b> Valide you strategy: </b>', parse_mode='HTML')
    
    
def Strategy_final_state(message: types.Message, bot : TeleBot): #  Amount per Trade
    if 'yes' in message.text.lower():
         
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            
            name = data['name']
            take_profit = data['take_profit']
            first_entry = data['first_entry']
            close_trade = data['close_trade']
            amount_per_trade = data['amount_per_trade']
        print('name:', name, 
            'take profit:', take_profit,
            'first entry:', first_entry, 
            'close trade:', close_trade,
            'amount per trade:', amount_per_trade)
        bot.set_state(user_id=message.from_user.id, state=strategyState.name_strategy, chat_id=message.chat.id)
        bot.reply_to(message, '<b> Congrulation Final strategy</b>', parse_mode='HTML')
    else:
        bot.set_state(user_id=message.from_user.id, state=strategyState.name_strategy, chat_id=message.chat.id)
        bot.reply_to(message, '<b> Return to new strategy  give name </b>', parse_mode='HTML')