from telebot import TeleBot, types

import config
import logging



# @bot.message_handler(commands=['start', 'help'])



def _start(message, bot):
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
        bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id,text=config.TRADING_MESSAGE_START, parse_mode='HTML', reply_markup=markup)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     # bot.reply_to(message, "Howdy, how are you doing?")
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     # markup.add(button5)
#     bot.set_state(user_id=message.from_user.id, state=adminState.toto, chat_id=message.chat.id)
#     b

def bot_configuration(message: types.CallbackQuery, bot : TeleBot): #Todo Done
    print('Bot config.')
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.GENERAL, callback_data=config.GENERAL)
    # btn2 = types.InlineKeyboardButton(text=config.STRATEGIES, callback_data=config.STRATEGIES)
    btn3 = types.InlineKeyboardButton(text=config.STOP, callback_data=config.STOP)
    btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING_FILTERS, callback_data=config.AUTO_TRADING_FILTERS)
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.BACK)
    btn6 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU)
    markup.add(btn1)
    markup.add(btn3, btn4)
    markup.add(btn6)
    # bot.delete_message(chat_id=message.message.chat.id,message_id=message.message.message_id)
    bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=config.BOT_CONFIG_START, parse_mode='HTML', reply_markup=markup)


def optimised_config(message: types.Message, bot : TeleBot):
    print('optimised_config')
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.PORTFOLIO_BTN, callback_data='myplan1')
    btn2 = types.InlineKeyboardButton(text=config.OPTIMIZED_CONFIG_BTN, callback_data='myplan2')
    btn3 = types.InlineKeyboardButton(text=config.BOT_CONFIG_BTN, callback_data='myplan2')
    btn4 = types.InlineKeyboardButton(text=config.AUTO_TRADING_BTN, callback_data='myplan2')

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    
    bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=config.OPTIMISED_CONFIG_START, parse_mode='HTML', reply_markup=markup)


def auto_trading_filters(message: types.CallbackQuery, bot : TeleBot):
    print('auto_trading')
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text=config.MAX_TRADE, callback_data=config.MAX_TRADE,)
    btn2 = types.InlineKeyboardButton(text=config.BLACK_LIST_SYMBOLES, callback_data=config.BLACK_LIST_SYMBOLES,)
    btn3 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.BOT_CONFIG_BTN,)
    btn4 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn2)
    markup.add(btn4, btn3 )
    bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=config.AUTO_TRADING_START, parse_mode='HTML', reply_markup=markup)


def portfolio(message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('portfolio')
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1)
    bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=config.PORTFOLIO_START, parse_mode='HTML', reply_markup=markup)


def max_trade (message: types.CallbackQuery, bot : TeleBot):  #todo DONE
    print('portfolio')
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text=config.BACK, callback_data=config.AUTO_TRADING_FILTERS)
    btn1 = types.InlineKeyboardButton(text=config.MAIN_MENU, callback_data=config.MAIN_MENU,)
    markup.add(btn1, btn5)
    bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=config.PORTFOLIO_START, parse_mode='HTML', reply_markup=markup)

