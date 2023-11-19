import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)
print(type(texts))
print(texts[0])
print(r.status_code) # узнаем статус полученного ответа


