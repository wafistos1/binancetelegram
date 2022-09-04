# from telebot import TeleBot, types
# from membership_bot.database import databasehelper as DB


# def backHandler(message: types.CallbackQuery, bot: TeleBot):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text=config.button3, callback_data='myplan1')
#     btn2 = types.InlineKeyboardButton(text=config.button4, callback_data='myplan2')
#     markup.add(btn1, btn2)

#     bot_token = bot.token
#     plans = DB.processGetQuery('select * from bots where bot_token = %s', (bot_token,))
#     day1_cost, day1_duration = plans[4], plans[6]
#     day2_cost, day2_duration = plans[5], plans[7]

#     bot.edit_message_text(
#         chat_id=message.from_user.id,
#         text=config.userStartText.format(
#         message.from_user.first_name,
#         day1_cost, day1_duration,
#         day2_cost, day2_duration
#     ), parse_mode='HTML', reply_markup=markup, message_id=message.message.message_id)


