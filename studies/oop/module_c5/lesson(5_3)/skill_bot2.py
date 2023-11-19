import telebot

TOKEN = '6663856800:AAHqIFd8K6fIKiL54HtvDChlp_-P6ebZ9Uk'  # 2-й токен  Seraphim700_Bot NemoSkillFactory2 (красный)

bot = telebot.TeleBot(TOKEN)


###  получаем ответ на приветствие и все (других ответов нет)
@bot.message_handler(commands=['start', 'help'])
def send_mess_name(message):
    bot.reply_to(message, f'Приветствую Вас от имени {message.chat.username}')  # убрать .chat.id


bot.polling(none_stop=True)