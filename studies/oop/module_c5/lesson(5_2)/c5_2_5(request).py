# C5.2. Библиотека Requests и её лучший друг JSON

#API (Application programming interface) — это набор публичных свойств и методов для взаимодействия
# с другими программами, которые могут быть написаны даже на другом языке программирования.
# API можно определить как: «Ко мне можно обращаться так и так, я обязуюсь делать то и это».

import requests

r = requests.get('https://api.telegram.org/botToken/getUpdates')
#r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# делаем запрос на сервер по переданному адресу
print(r.content)
print(r.status_code) # узнаем статус полученного ответа

# В результате работы данного кода в консоль выведется HTML-код сгенерированного текста, т. к. запрос на получение
# странички через браузер на самом деле эквивалентен вызову функции .get() (и то, и то отправляет GET-HTTP-запрос,
# о котором мы будем говорить более подробно чуть позже на нашем курсе).

# Есть несколько категорий ответов, например:
#
# 200, 201, 202 и т. д. — ответы, которые говорят, что с запросом всё хорошо и ответ приходит правильный, т. е. его можно обрабатывать и как-либо взаимодействовать с ним. На самом деле почти все серверы всегда в ответ шлют именно ответ 200, а не какой-либо другой из этой же категории.
# 300, 301 и т. д. — ответы, которые говорят, что вы будете перенаправлены на другой ресурс (необязательно на этом же сервере).
# 400, 401 и т. д. — ответы, которые говорят, что что-то неправильно с запросом. Запрашивается либо несуществующая страница (всем известная 404 ошибка), либо же недостаточно прав для просмотра страницы (403) и т. д.
# 501, 502 и т. д. — ответы, которые говорят, что с запросом всё хорошо, но вот на сервере что-то сломалось, и поэтому нормальный ответ прийти не может.

