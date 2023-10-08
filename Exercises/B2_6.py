numbers = '1 2 3 4 5 6 7'
t = numbers.split()
print('\n'.join(t))

pi = 31.4159265
print ("%.4e" % (pi))

hours, minutes, seconds = 1, 2, 3
print("%02d:%02d:%02d" % (hours, minutes, seconds))

L = ["а", "б", "в", 1, 2, 3, 4]
print('1:', L[1:4:1])
print('2:', L[0::3])
print('3:', L[-4::-1])   #[3::-1]
print('4:', L[:-4:-1])

list_of_string = '1 1 2 3 5 8 13 21 34 55'.split()  # список строковых представлений чисел
print('s:', list_of_string)
fibo = list(map(int, list_of_string))
print('int: ', fibo)
fibo[0], fibo[-1] = fibo[-1], fibo[0]
fibo.append(sum(fibo))
print('result: ', fibo)

d = {'day' : 22, 'month' : 6, 'year' : 2015}
print("||".join(d.keys()))
# ================= 2.6.11 ============================
entry = 'title Qwerty author Swift year 1900'.split()
print('entry:', entry)
keys = [entry[0], entry[2], entry[4]]
values = [entry[1], entry[3], int(entry[5])]
print('keys:', keys)
print('values:', values)
d = dict(zip(keys, values))
print('d:', d)

b = 'title author year'
title = 'Алиса в стране чудес'
author = 'Кэрролл'
year = '1865'
print({'title': title, 'author': author, 'year': int(year)})

# Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.
entry = 'мама папа и дети мама и дед и баба'
sp = entry.split()
unique = list(set(sp))
print('unique:', unique)
print("Количество уникальных символов: ", len(unique))

# ============== 2.6.13 ==========================
# Используя алгоритм из прошлой задачи, найдите количество уникальных символов в тексте. Скопируйте его к себе в
# консоль целиком.

entry = "The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
#print('entry: ', entry)
sp = entry
unique = list(set(sp))
print('Zen:', len(unique))

# string = input("Введите числа через пробел:")
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка