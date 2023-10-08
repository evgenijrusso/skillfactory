# Задание 4.2.1 # Задание на самопроверку.

# Задание 4.2.3
def delitel(a, n):
    if a % n == 0:
        print(f"Число {n} является делителем числа {a}")
    else:
        print(f"Число {n} не является делителем числа {a}")

delitel(4, 2)
delitel(5, 2)
print()

print('Задание 4.2.4 Задание на самопроверку.')
# Напишите функцию, которая печатает «обратную лесенку» следующего типа:

def reverse_stair(n):
    for i in range(n, 0, -1):
        result = i * '*'
        print(result)

reverse_stair(3)
print()
reverse_stair(4)
print()
print('Задание 4.2.5 Задание на самопроверку. Напишите функцию, которая будет возвращать количество делителей числа а.')

def get_multipliers(a):
    count = 0
    for n in range(1, a+1):
        if a % n == 0:
            count += 1
    return count

print(get_multipliers(8))

print()
print('Задание 4.2.6 Напишите функцию, которая проверяет, является ли '
      'данная строка палиндромом или нет, и возвращает результат проверки.')

def check_palindrome(st):
    st = st.lower()
    st = st.replace(" ", "")
    if st == st[::-1]:
        return True
    else:
        return False

s = 'Кит на море не романтик'
print(check_palindrome(s))

print('\n', 'Задание 4.3.2', 'Написать функцию, которая будет перемножать любое количество переданных ей аргументов.')

def muller(*nums):
    mul = 1
    for n in nums:
        mul *= n
    return mul

print(muller(0))
print(muller(1))
print(muller(1,2))
print(muller(1,2,3))
print(muller(1,2,3,4))

print('\n', 'Фибоначи, рекурсия')

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print('fibo: ', fibo(10))


print('\n', 'Задание 4.3.3 С помощью рекурсивной функции найдите сумму чисел от 1 до n.')
def summa(n):
    if n == 1:
        return 1  # терминальный случай
    return n + summa(n-1)

print('summa: ', summa(5))

print('\n', 'Задание 4.3.4  С помощью рекурсивной функции разверните строку')

def rec_string(st):
    if len(st) == 0:
        return ''
    return st[-1] + rec_string(st[:-1])

s = 'Майка'
print(rec_string(s))

print('\n', 'Задание 4.3.5  Дано натуральное число N. Вычислите сумму его цифр.')
print('natur: ', 35437)
def natur(n):
    if n < 10:
        return n
    else:
        return n % 10 + natur(n // 10)

print('natur: ', natur(35437))