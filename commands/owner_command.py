from telebot import TeleBot, types
from database.create_model import select_table, select_user
from database.create_model import (
    Percentage,
    AmountTrade,
    FixedUsdAmount,
    FristEntryGracePercentage,
    EntryStrategy,
    # NumberTarget,
    CloseTradeOnTakeProfit,
    BlacklistSymbols,
    StopLossTimeout,
    DefaultStopLoss,
    MaxTrades,
    Owner,
    User,
    Binance,
    StrategyOwner,
    StrategyUser,
    TakeProfitStrategy,
    )

import config
import logging



# @bot.message_handler(commands=['start', 'help'])
def return_markup(table, back_btn):
    table_numbers = select_table(table)
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


def _start(message, bot):
    
        user = select_user(Owner)
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text=config.PORTFOLIO_BTN, callback_data=config.PORTFOLIO_BTN)
        btn2 = types.InlineKeyboardButton(text=config.OPTIMIZED_CONFIG_BTN, callback_data=config.OPTIMIZED_CONFIG_BTN)
        btn3 = types.InlineKeyboardButton(text=config.BOT_CONFIG_BTN, callback_data= config.BOT_CONFIG_BTN)
        btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING_FILTERS, callback_data=config.AUTO_TRADING)
        # btn3 = types.InlineKeyboardButton(text='❓ كيفيه التحويل لمحفظه اخرى?', url='https://youtu.be/AcCgcKrABms')
        # btn4 = types.InlineKeyboardButton(text='♦️ Admin', url='tg://user?id={}'.format(admin_id))
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)

        bot.edit_message_text(chat_id=message.from_user.id,
                              message_id=message.message.message_id,
                              text=config.TRADING_MESSAGE_START.format(user), 
                              parse_mode='HTML',
                              reply_markup=markup
                              )


def optimised_config(message: types.Message, bot : TeleBot):
    print('optimised_config')
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.PORTFOLIO_BTN, callback_data='myplan1')
    btn2 = types.InlineKeyboardButton(text=config.OPTIMIZED_CONFIG_BTN, callback_data='myplan2')
    btn3 = types.InlineKeyboardButton(text=config.BOT_CONFIG_BTN, callback_data='myplan2')
    btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING_BTN, callback_data='myplan2')

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    
    bot.edit_message_text(chat_id=message.from_user.id,
                          message_id=message.message.message_id,
                          text=config.OPTIMISED_CONFIG_START,
                          parse_mode='HTML',
                          reply_markup=markup
                          )


def auto_trading(message: types.CallbackQuery, bot : TeleBot):
    print('auto_trading_filters')
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
    table_numbers = select_table(MaxTrades)
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
    
    markup = return_markup(BlacklistSymbols, config.AUTO_TRADING_FILTERS)
    
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
    markup = return_markup(EntryStrategy, config.STRATEGIES)
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
    markup = return_markup(TakeProfitStrategy, config.STRATEGIES)
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
    table_numbers = select_table(FristEntryGracePercentageGracePercentage)
    print('Table: ', table_numbers)
    markup = return_markup(FristEntryGracePercentageGracePercentage, config.STRATEGIES)
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
    
    table_numbers = select_table(FixedUsdAmount)
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