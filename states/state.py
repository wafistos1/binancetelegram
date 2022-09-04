# from telebot.handler_backends import State, StatesGroup
# from database import databasehelper as DB
# import time
# import re
# import logging
# logging.basicConfig(filename='./wafistos7.log', level=logging.INFO)

# class paidStateInitializing(StatesGroup):
#     stop = State()
#     strategie = State()
#     auto_trading = State()





# def paidStateHandler(message: types.Message, bot: TeleBot):
    
#     if len(message.text) < 10: return bot.reply_to(message, '⚠️ رقم الحواله غير صحيح, اعد المحاوله!')

#     bot_token = bot.token
#     botInfo = DB.processGetQuery('select * from bots where bot_token = %s', (bot_token,))
#     api_key, api_secret = botInfo[2], botInfo[3]
#     plancost = botInfo[4]

# # Wafi's edit
#     regex = re.compile(r'Internal transfer (?P<froms>\d*\.?\d*)')
#     p = re.match(regex, message.text)

#     # 3 suposition pour l'enregistrement
#     if p != None:  # example:Internal transfer 123123231312
#         logging.info('example:Internal transfer 123123231312')

#         result = binanceHelper.getTX_Info(api_key, api_secret, message.text)
#         logging.info('afterisexis')
#         isExists = DB.processGetQuery('select * from purchases where tx_id = %s', (str(p['froms']),))
#         if not isExists:
#             logging.info('afternotisexist')
#             isExists = DB.processGetQuery('select * from purchases where tx_id = %s', (message.text,))

#     elif len(str(message.text)) <= 15:  # example: 123123231312
#         logging.info('# example: 123123231312')
#         txt = 'Internal transfer ' + message.text
#         result = binanceHelper.getTX_Info(api_key, api_secret, txt)
#         isExists = DB.processGetQuery('select * from purchases where tx_id = %s', (message.text,))
#         if not isExists:
#             isExists = DB.processGetQuery('select * from purchases where tx_id = %s', (txt,))


#     else:  # example: 123123231312dfsadfasdfasdfdcxcccsfsasdfasd
#         # only number
#         logging.info('## example: 123123231312dfsadfasdfasdfdcxcccsfsasdfasd')
#         result = binanceHelper.getTX_Info(api_key, api_secret, message.text)
#         isExists = DB.processGetQuery('select * from purchases where tx_id = %s', (message.text,))

#     # end Edits

#     # result = binanceHelper.getTX_Info(api_key, api_secret, message.text)
#     # isExists = DB.processGetQuery('select * from purchases where tx_id = %s', (message.text,))
#     if isExists: return bot.reply_to(message, '⚠️ رقم التحويل مستخدم من قبل!')
#     if not result: return bot.reply_to(message, '⚠️ اما ان الحواله لم تصل بعد او ان رقم التحويل خطأ!')
#     #logging.info('example:Internal transfer 123123231312')
#     bot.send_message(message.chat.id, '✅ تأكيد وصول حواله بمبلغ <b>{} دولار رقمي</b>'.format(result), parse_mode='HTML')

#     if float(result) < plancost:
#         lessAmount = float(plancost) - float(result)
#         if lessAmount > 1:
#             return bot.reply_to(message, 'المبلغ المتبقي {} دولار رقمي, يرجى التواصل مع <a href="tg://user?id={}">Admin!</a>'.format(lessAmount, botInfo[10]), parse_mode='HTML')

#     # DB.processUpdateQuery('insert into purchases (tx_id, amount) values (%s, %s)', (message.text, result))
#     # Wafi edit's
#     # Save as DATABASE
#     regex = re.compile(r'Internal transfer (?P<froms>\d*\.?\d*)')
#     p = re.match(regex, message.text)

#     # 
#     if p != None:  # EX: Internal transfer 2342423423423
#         DB.processUpdateQuery('insert into purchases (tx_id, amount, username, bot_token) values (%s, %s, %s, %s)',
#                               (message.text, result, message.from_user.id, bot_token))

#     # elif len(message.text) <= 15: # 2342423423423
#     #     pass

#     else:  # EX: FSDFSF334343434EDFSSDFSDFSDF
#         DB.processUpdateQuery('insert into purchases (tx_id, amount, username, bot_token) values (%s, %s, %s, %s)',
#                               (message.text, result, message.from_user.id, bot_token))
#     # Endedit's

#     try:
#         bot.unban_chat_member(chat_id=botInfo[8], user_id=message.from_user.id)
#         invite_link_group = None
#         if botInfo[13] != 'none':
#             bot.unban_chat_member(chat_id=botInfo[13], user_id=message.from_user.id)
#             invite_link_group = bot.create_chat_invite_link(chat_id=botInfo[13], member_limit=1)

#         invite_link = bot.create_chat_invite_link(chat_id=botInfo[8], member_limit=1)
#         expire_time = time.time() + (botInfo[6] * (60 * 5))
#         DB.processUpdateQuery('update `bots` set `totalIncome` = totalIncome + %s where `bot_token` = %s', (float(result), bot.token))

#         is_renew = DB.processGetQuery('select * from memberships where user_id = %s and bot_token = %s', (message.from_user.id, bot.token))
#         print(is_renew)
#         if not is_renew:
#             DB.processUpdateQuery('insert into memberships (user_id, expire_time, bot_token, username) values (%s, %s, %s, %s)', (message.from_user.id, expire_time, bot.token,message.from_user.username if message.from_user.username else message.from_user.first_name))
#             # bot.send_message(message.chat.id, str(message.from_user))
#             expire_time_for_user = datetime.datetime.now() + datetime.timedelta(days=int(botInfo[6] * 30))
#             expire_time_for_user = expire_time_for_user.strftime("%d %B, %Y")
#         else:
#             additional_time = botInfo[6] * (24 * 60 * 60 * 30)
#             DB.processUpdateQuery('update memberships set expire_time=expire_time+%s where user_id = %s and bot_token = %s', (additional_time, message.from_user.id, bot.token))

#             current_timestamp = DB.processGetQuery('select * from memberships where user_id = %s and bot_token = %s', (message.from_user.id, bot.token))
#             expire_time_for_user = datetime.datetime.fromtimestamp(int(float(current_timestamp[2]))) + datetime.timedelta(days=int(botInfo[6] * 30))
#             expire_time_for_user = expire_time_for_user.strftime("%d %B, %Y")

#         markup1 = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton(text='Click to Join',  url=f'{invite_link.invite_link}')
#         markup1.add(btn1)
#         bot.delete_state(chat_id=message.chat.id, user_id=message.from_user.id)
#         bot.send_message(message.chat.id, 'باقتك الحاليه تنتهي بتاريخ: {}'.format(expire_time_for_user), reply_markup=markup1)
#         message_terme = botInfo = DB.processGetQuery('SELECT `after_pay_text` FROM bots WHERE bot_token = %s', (bot_token,))
#         logging.info(f'Message terme {message_terme}')
#         # message_terme = 'tesesting'
#         bot.send_message(message.chat.id, str(message_terme[0]), parse_mode='HTML')
        
#         if not invite_link_group: bot.send_message(message.chat.id, invite_link_group.invite_link, reply_markup=types.ReplyKeyboardRemove())
#         bot.send_message(message.chat.id, 'لاي استفسارات <a href="tg://user?id={}">Admin!</a>'.format(botInfo[10]), parse_mode='HTML')
#         bot.send_message(message.chat.id, 'لاي استفسار تواصل مع <a href="tg://user?id={}">Admin!</a>'.format(botInfo[10]), parse_mode='HTML')
        
#     except Exception as error:
#         # bot.send_message(message.chat.id, str(error))
#         print(error)
