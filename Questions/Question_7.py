# Вопрос 7
# Уровень 2
#
# Вопрос: Напишите программу, которая принимает 2 цифры, X, Y в качестве входных данных и генерирует двумерный массив.
# Значение элемента в i-й строке и j-м столбце массива должно быть i*j.
# Примечание: i=0,1.., X-1; j=0,1,¡Y-1.
# Пример Предположим, что программе заданы следующие входные данные: 3,5
# Тогда выходные данные программы должны быть: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Подсказки: Примечание: В случае ввода данных в вопрос следует предполагать,
# что это консольный ввод в форме, разделенной запятыми.
#
# Решение:

input_str = input('Введите:')
dimensions = [int(x) for x in input_str.split(',')]
print(dimensions)
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
print('-1:', multilist)

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col

print('-2:', multilist)
