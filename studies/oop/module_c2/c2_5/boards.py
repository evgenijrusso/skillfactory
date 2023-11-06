from oop.module_c2.c2_5.ships import Ship, Dot
class Board:
    """
     Игровая доска. Доска описывается параметрами:

    Двумерный список, в котором хранятся состояния каждой из клеток - size.
    Список кораблей доски - ships.
    Параметр hid типа bool — информация о том, нужно ли скрывать корабли на доске (для вывода доски врага) или нет (для своей доски).
    Количество живых кораблей на доске - live_count_ships.
    """

    def __init__(self, size: int, hid: False):
        self.size = size
        self.busy = []
        self.ships = []
        self.hid = hid
        self.last_hit = []  # список точек, раненого корабля
        self.field = [['0'] * size for _ in range(size)]
        self.count_destr_ships = 0  # счетчик уничтоженных кораблей

    def __str__(self):
        result = '  | ' + ' | '.join(map(str, range(1, self.size +1))) + ' |'
        for i, row in enumerate(self.field):
            result += f'\n{i+1} | ' + ' | '.join(row) + ' |'
            if self.hid:
                result = result.replace('■', '0')
        return result

    def out(self, d:Dot)-> bool: # Метод out, который для точки (объекта класса Dot) возвращает True,
                          # если точка выходит за пределы поля, и False, если не выходит.
        return not (0 < d.x < self.size and 0 < d.y < self.size)

    def add_ship(self, ship):  # ставит корабль на доску (если ставить не получается, выбрасываем исключения).
        for d in ship.dots:
            if self.busy or self.out(d):
                raise BoardUsedException()
        for d in ship.dots:
            self.field[d.x][d.y] = '■'
            self.busy.append(d)
        self.ships.append()
        self.contour(ship)

    """
     Обводит корабль по контуру. Он будет полезен и в ходе самой игры, и в при расстановке кораблей 
     (помечает соседние точки, где корабля по правилам быть не может).
    """
    def contour(self, ship, visible=False):
        around = [(i,j) for i in range(-1,2) for j in range(-1,2)]
        for dot in ship.dots:
            for dx,dy in around:
                current_dot = Dot(dot.x + dx, dot.y + dy)
                if not self.out(current_dot) and current_dot not in self.busy:
                   if visible: # видно контур
                       self.field[current_dot.x][current_dot.y] = '.'
                   self.busy.append(current_dot)
    def set_hid(self): # выводит доску в консоль в зависимости от параметра hid.
        return self.hid if True else False

   # Метод shot, который делает выстрел по доске (если есть попытка выстрелить за пределы и
   # в использованную точку, нужно выбрасывать исключения)
    def shot(self, d: Dot) -> bool:    #возвращает True, если нужно ход переходить
        if d in self.busy:
            raise BoardUsedException()
        if self.out(d):
            raise BoardOutException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.is_hit(d):
                self.field[d.x][d.y] = 'X'
                print('Попадание!')
                ship.lives -= 1
                if ship.lives == 0:
                    self.count_destr_ships += 1
                    self.contour(ship, visible=True)
                    print('Корабль уничтожен!')
                    self.last_hit = []
                    return False
                else:
                    print('Корабль ранен!')
                    self.last_hit.append(d)
                    return True

        self.field[d.x][d.y] = '.'
        print('Мимо!')
        return False

    def begin(self):    # начало
        self.busy = []

    def defeat(self):    # все корабли погибли
        return self.count_destr_ships == len(self.ships)


