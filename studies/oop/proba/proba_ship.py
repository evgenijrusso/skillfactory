from oop.module_c2.c2_5.ships import Ship, Dot, BoardOutException

print(' ------- Dot ---------')
ex_dot1 = Dot(1, 2)
print('dx,dy:', ex_dot1.x, ex_dot1.y)
print('ex_dot1', ex_dot1.__str__())

# добавил @property, тем самым преобразовал метод в атрибут
print('\n ------- Ship (dots)---------')
ex_ship1 = Ship(Dot(1, 1), 3, True)
list_dots = ex_ship1.dots
print('__dict__:', ex_ship1.__dict__)
for i in list_dots:
    print('list_dots:', i)

print('\n ------- Ship (is_hit)---------')

dot = Dot(2, 1)
if dot in list_dots:
    print('is_hit:', dot, ' ', True)
else:
    print('is_hit:', False)

