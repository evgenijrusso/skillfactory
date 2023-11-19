import requests
import json

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json-ответ
# texts = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы
# print(r.status_code)
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:
#     print(text[:50], '\n')

r = requests.get('https://api.github.com') # В консоли мы увидим структуру, похожую на словарь:
d = json.loads(r.content)
print(type(d))
print(d['following_url'])