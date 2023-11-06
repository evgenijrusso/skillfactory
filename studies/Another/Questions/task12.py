# функции как тип

def sum(a,b):
    return  a+b

def mult(a,b):
    return a*b

operation = sum
print(operation(5, 6))
operation = mult
print(operation(5, 6))

# рекурсии
def rec(x):
    if x<20:
        print(x)
        rec(x+1)
        print(x)
rec(1)

# факториал числа

def fact(x):
    if x == 1:
        return 1
    return fact(x-1)*x

print(fact(3))

# ----------  рекурсия и определение четных чисел
# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#
# n = int(input('введите число: '))
#
# if (check(n) == True):
#     print('четное')
# else:
#     print('нечетное')

#  итераторы и генераторы (генератор списка)
a= [i ** 2 for i in range(1, 6)]
b = ['2', '5', '8']
print(a)

b_map = list(map(int, b))
cg = [int(i) for i in b]
print('`b_map:', b_map)
print('cg:', cg)

# выражение генераторов (генеротор - это итератор, кторый можно генерировать только один раз)

d = (i ** 2 for i in range(1, 6))
print('d', next(d))
print('d', next(d))
print('d', next(d))

# yield == return


def cube_numbers(nums):
    cube_list = []
    for i in nums:
        cube_list.append(i**3)
    return cube_list


print('cube:', cube_numbers([1,2,3,4]))


def cube_numbers(nums):

    for i in nums:
        yield i**3

cubt = cube_numbers([1,2,3,4])
print('cube_gen:', cubt)
print(next(cubt))
print(next(cubt))
print(next(cubt))
print(next(cubt))

# декоратор

# 1
def my_decor(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper


def my_func():
    print('my_func1:', 'Основная функция')

my = my_decor(my_func)
my()

#2

def my_decor(func):
    def wrapper(n):
        print('start')
        func(n)
        print('end')
    return wrapper


@my_decor
def my_func(number):
    print('my_func2:', number ** 2)

my_func(10)
