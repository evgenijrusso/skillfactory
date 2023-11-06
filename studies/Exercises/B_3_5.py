# Задание 3.5.1 (External resource)
# Запишите вместо вопросительных знаков выражение, которое вернет True, когда каждое из чисел А и В нечетное.

def are_both_odd(A, B):
    if A % 2 != 0 and B % 2 != 0:
        return True
    else:
        return False


def are_both_odd(A, B):
    return A % 2 == 1 and B % 2 == 1


print('============  Задача 3.5.3 ===============')


def get_wind_class(speed):
    if 1 <= speed <= 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return "strong [3]"
    elif speed >= 19:
        return "hurricane [4]"


speed = 1

print(get_wind_class(speed))  #Правильно: без print


print('============  Задача 3.5.4 ===============')

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}


def check_user(username, password):
    if username in user_database.keys():
        if password in user_database[username]:
            return True
        else:
            return False
    else:
        return False


# username = 'user'
# password = 'password'

print(check_user(username='user', password='password'))  # без print

# Тернарный условный оператор
print('============  Задача 3.5.5 (Самостоятельная работа)===============')

# a = int(input('введите первое число\n'))
# b = int(input('введите первое число\n'))
# c = int(input('введите первое число\n'))

a, b, c = 12, 47, 56

if ((a < 45) and (b>=45) and (c>=45) or \
   (a>45) and (b<45) and (c >=45) or \
   (a>=45) and (b>=45) and (c< 45)):
   print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')

# Тернарный условный оператор
print('============  Задача 3.5.7 (Самостоятельная работа)===============')

val = 15


print('целочисленное деление', val // 5)
print('деление с остатком', val % 5)

if (val % 5 == 0) or (val // 5 == 10):
    print('есть в числе цифра 5')
else:
    print('нет в числе цифры 5')


# Тернарный условный оператор
print('============  Задача 3.5.6 (Самостоятельная работа)===============')

a = 7

if not (-10 <= a < -1 or 2 <= a <= 15 ):
    print("Число не принадлежит интервалу")
else:
    print("Число принадлежит интервалу")


print('============  Задача 3.5.8 (Самостоятельная работа)===============')
# Проверить, все ли элементы в списке являются уникальными.
# Решение:
list_ = [5, -2, 0, 7, 12, -7]
print(len(list_) == len(set(list_)))

print('============  Задача 3.5.9 (Самостоятельная работа)===============')
# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково слева направо и
# справа налево)
num = 12345678

print(str(num) == str(num)[::-1])