# Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD».
# Бот должен отвечать не отдельным сообщением, а с привязкой к картинке.

import telebot

TOKEN = '6717574574:AAFhQn2vTT27HWn8cZZ1d1-Ug7Vaps_lKIk'    # 1-й токен  Seraphim700Bot NemoSkillFactory1 (синий)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['photo', ])
def handle_photo_message(message):
    # Обрабатываем сообщение с фотографией
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)