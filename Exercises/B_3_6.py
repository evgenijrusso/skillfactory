# B3.6. Циклы
S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

print('Задание 3.6.1')
start = 20
end = 1
step = -2
count = 0
for i in range(start, end, step):
    count += 1
    print("Текущее число и число циклоы: ", i, ' ', count)

# Задание 3.6.2

print("\n")
print('Задание 3.6.2 ', 'подсчитать произведение всех чисел от 1 до N включительно.')
n = 5  # заводим переменную-счётчик, в которой мы будем считать сумму
p = 1
for i in range(1, n + 1):
    p *= i  # умнождаем текущее число i и перезаписываем значение произведения
    print("Текущее число: ", i)
    print("Значение произведения после умножения: ", p)
print("Ответ: произведение равна = ", p)

# Задание 3.6.3 Написать программу, которая будет печатать лесенку следующего типа:
print("3.6.3")
n = 3
for i in range(1, n + 1):
    print('*' * i)

# Задание 3.6.4 Напишите цикл while, который находит максимальное натуральное число, квадрат которого меньше 1000.
print('1 вариант')
n = 1
q = 1
while q < 1000:
    q = n ** 2
    n += 1
    print('Считаю...')
print('число', q ** 0.5)
print('Кол-во чисел', n)

print('2 вариант')
n = 1
while n ** 2 < 1000:
    n += 1
print('число', n)

# Задание 3.6.5 Напишите бесконечный цикл while с условием выхода внутри цикла, находящего максимальное натуральное
# число, квадрат которого меньше 1000.

print('\n', 'Задание 3.6.5')
n = 1
while True:
    print('Бесконечный цикл')
    if n ** 2 >= 1000:
        print('Остановились ', n - 1)
        break
    n += 1

# Пример 3. Условие задачи: дана двумерная матрица 3x3 (двумерный массив).
# Определить максимум и минимум каждой строки, а также их индексы.

random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []

for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]

    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col

        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col

    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print('Минимальные элементы:', min_value_rows)
print('Их индексы:', min_index_rows)
print('Максимальные элементы:', max_value_rows)
print('Их индексы:', max_index_rows)
