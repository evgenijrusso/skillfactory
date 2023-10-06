# Вопрос 5
# Уровень 1
#
# Вопрос: Определите класс, который имеет как минимум два метода:
# getString: для получения строки из консольного ввода
# print String: для печати строки в верхнем регистре.
# Также, пожалуйста, включите простую тестовую функцию для проверки методов класса.
#
# Подсказки: Используйте метод init для построения некоторых параметров

class InputOutString(object):

    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input('get string:')

    def print_string(self):
        print(self.s.upper())


stObj = InputOutString()
stObj.getString()
stObj.print_string()