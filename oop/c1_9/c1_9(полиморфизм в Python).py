# C1.9. Полиморфизм в Python

# Полиморфизм в ООП обрабатывает разные типы данных, принадлежащих к разным классам, с помощью одной и той же функции
# (метода). По сути одинаковым является только имя метода, но результаты работы одноимённых методов могут различаться.

# Рассмотрим пример
# Нам необходимо рассчитать площадь геометрической фигуры на основе полиморфизма:

# Еще немного о полиморфизме и магических методах на примере __eq__ и __str__
# Давайте рассмотрим ещё один полезный пример полиморфизма в классах Python — перегрузку операторов и методов.
#
# Перегрузка представляет собой изменение поведения стандартного оператора или метода под особенности класса.

# Возьмём несколько наиболее часто используемых методов:
#
# __eq__ — определяет поведение оператора равенства ==;
# __str__ — определяет поведение функции str() или вызов внутри функции print().
# А теперь рассмотрим примеры.

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Нам необходимо уметь сравнивать точки между собой и выводить их для пользователя.
# Соответственно переопределим методы __eq__ и __str__ внутри класса Dot.

    def __eq__(self, other):
        return  self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x} {self.y}'

p1 = Dot(1,2)
p2 = Dot(1,2)
print(p1==p2)
print(str(p1))
print(p2)

# Задание 1.9.1
# Выполните задание, взяв за основу код из примера выше.
# Добавьте ещё один класс — круг (class Circle), конструктор которого содержит параметр радиус.
# Добавьте метод для расчёта площади круга (вспомните формулу).
# Далее сделайте вывод информации о площади в консоль.

