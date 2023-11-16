import os
#  Работа с файлами
# В операционных системах UNIX разделительным знаком при записи пути является «/», в Windows — «\».
# Эти знаки служат для разделения названия каталогов, составляющих путь к файлу. Все вы видели,
# например, такой путь на ОС Windows: C:\Program Files. Это и есть путь до папки Program Files.

# Существует два типа пути:
#- абсолютный,
#- относительный.
# Абсолютный путь всегда считается от «корня», той папки, откуда потом вырастают все остальные папки.
# Для Windows это диск С:, D: и т. д., для Unix это «\» (обратный слеш). Абсолютный путь всегда уникальный.

# Чтобы поработать с путями есть модуль os.
# Функция os.chdir() позволяет нам изменить директорию, которую мы в данный момент используем.
# Если вам нужно знать, какой путь вы в данный момент используете, для этого нужно вызвать os.getcwd().

# получить текущий путь
start_path = os.getcwd()
print(start_path)  # C:\works\SkillFactory\studies\oop\module_c3

# Далее попробуем подняться на директорию выше:
os.chdir("..")      # подняться на один уровень выше
print(os.getcwd())  # C:\works\SkillFactory\studies\oop

# Теперь вернёмся в ту директорию, из которой стартовали. Изначально мы сохраняли её в переменной start_path.
os.chdir(start_path)
os.getcwd()
print(os.getcwd())  # C:\works\SkillFactory\studies\oop\module_c3

# список файлов и директорий в папке
print(os.listdir())

# соединяет пути с учётом особенностей операционной системы
print(start_path)
print(os.path.join(start_path, 'test'))

# Сделайте функцию, которая принимает от пользователя путь и выводит всю информацию о содержимом этой папки.
# Для реализации используйте функцию встроенного модуля os.walk(). Если путь не указан, то сравнение начинается
# с текущей директории.

def walk_desc(path=None):
    start_path = path if path is not path else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print('Текущая директория', root)
        print('----------')

        if dirs:
            print('Список каталогов', dirs)
        else:
            print('Каталогов нет')
            print('----------')

        if files:
            print('Список файлов', files)
        else:
            print('файлов нет', files)
            print('----------')

        if files and dirs:
            print('Все пути')

        for f in files:
            print('Файл ', os.path.join(root,f))
        for d in dirs:
            print('Каталог ', os.path.join(root,d))

walk_desc()

