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

# =========================  последовательно рабатают ==================
from telebot.handler_backends import ContinueHandling

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello!')
    return ContinueHandling()


@bot.message_handler(commands=['start'])
def start2(message):
    bot.send_message(message.chat.id, 'Hello 2!')


# ======================  шрифт ==========================
from telebot import types, formatting

@bot.message_handler(commands=['start'])
def start_message(message):
    text1 = 'sdsds dddd'
    bot.send_message(
        message.chat.id,
        # function which connects all strings
        formatting.format_text(
            formatting.hcode(text1),      # простой текст  
            formatting.hstrikethrough(text1), # ----
            formatting.hbold(text1),        # bold
            formatting.hitalic(text1)   # с наклоном
        ),
        parse_mode='HTML'
    )

# -------------------------   не использовал -------------------------

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
     try:
         base, quote, amount = message.text.split()
     except ValueError:
         bot.reply_to(message, 'Неверное количество параметров!\nПравильный формат команды для бота можно посмотреть в \
         /help. Или воспользуйся командой /convert.')
     else:
         base = base.capitalize()
         quote = quote.capitalize()
         try:
             conv = Currency.get_price(base, quote, amount)
             answer_text = f'Стоимость {amount} едениц валюты {base} в валюте {quote}: {conv}\n{amount} \
             {currencies[base]} = {conv} {currencies[quote]}'
             bot.reply_to(message, answer_text)
         except APIException as e:
             bot.reply_to(message, f'Ошибка в команде:\n{e}')
         except Exception as e:
             bot.reply_to(message, f'Системная ошибка.\n{e}')


 @bot.message_handler(commands=['start', 'help'])
 def proba(message):
     try:
         b = obj.get_price(base=base, quote=quote, amount=amount)
         bot.send_message(message.chat.id, b)
     except Exception as e:
         bot.send_message(message.chat.id, 'Произошла ошибка: {}'.format(e))
