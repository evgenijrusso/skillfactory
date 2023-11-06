from studies.oop.module_c2.c2_5.boards import Board
from  oop.module_c2.c2_5.ships import Ship,Dot, BoardUsedException, BoardOutException

print('===============  Class Board ========================')
ex_board = Board(size=6, hid=False)

# метод  def __str__(self):
print('Выводится доска 6*6')
print(ex_board.__str__(), '\n')

print('------------ def set_hid ->bool: ------------')
if ex_board.set_hid():
    print('def set_hid ->bool  -- True')
else:
    print('def set_hid ->bool -- False')

print('\n', '---------- def out(self, d:Dot)-> bool:--------')
d = Dot(x=1, y=1)
if not (0 < d.x < ex_board.size and 0 < d.y < ex_board.size):
    print('True: - это точка за пределами игрового поля')
else:
    print('False - это точка в пределах игровой доски')

print('\n', '---------- def add(self, ship):--------')
print('ставит корабль на доску (если ставить не получается, выбрасываем исключения')
ex_ship1 = Ship(Dot(1, 1), 3, True)  # экземпляр класса Ship
ex_board.ships = []
ship_dots = ex_ship1.dots            # список точек Ship
for d in ship_dots:
    ex_board.field[d.x][d.y] = '■'
    ex_board.busy.append(d)
ex_board.ships.append(ex_ship1)   # должно появится в ships(list)?
[print(i) for i in ex_board.busy]
[print(j) for j in ex_board.ships]  # ?

print('\n', '---------- def shot(self, d:Dot):--------')
d = Dot(x=3, y=2)
ex_board.busy = [Dot(1,1), Dot(1,2), Dot(1,3),Dot(2,1),Dot(2,2),Dot(2,3)]
print(d)
if d in ex_board.busy:
    print('Выстрел в ногу. Проверка на исключение')
    raise BoardUsedException()
else:
   print('Выстрел в поле')

d = Dot(x=6, y=7)
print(d)
if ex_board.out(d):
    print('Выстрел в аут. Проверка на исключение')
    raise BoardOutException()
else:
   print('Выстрел в поле')

# else:
# raise Exception('error, invalid attrlink')

# pip install keyboard
#
# import keyboard
#
# while True:
#     # do something
#     if keyboard.is_pressed("q"):
#         print("q pressed, ending loop")
#         break