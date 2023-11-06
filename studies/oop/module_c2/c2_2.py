print('Задание 2.2.4')
# Напишите класс SquareFactory с одним статическим методом, принимающим единственный аргумент — сторону квадрата.
# Данный метод должен возвращать объект класса Square с переданной стороной.


class Square:

    _side = None
    def __init__(self, side):
        self.side = side

    @property
    def get_area_square(self):
        return self.side ** 2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
        else:
            raise ValueError("Нельзя вводить отриц. число")


class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)


sf1 = SquareFactory.create_square(2)
print(sf1.side)

# Задание 2.3.4
# Создать вычисляемое свойство для класса Square. Сделайте метод по вычислению площади свойством.
# Сделайте сторону квадрата свойством, которое можно установить только через сеттер. В сеттере
# добавьте проверку условия, что сторона должна быть неотрицательной.
print('\n', 'Задание 2.3.4')

sq1 = Square(side=4)
sq2 = Square(side=5)
print("Площадь квадрата", sq1.get_area_square)
sq2.side = 10
print("Сторона квардата: ", sq2.side)

print('\n','Задание 2.4.8')
# Создать скрипт, который будет в input() принимать строки, и их необходимо будет конвертировать в числа, добавить
# try-except на то, чтобы строки могли быть сконвертированы в числа.
# В случае удачного выполнения скрипта написать: «Вы ввели правильное число».
# В конце скрипта обязательно написать: «Выход из программы».
# Примечание: для отлова ошибок используйте try-except, а также блоки finally и else.

try:
    num = int(input('Введите число: '))
except ValueError as e:
    print('Ввел неправильное число')
else:
    print(f'Ввел число: {num}')
finally:
    print('Выход из программы')
