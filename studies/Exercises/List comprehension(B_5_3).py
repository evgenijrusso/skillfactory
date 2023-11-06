# List comprehension

# Генераторы списков — это специальный синтаксис, определяющий правила создания и заполнения списков.
# В общем виде эта конструкция записывается следующим образом:

some_iter_obj = [...]
cond = ''
L = [a for a in some_iter_obj if cond ]

# Такая запись аналогична следующей:

L = []

for a in some_iter_obj:
    if cond:
        L.append(a)

# Напишем генератор списков, в котором будут храниться квадраты первых 10 натуральных чисел.
squares1 = [i**2 for i in range(1, 11)]
print('squares1: ', squares1)

# Можно модифицировать этот генератор списков таким образом, что в список будут включаться квадраты только от нечётных чисел.

squares2 = [i**2 for i in range(1, 11) if i % 2 == 1]
print('squares2: ', squares2)

# Можно  составить список из кортежей:
squares3 = [(i, i**2) for i in range(1, 11) if i % 2 == 1]
print('squares3: ', squares3)

print('Задание 5.3.13. При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.')
tabl_mul = [[i*j for j in range(1,11)] for i in range(1,11)]
print('tabl_mul', tabl_mul)

# Заполнение список через консоль, можно заранее и с целыми числаим L = [int(input()) for i in range(5)]
# L1 = [int(input('Введите число: ')) for i in range(3)]
# print(L1)

# Модифицируйте последний пример таким образом, чтобы в список сохранялось True, если элемент чётный, и False, если элемент нечётный.
# L2 = [int(input('Введите: ')) % 2 == 0 for i in range(5)]
# print(L2)

print("Задание 5.3.15 А вот здесь нам и поможет использование функций all([ ]) и any([ ])."
      "Замените знаки «?» таким образом, чтобы программа выводила True, если есть хотя бы одно чётное число.")

# L3 = [int(input('Введите: ')) % 2 == 0 for i in range(5)]
# print(any(L3))


print("Задание 5.3.16. Подумайте, как нужно записать логическое выражение, используя all([ ]) и any([ ]) "
      "над списком чётности, если его результат будет истинным тогда и только тогда, когда в списке есть хотя бы "
      "один чётный и хотя бы один нечётный элемент.")
s= [1,2]
print(any(s) and not any(s))

# zip() Рассмотрим ещё одну полезную «фичу», которая упрощает работу со списками в циклах (а значит, и во вложенных генераторах).

print("Задание 5.3.17 Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков L и M")

L4 = [1, 2, 3]
M4 = [3, 2, 1]

n = [a*b for a,b in zip(L4,M4)]
print(n)

print("Задание 5.3.18 Реализуйте программу, которая сжимает последовательность символов. "
      "На вход подаётся последовательность вида")
text = 'aaabbccccdaa'
first = text[0]
count = 0
res = ''
for i in text:
    if i == first:
        count += 1
    else:
        res += first + str(count)
        first = i
        count = 1
res += first + str(count)
print(res)