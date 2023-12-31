# Вопрос 6
# Уровень 2
#
# Вопрос: Напишите программу, которая вычисляет и печатает значение в соответствии с приведенной формулой:
# Q = квадратный корень из [(2 * C * D)/H]
# Ниже приведены фиксированные значения C и H: C равно 50. H равно 30. D - это переменная, значения которой должны
# вводиться в вашу программу в последовательности, разделенной запятыми.
# Пример Давайте предположим, что программе задана следующая последовательность ввода,
# разделенная запятыми: 100,150,180 Выходные данные программы должны быть: 18,22,24
#
# Подсказки: Если полученные выходные данные представлены в десятичной форме, их следует округлить до ближайшего
# значения (например, если полученные выходные данные равны 26.0, они должны быть напечатаны как 26). В случае ввода
# данных в вопрос следует предположить, что это ввод с консоли.
#
# Решение:

c = 50
h = 30
q = []


def Qroot(nums):
    for d in nums:
        q.append(int(((2 * c * int(d)) / h) ** 0.5))
    return q


spisok = input('введите числа ')
D = list(spisok.split(','))
print(D)
print('result: ', Qroot(D))

#  решение задачи из сборника (по другому)
# import math
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#
# print(','.join(value))