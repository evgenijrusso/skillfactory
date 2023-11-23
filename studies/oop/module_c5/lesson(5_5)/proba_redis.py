#   С5.5. Кеширование с помощью Redis
# Кеширование — это временное сохранение данных для дальнейшего доступа к ним.
#  p.s. нельзя одинаково называть файл 'redis' и импорт (redis)
import redis
import json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?

red = redis.Redis(host='localhost', port=6379, password='')
print(red.ping())

red.set('var1', 'value1')  # записываем в кеш строку "value1"
print(red.get('var1'))   # считываем из кеша данные

dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1'))  # с помощью знакомой нам функции превращаем данные, полученные из кеша обратно в словарь
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))