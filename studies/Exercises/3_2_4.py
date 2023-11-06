#  Год является високосным, если он кратен 4 и при этом не кратен 100 либо кратен 400.

#year = 2000


def is_leap_year(x):
    if (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0)):
        return True
    else:
        return False


year = int(input('введите год: '))


print(is_leap_year(year))

# p.s.
# Введите свое решение ниже и прошло....
# def is_leap_year(x):
#     if (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0)):
#         return True
#     else:
#         return False

#Напишите выражение (задание на самопроверку).
#Дано n-значное целое число N. Определить: входят ли в него цифры 3 и 7

digit = input('get value:')

print('3' in str(digit) or '7' in str(digit))
