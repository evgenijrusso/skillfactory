#  Разные функции

```
@bot.message_handler(content_types=['text'])   # работает на ответ
def send_mess_name(message):
    bot.reply_to(message, f'Привет2 от ...')
```

```
@bot.message_handler(content_types=['text'])
def echo(message):
    # bot.send_message(message.from_user.id, 'Привет всем')
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
```

```python
#  повторение текста
@bot.message_handler(content_types=['text'])
def handler_text_mess(message):
    text_message = message.text
    print(text_message)
    bot.send_message(message.chat.id, message.text)
```

###  повторение
```
@bot.message_handler(content_types=['text'])
def handler_text_mess(message):
    bot.send_message(message.chat.id, message.text)
```

###  один и тот же ответ на приветстивие или ввод иного текста
```
@bot.message_handler(content_types=['text'])  # ['start', 'help']
def send_mess_name(message):
    bot.send_message(message.chat.id, f'Привет от {message.chat.username}')
```

###  получаем ответ на приветствие и все (других ответов нет, только ответ на start и help)
```
@bot.message_handler(commands=['start', 'help'])
def send_mess_name(message):
    bot.reply_to(message, f'Приветствую Вас от имени {message.chat.username}')  # убрать .chat.id
```
``` # выбираю картинку и в ответ сообщение, связанное с картинкой
@bot.message_handler(content_types=['photo', ])
def handle_photo_message(message):
    # Обрабатываем сообщение с фотографией
    bot.reply_to(message, 'Nice meme XDD')
```