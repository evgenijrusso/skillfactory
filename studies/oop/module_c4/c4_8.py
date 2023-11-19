# Сортировка выбором
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)): # проходим по всему массиву

    idx_min = i # сохраняем индекс предположительно минимального элемента
    for j in range(i+1, len(array)):
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j
        if i != idx_min: # если индекс не совпадает с минимальным, меняем
            array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(count)

# Сортировка пузырьком

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

# Сортировка вставками (3)

count1 = 0
count2 = 0
count3 = 0
count4 = 0
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(1, len(array)):
    x = array[i]
    idx = i

    while idx > 0:
        count4 += 1
        if (array[idx-1] <= x):
            count1 += 1
            break
        array[idx] = array[idx-1]
        count2 += 1
        idx -= 1
    array[idx] = x
    count3 += 1

print('count =: ', count1, "", count2, " ", count3, count4)
# 13

# Задание 4.8.6
# Задание на самопроверку.
# Реализуйте алгоритм сортировки слиянием.


def merge_sort(L):  # «разделяй»
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

# Быстрая сортировка
#Быстрая сортировка в виде танца.

def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
def merge(left, right):  # «властвуй»
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
