import telebot
from telebot import types, formatting

TOKEN = '6663856800:AAHqIFd8K6fIKiL54HtvDChlp_-P6ebZ9Uk'  # 2-й токен  Seraphim700_Bot NemoSkillFactory2 (красный)

bot = telebot.TeleBot(TOKEN)

#
# @bot.message_handler(commands=['start'])
# def first(message):
#     markup = types.InlineKeyboardMarkup()
#     bot1 = types.InlineKeyboardButton('Currency USD', url='https://t.me/Seraphim700_Bot')
#     bot2 = types.InlineKeyboardButton('help', callback_data='help')
#     bot3 = types.InlineKeyboardButton('query', callback_data='query')
#     markup.row(bot1, bot2)
#     markup.row(bot3)
#     bot.send_message(
#         message.chat.id,
#         f'<i>Приветствуем Вас,<b>{message.chat.username}</b></i>',
#         parse_mode='html', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'help':
#         bot.send_message(callback.message.chat.id, f'<i>Собираемся все вместе <b>Разное</b></i>', parse_mode='html')


bot.polling(none_stop=True)
