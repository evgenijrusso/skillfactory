from oop.module_c1.C1_practice.cat import Cat

# Задание 1.10.1
"""
Создайте класс одной из геометрических фигур (например, прямоугольника),
где в конструкторе задаются атрибуты:  начальные координаты x, y, width и height
(или другие в зависимости от выбранной фигуры).
"""

# Задание 1.10.2
"""
В классе, написанном в предыдущем задании, создайте метод, который будет рассчитывать площадь фигуры. 
Выведите значение площади на экран.
"""

class Restangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.heigth}'

    def get_area_rect(self):
        return self.width * self.heigth

    @property
    def proba(self):
        return self.x + 100

r1 = Restangle(x=5, y=10, width=50, height=100)
r2 = Restangle(5,10,50,100)

print('Задание 1.10.1')
print('r1: ', r1)
print('r2: ', r2.proba)

print('\n','Задание 1.10.2')
print('squery: ', r1.get_area_rect())


print('\n','Задание 1.10.3')
"""
В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо создать класс «Клиент», 
который будет содержать данные о клиентах и их финансовых операциях. О клиенте известна следующая 
информация: имя, фамилия, город, баланс.
Далее сделайте вывод о клиентах в консоль в формате:
«Иван Петров. Москва. Баланс: 50 руб.»
"""

class Client(Cat):
    def __init__(self, name, family, city, balance):
        self.name = name
        self.family = family
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.family}. {self.city}. Баланс: {self.balance} руб.'

    def det_client(self):
        return f'{self.name} {self.family}. {self.city}'


client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Владимир','Зайцев','Кострома',50)
client_3 = Client('Олеся','Янина','Новосибирск',50)
print(client_1)

print('\n','Задание 1.10.4')
# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.
guest_list = [client_1, client_2, client_3]
for guest in guest_list:
    print(guest.det_client())