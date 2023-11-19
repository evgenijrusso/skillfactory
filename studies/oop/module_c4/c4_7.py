# C4.7. Алгоритмы поиска
## Линейный поиск

def find(element, array):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


# array = list(map(int, input('МАсссив чисел: ').split()))
# element = int(input("Поисковое число: "))
#print(find(element, array))

def count(element, array):
    count_ = 0
    for a in array:
        if a == element:
            count_ += 1
    return count_

# Двоичный поиск
# Алгоритм двоичного поиска является более совершенным, чем линейный поиск, однако он накладывает на
# структуру сильное ограничение — она должна быть отсортирована.

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит, элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input('число: '))
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 99))