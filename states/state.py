from telebot import TeleBot, types
from telebot.handler_backends import State, StatesGroup
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

class strategyState(StatesGroup):
    stop = State()
    strategie = State()
    auto_trading = State()
    name_strategy = State()





def Create_strategy_state(message: types.Message, bot: TeleBot):
    
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        
        data['name'] = message.text
    bot.set_state(user_id=message.from_user.id, state=strategyState.name_strategy, chat_id=message.chat.id)
    bot.reply_to(message, '<b>Enter name of strategy</b>', parse_mode='HTML')