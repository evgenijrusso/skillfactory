#  B4.4. Итераторы и генераторы, оператор yield

# Функции-генераторы
print('\n', 'Задание 4.4.1')
def fib():
    a, b = 0, 1
    yield a     # F0
    yield b     # F1

    while True:
        a, b = b, a + b
        yield b

for num in fib():
    if num < 100:
        print('fib: ', num)
    else:
        break

print('\n', 'Задание 4.4.2')

def repeat_list(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value

# for i in repeat_list([1,2,3]):  # не ростановилась
#     print(i)

str='my_tet'
str_iter = iter(str)
print(type(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))

tmp = 'core_Person'
person = 'person'
q = tmp.lower().split('_')[1]
w = tmp.lower()[5:]
print(q)
print(w)
print(person in tmp.lower())

print('Передача аргументов в декорируемую функцию')

def do_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@do_decorator
def say_word(word):
    print(word)

say_word('Oy..!')

print('\n', 'Задание 4.5.2 Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. ')

def count_call(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        print(f"Запустилась функция {fn}")
        fn(*args, **kwargs)
        count += 1
        print(f"Функция {fn} будет вызвана после каждого вызова функции, {count} раз")
    return wrapper


@count_call
def ires(n):
    print(n)

ires(5)
ires(2)

print('\n', 'Задание 4.5.3 Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.. ')
# Словарь должен находиться в nonlocal области в следующем формате:
# по ключу располагается аргумент функции, по значению — результат работы функции, например, {n: f(n)}.

def cache(fn):
    cache_dict = {}

    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict = fn(num)
            print(f"Добавление результата в кэш: {cache_dict[num]}")
        else:
            print(f"Возвращение результата из кэша: {cache_dict[num]}")
        print(f' Кэш {cache_dict}')
        return cache_dict[num]
    return wrapper

@cache
def f(n):
   return n * 123456789

print(f(10))