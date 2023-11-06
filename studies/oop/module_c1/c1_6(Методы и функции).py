#    C1.6. Методы и функции

class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


eggs = Product('eggs', 'food', 5)
print('eggs:', eggs.is_available())

# хотим обрабатывать некоторые события из уже известных нам логов событий. Создадим класс с конструктором:
# Допустим, мы уже распарсили наши логи и получили список словарей вроде такого:
class Event1:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.event_type = event_type
        self.session_id = session_id

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]
# Давайте для каждого события в списке создадим соответствующий ему объект с помощью конструктора, как мы уже делали.
# А чтобы убедиться, что объект создаётся, выведем на печать какой-нибудь из атрибутов:

for event in events:
    event_obj = Event1(timestamp=event.get('timestamp'),
                      event_type=event.get('type'),
                      session_id=event.get('session_id'))
    print('event: ',event_obj.timestamp)
    print('event: ', event_obj.event_type)

# Здесь мы использовали метод словаря .get(), который возвращает значение ключа и не вызывает ошибку, если такого ключа в словаре нет.
# Вместо такого явного разбора словаря в цикле мы могли бы задать нашему классу метод, который позволяет инициализировать наш объект напрямую.
print()
class Event2:
    def __init__(self, timestamp=0, event_type='', session_id=""):
        self.timestamp = timestamp
        self.event_type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.event_type = event_dict.get('type')
        self.session_id = event_dict.get('session_id')

for event in events:
    event_obj = Event2()
    event_obj.init_from_dict(event)
    print('ev:', event_obj.timestamp)

# # Более правильный пример
class Humen:
    age = None

    def __init__(self, age=4):
        self.age = age

# Добавляем геттер - спец. метод для получения поля
    def get_age(self):
        return self.age

# добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age,int): ## проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age

h = Humen()
h.set_age(15)
print('age:', h.get_age())