# После установки необходимо создать новый файл, импортировать туда модуль telebot и создать объект bot,
# используя токен, полученный при регистрации.

import telebot

TOKEN = '6717574574:AAFhQn2vTT27HWn8cZZ1d1-Ug7Vaps_lKIk'    # 1-й токен  Seraphim700Bot NemoSkillFactory1 (синий)


bot = telebot.TeleBot(TOKEN)

# message — это объект класса telebot.types.Message
#  повторение
@bot.message_handler(content_types=['text'])
def handler_text_mess(message):
    text_message = message.text
    print(text_message)
    bot.send_message(message.chat.id, text_message)


@bot.message_handler(content_types=['photo'])
def handle_photo_message(message):
    # Обрабатываем сообщение с фотографией
    bot.send_photo(message.chat.id, message.photo[-1].file_id)


# Параметр none_stop=True говорит, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок.
bot.polling(none_stop=True)
