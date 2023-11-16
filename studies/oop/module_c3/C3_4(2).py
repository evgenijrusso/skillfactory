# Задание 3.4.4
# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.

# with open('input.txt', 'r', encoding='utf8') as fr:
#     for line in fr:
#         print(line, end='')


with open('input.txt', 'r', encoding='utf8') as fr:
    with open('output.txt', 'w', encoding='utf8') as fw:
        for line in fr:
            fw.write(line)

print('======== Задание 3.4.5 ===========')
# Дан файл numbers.txt, компоненты которого являются действительными числами
# (файл создайте самостоятельно и заполните любыми числами, в одной строке одно число).
# Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt.
# p.s. дожлна быть обязательно  после списка пустая строа


with open('numbers.txt', 'r', encoding='utf-8') as fr:
    with open('out.txt', 'w', encoding='utf-8') as fw:
        lst = [float(line[:-1]) for line in fr]
        s_min = min(lst)
        s_max = max(lst)
        print(lst)
        print(s_min, ' - ', s_max)
        fw.write(f's_min: {s_min}\n')
        fw.write(f's_max: {s_max}\n')

import re
print('')
print('======== Задание 3.4.6 ===========')
# В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную.
# Выведите на экран всех учащихся, чья оценка меньше 3 баллов.
with open('student.txt', 'r', encoding='utf-8') as fr:
   lt = [line[:-1] for line in fr]  # выбрал в список всех учащихся и их баллы
   ltfio = [line[:-2] for line in lt]  # только фио (убрвл цифру и пробел
   grade = [int(sub.split('. ')[1]) for sub in lt] # только оценки
   d = dict(zip(ltfio, grade))    # создание из двух списков словаря
   d3 = [v for v in d.values() if v<3]
   u3 = {k: v for k,v in d.items() if v<3}  # это правильно

   #u3 = [j for j in d.keys()]
   #digit = re.findall(r'\b\d+\b',lt)   # выбрать только цифры из строки
   # lt_num = [line for line in re.findall(r'\b\d+\b',lt)]  # только фио
   print('lt: ', lt, ' - ', len(lt))
   print('lffio: ', ltfio, ' - ', len(ltfio))
   print('grade: ', grade, ' - ', len(grade))
   print('d: ', d, ' - ', len(d))
   print('меньше 3 баллов (d3): ', d3)
   print('меньше 3 баллов (u3): ', u3)

# p.s Простое решение
# with open('input.txt', encoding="utf8") as file:
#     for line in file:
#         points = int(line.split()[-1])
#         if points < 3:
#             name = " ".join(line.split()[:-1])
#             print(name)



# Пример:
# initializing list
# test_list = ['Rs. 24', 'Rs. 18', 'Rs. 8', 'Rs. 21']
# printing original list
# print("The original list : " + str(test_list))
# using list comprehension + split()
# Extracting numbers from list of strings
# res = [int(sub.split('.')[1]) for sub in test_list]
# print result
# print("The list after Extracting numbers : " + str(res))

# Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).
print('')
print('======== Задание 3.4.7 ===========')
with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)
