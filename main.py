

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
    # bot_token = bot.token
    # plans = DB.processGetQuery('select * from bots where bot_token = %s', (bot_token,))
    #day1_cost, day2_cost, day1_duration, day2_duration, admin_id, description  = DB.processGetQuery('SELECT `pack_1_cost`, `pack_2_cost`, `pack_1_duration`, `pack_2_duration`, `adminID`, `description` FROM bots WHERE bot_token = %s', (bot_token,))

    # day1_cost, day1_duration = plans[4], plans[6]
    # day2_cost, day2_duration = plans[5], plans[7]
    # admin_id = plans[10]
    # description = plans[11]
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.PORTFOLIO_BTN, callback_data=config.PORTFOLIO_BTN)
    btn2 = types.InlineKeyboardButton(text=config.OPTIMIZED_CONFIG_BTN, callback_data=config.OPTIMIZED_CONFIG_BTN)
    btn3 = types.InlineKeyboardButton(text=config.BOT_CONFIG_BTN, callback_data= config.BOT_CONFIG_BTN)
    btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING_FILTERS, callback_data=config.AUTO_TRADING_FILTERS)
    # btn3 = types.InlineKeyboardButton(text='❓ كيفيه التحويل لمحفظه اخرى?', url='https://youtu.be/AcCgcKrABms')
    # btn4 = types.InlineKeyboardButton(text='♦️ Admin', url='tg://user?id={}'.format(admin_id))
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    # adminMarkup = types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton(text=config.button7, callback_data=config.button7)
    # btn6 = types.InlineKeyboardButton(text=config.button14, callback_data=config.button14)
    # btn2 = types.InlineKeyboardButton(text=config.button8, callback_data=config.button8)
    # btn3 = types.InlineKeyboardButton(text=config.button9, callback_data=config.button9)
    # btn4 = types.InlineKeyboardButton(text=config.button10, callback_data=config.button10)
    # btn5 = types.InlineKeyboardButton(text='رابط التنبيهات', callback_data=config.button11)
    # btn7 = types.InlineKeyboardButton(text=config.button13, callback_data=config.button13)
    # btn8 = types.InlineKeyboardButton(text=config.button14, callback_data=config.button14)
    # adminMarkup.add(btn6, btn1)
    # adminMarkup.add(btn2, btn3)
    # adminMarkup.add(btn5, btn4)
    # adminMarkup.add(btn7)


    # if int(message.from_user.id) == int(admin_id):
    #     return bot.reply_to(
    #         message,
    #         '<b>🖥 اهلا بك بصفحه الاداره !</b>',
    #         reply_markup=adminMarkup,
    #         parse_mode='HTML'
    #     )
    # bot.edit_messa
    # ge_text()
    
    bot.send_message(text=config.TRADING_MESSAGE_START, chat_id=message.chat.id,  parse_mode='HTML', reply_markup=markup )
    # bot.send_message(text='Welecom to my Channel', chat_id=message.chat.id,  parse_mode='HTML', reply_markup=markup )

bot.register_message_handler(trading_start, commands=['start'])
# bot.register_message_handler(trading_start, commands=['start'])
bot.register_callback_query_handler(_start, pass_bot=True, func=lambda message: message.data == config.MAIN_MENU)
# bot.register_message_handler(callback=trading_start, pass_bot=True, commands=['start'], chat_types=['private'], is_on=True)
bot.register_callback_query_handler(bot_configuration, pass_bot=True,  func=lambda message: message.data == config.BOT_CONFIG_BTN)
bot.register_callback_query_handler(auto_trading_filters, pass_bot=True,  func=lambda message: message.data == config.AUTO_TRADING_FILTERS)
bot.register_callback_query_handler(optimised_config, pass_bot=True,  func=lambda message: message.data == config.OPTIMIZED_CONFIG_BTN)
bot.register_callback_query_handler(portfolio, pass_bot=True,  func=lambda message: message.data == config.PORTFOLIO_BTN)
bot.register_callback_query_handler(max_trade, pass_bot=True,  func=lambda message: message.data == config.MAX_TRADE)
bot.register_callback_query_handler(black_list_symboles, pass_bot=True,  func=lambda message: message.data == config.BLACK_LIST_SYMBOLES)
bot.register_callback_query_handler(stop, pass_bot=True,  func=lambda message: message.data == config.STOP)
bot.register_callback_query_handler(default_stop, pass_bot=True,  func=lambda message: message.data == config.DEFAULT_STOP)
bot.register_callback_query_handler(stop_loss_time, pass_bot=True,  func=lambda message: message.data == config.STOP_LOSS_TIME)
bot.register_callback_query_handler(stategy, pass_bot=True,  func=lambda message: message.data == config.STRATEGIES)
bot.register_callback_query_handler(entry_strategy, pass_bot=True,  func=lambda message: message.data == config.ENTRY_STRATEGY)
bot.register_callback_query_handler(take_profit_strategy, pass_bot=True,  func=lambda message: message.data == config.TAKE_PROFIT_STRATEGY)
bot.register_callback_query_handler(amount_per_trade, pass_bot=True,  func=lambda message: message.data == config.AMOUNT_PER_TRADE)
bot.register_callback_query_handler(close_trade_on_take_profit, pass_bot=True,  func=lambda message: message.data == config.CLOSE_TRADE_ON_TAKE_PROFIT)
bot.register_callback_query_handler(first_entry_grace_percentage, pass_bot=True,  func=lambda message: message.data == config.FIRST_ENTRY_GRACE_PERCENTAGE)
# bot.register_callback_query_handler(plan1Buy, pass_bot=True, func=lambda message: message.data.startswith('myplan1'), is_on=True)


bot.add_custom_filter(custom_filters.StateFilter(bot))
# bot.add_custom_filter(AdminFilter())
bot.infinity_polling()

