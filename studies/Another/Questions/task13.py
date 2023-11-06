# Вебинар «Функции Python»
# Запаковка
person = ('Сидоров Иван Иванович', 30, 'Омск')
print(person)

# Разпаковка
fio, age, region = person

# Автоматическая распаковка
a, b = 1, 2
1, 2

numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers
#  Оператор * означает, что остаток списка запакуется в одну переменную
print('first', first)
print('second', second)
print('rest', rest)


def average(a, b, c):
    return (a + b +c) / 3

print('aver', average(2, 3, 4))


def average(*args):
    if len(args) == 0:
        return sum(args)


# def process_data(data):
#     return
# data = [1, 2,3 ,4 ,5]
# process_data(*data)

# Именованные аргументы (запаковка именованных аргументов)

def create_dict(**kwargs):
    dict1 = kwargs
    return dict1


print('Словарь:', create_dict(name='Сидоров Иван Иванович', age =30, region='Омск'))

def calc_total(**kwargs):
    '''Рассчитай  сумму чека'''
    total = 0
    for item, price in kwargs.items():
        total += price
    return total

order_total = calc_total(apple=12, banana=10, orange=15)
print('Общая стоимость заказа: ', order_total)

# Написать функцию create_user. которая будет создавать нового пользователя. Функция принимает различные параметры,
# такие как фамилия, имя, отчество, вораст, почта, номер телефона. Функция возвращает словарь.
#Пример:
#user1 = create_user(surname='Rue', name='John', age=25)

# Объединение словарей
d1 = {'a': 1, 'b': 2}
d2 = {'a': 1, 'b': 3}

# Реализовать функцию - счетчик

def counter():
    cnt = 0
    def step():
        nonlocal cnt
        cnt += 1
        return cnt
    return step


# def outer():
#     funcs = []
#     for i in range(4):
#         def func(i):   # a=i
#             print('i:', i)  #a
#         funcs.append(func)
#     return funcs
#
# outer()[i]()
# outer()[2]()


my_counter = counter()

print(my_counter())
print(my_counter())
print(my_counter())

from functools import wraps
# Декоратор
def decorator_func(original_func):
    def wrapper_func():
#        @wraps(original_func)   # запоминаем код оригинальной функции
        #  print('Доп. код, выполняемый перед вызовом функции')
        original_func()
        print('Доп. код, выполняемый после вызова функции')
    return wrapper_func

# -------------------  пример -------------
def my_func():
    print('My function')

decorator_func = decorator_func(my_func)
decorator_func()
# 'Доп. код, выполняемый перед вызовом функции'
# Доп. код, выполняемый после вызова функции

# @decorator_func
# def my_func():
#     '''Это простая функции'''
#     print('My function -------')
#
# my_func()
# 'Доп. код, выполняемый перед вызовом функции'
# Доп. код, выполняемый после вызова функции

import time

def time_of_func(func):
    def wrapped(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print('Used time:', end - start)
        return res
    return wrapped

@time_of_func
def my_func(a, b):
    return a + b

print(my_func(10, 20))