

import time
import os
import requests
import re
from config import BOT_TOKEN
from telebot import TeleBot, custom_filters, types
from telebot.custom_filters import SimpleCustomFilter
from commands.command import (
    bot_configuration,
    auto_trading_filters,
    optimised_config,
    portfolio,
    _start,
    max_trade,
    black_list_symboles,
    stop,
    default_stop,
    stop_loss_time,
    stategy,
    entry_strategy,
    take_profit_strategy,
    amount_per_trade,
    close_trade_on_take_profit,
    first_entry_grace_percentage,
    percentage,
    fixed_usd_amount,
    auto_trading,
    )
from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State, StatesGroup
import logging
import config




state_storage = StateMemoryStorage()
bot = TeleBot(token=BOT_TOKEN, num_threads=10)

class adminState(StatesGroup):
    bot_token = State()
    pack_2_duration = State()
    toto = State()
    
def trading_start(message):

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.PORTFOLIO_BTN, callback_data=config.PORTFOLIO_BTN)
    btn2 = types.InlineKeyboardButton(text=config.OPTIMIZED_CONFIG_BTN, callback_data=config.OPTIMIZED_CONFIG_BTN)
    btn3 = types.InlineKeyboardButton(text=config.BOT_CONFIG_BTN, callback_data=config.BOT_CONFIG_BTN)
    btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING, callback_data=config.AUTO_TRADING)

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)


    
    bot.send_message(text=config.TRADING_MESSAGE_START, chat_id=message.chat.id,  parse_mode='HTML', reply_markup=markup )
    # bot.send_message(text='Welecom to my Channel', chat_id=message.chat.id,  parse_mode='HTML', reply_markup=markup )

bot.register_message_handler(trading_start, commands=['start'])
# bot.register_message_handler(trading_start, commands=['start'])
bot.register_callback_query_handler(_start, pass_bot=True, func=lambda message: message.data.startswith(config.MAIN_MENU))
# bot.register_message_handler(callback=trading_start, pass_bot=True, commands=['start'], chat_types=['private'], is_on=True)
bot.register_callback_query_handler(bot_configuration, pass_bot=True,  func=lambda message: message.data == config.BOT_CONFIG_BTN)
bot.register_callback_query_handler(auto_trading_filters, pass_bot=True,  func=lambda message: message.data == config.AUTO_TRADING_FILTERS)
bot.register_callback_query_handler(optimised_config, pass_bot=True,  func=lambda message: message.data == config.OPTIMIZED_CONFIG_BTN)
bot.register_callback_query_handler(portfolio, pass_bot=True,  func=lambda message: message.data == config.PORTFOLIO_BTN)
bot.register_callback_query_handler(max_trade, pass_bot=True,  func=lambda message: message.data.startswith(config.MAX_TRADE))
bot.register_callback_query_handler(black_list_symboles, pass_bot=True,  func=lambda message: message.data.startswith(config.BLACK_LIST_SYMBOLES))
bot.register_callback_query_handler(stop, pass_bot=True,  func=lambda message: message.data == config.STOP)
bot.register_callback_query_handler(default_stop, pass_bot=True,  func=lambda message: message.data == config.DEFAULT_STOP)
bot.register_callback_query_handler(stop_loss_time, pass_bot=True,  func=lambda message: message.data == config.STOP_LOSS_TIME)
bot.register_callback_query_handler(stategy, pass_bot=True,  func=lambda message: message.data.startswith(config.STRATEGIES))
bot.register_callback_query_handler(entry_strategy, pass_bot=True,  func=lambda message: message.data.startswith(config.ENTRY_STRATEGY))
bot.register_callback_query_handler(take_profit_strategy, pass_bot=True,  func=lambda message: message.data.startswith(config.TAKE_PROFIT_STRATEGY))
bot.register_callback_query_handler(amount_per_trade, pass_bot=True,  func=lambda message: message.data.startswith(config.AMOUNT_PER_TRADE))
bot.register_callback_query_handler(close_trade_on_take_profit, pass_bot=True,  func=lambda message: message.data == config.CLOSE_TRADE_ON_TAKE_PROFIT)
bot.register_callback_query_handler(first_entry_grace_percentage, pass_bot=True,  func=lambda message: message.data.startswith(config.FIRST_ENTRY_GRACE_PERCENTAGE))
bot.register_callback_query_handler(percentage, pass_bot=True,  func=lambda message: message.data.startswith(config.PERCENTAGE))
bot.register_callback_query_handler(fixed_usd_amount, pass_bot=True,  func=lambda message: message.data.startswith(config.FIXED_USD_AMOUNT))
bot.register_callback_query_handler(auto_trading, pass_bot=True,  func=lambda message: message.data.startswith(config.AUTO_TRADING))
# bot.register_callback_query_handler(plan1Buy, pass_bot=True, func=lambda message: message.data.startswith('myplan1'), is_on=True)


bot.add_custom_filter(custom_filters.StateFilter(bot))
# bot.add_custom_filter(AdminFilter())
bot.infinity_polling()

