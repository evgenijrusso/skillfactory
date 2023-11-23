import telebot
from telebot import types, formatting

from config import TOKEN, currencies
from extensions import Currency, APIException


bot = telebot.TeleBot(TOKEN)

text_messages = {
    'welcome':
        u'Приветствую всех трудящихся!\n\n'
        u'Работаю над проектом по созданию телеграм-бота, на основе библиотеки pyTelegramBotAPI.\n'
        u'Некоторые вопросы можно решить, использую этот ресурс\n'
        u'https://github.com/eternnoir/pyTelegramBotAPI\n\n'
        u'Удачи всем нам в этой жизни! /help - помощь.\n',

    'info':
        u'Бот производит конвертацию из одной валюты в другую.\n\nСписок доступных для конвертации валют: /values\n'
        u'Для конвертации, воспользуйтесь командой /convert или напишите боту в следующем формате:\n'
        u'- Имя валюты\n- В какую валюту перевести\n- Количество переводимой валюты\n\n'
        u'Доступные команды:\n/start - приветствие\n/help - помощь.\n'
        u'/convert - конвертация\n/values - список доступных валют\n'
    }

def create_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    buttons = []
    for currence in currencies:
        buttons.append(types.KeyboardButton(currence.capitalize()))
    markup.add(*buttons)
    return markup

def commands_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    buttons = ['/convert', '/values', '/help']
    markup.add(*buttons)
    return markup


# -----------------------------
@bot.message_handler(commands=['start',])
def start(message):
    bot.reply_to(message, text_messages['welcome'])

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text_messages['info'], reply_markup=commands_markup())

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:\n'
    for val in currencies:
        text = '\n'.join((text, val))
    bot.reply_to(message, formatting.format_text(
        formatting.hbold(text)), reply_markup=commands_markup(), parse_mode='HTML')


# -------------------  запрос по валюте (base, quote, amount) --------------
@bot.message_handler(commands=['convert'])
def convert(message):
    text = 'Выберете валюту из которой конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup())
    bot.register_next_step_handler(message, base_handler)

def base_handler(message):
    base = message.text
    text = 'Выберете валюту в которую конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup())  #hid=base
    bot.register_next_step_handler(message, query_handler, base)

def query_handler(message, base):
    quote = message.text
    text = 'Напишите количество конвертируемой валюты:'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, base, quote)


def amount_handler(message, base, quote):
    amount = message.text.strip()
    try:
        conv = Currency.get_price(base, quote, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка в конвертации:\n{e}')
    else:
        answer_text = f'Количество единиц валюты: {amount}, валюта: {base.lower()} \n' \
                      f'Цена {currencies[base]} = {conv} {currencies[quote].lower()} ({quote.lower()})'
        bot.send_message(message.chat.id, answer_text, reply_markup=commands_markup())


bot.polling(none_stop=True)
