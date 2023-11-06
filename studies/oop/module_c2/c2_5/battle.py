# Итоговое задание 2.5.1 (HW-02)
from random import randint, choice
from time import sleep


class BoardException(Exception):
    pass


class BoardWrongShipException(BoardException):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return 'Выстрел за пределы доски!'


class BoardUsedException(BoardException):
    def __str__(self):
        return 'В эту клетку вы уже стреляли!'


"""
класс точек на поле. Каждая точка описывается параметрами:
Координата по оси x .
Координата по оси y .
"""


class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot({self.x}, {self.y})'


class Ship:
    """
    Параметры:

    Длина - length.
    Точка, где размещён нос корабля - dota.
    Направление корабля (вертикальное/горизонтальное) - gorizon.
    Количеством жизней (сколько точек корабля ещё не подбито) - count_wise.

    И имеет метод dots, который возвращает список всех точек корабля.
    """

    def __init__(self, dota: Dot, length: int, gorizon: bool):
        self.length = length
        self.dota = dota
        self.gorizon = gorizon
        self.lives = length

    @property
    def dots(self) -> list[int, int]:  # возвращает список всех точек корабля
        dots_ship = []
        for i in range(self.length):
            current_x = self.dota.x
            current_y = self.dota.y
            if self.gorizon:
                current_x += i
            else:
                current_y += i
            dots_ship.append(Dot(current_x, current_y))
        return dots_ship

    def is_hit(self, dot) -> bool:
        return dot in self.dots


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
        result = '  | ' + ' | '.join(map(str, range(1, self.size + 1))) + ' |'
        for i, row in enumerate(self.field):
            result += f'\n{i + 1} | ' + ' | '.join(row) + ' |'
            if self.hid:
                result = result.replace('■', '0')
        return result

    def out(self, d: Dot) -> bool:  # Метод out, который для точки (объекта класса Dot) возвращает True,
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
        around = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        for dot in ship.dots:
            for dx, dy in around:
                current_dot = Dot(dot.x + dx, dot.y + dy)
                if not self.out(current_dot) and current_dot not in self.busy:
                    if visible:  # видно контур
                        self.field[current_dot.x][current_dot.y] = '.'
                    self.busy.append(current_dot)

    def set_hid(self):  # выводит доску в консоль в зависимости от параметра hid.
        return self.hid if True else False

    # Метод shot, который делает выстрел по доске (если есть попытка выстрелить за пределы и
    # в использованную точку, нужно выбрасывать исключения)
    def shot(self, d: Dot) -> bool:  # возвращает True, если нужно ход переходить
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

    def begin(self):  # начало
        self.busy = []

    def defeat(self):  # все корабли погибли
        return self.count_destr_ships == len(self.ships)


class Player:
    """
    Внешняя логика: класс Player — класс игрока в игру (и AI, и пользователь).
    Этот класс будет родителем для классов с AI и с пользователем.
    Игрок описывается параметрами:
    Собственная доска (объект класса Board) - my_board.
    Доска врага -ai_board.
    """

    def __init__(self, board: Board, rival: Board):
        self.board = board
        self.rival = rival

    def ask(self):
        """
        метод, который «спрашивает» игрока, в какую клетку он делает выстрел.
        Пока мы делаем общий для AI и пользователя класс, этот метод мы описать не можем.
        Оставим этот метод пустым. Тем самым обозначим, что потомки должны реализовать этот метод.
        """

    pass

    def move(self) -> bool:
        """
        метод, который делает ход в игре. Тут мы вызываем метод ask, делаем выстрел по вражеской доске
        (метод Board.shot), отлавливаем исключения, и если они есть, пытаемся повторить ход.

        :return: Метод должен возвращать True, если этому игроку нужен повторный ход
        (например, если он выстрелом подбил корабль).
        """
        while True:
            try:
                target = self.ask()
                repeat = self.rival.shot(target)
                sleep(1)
                return repeat
            except BaseException as e:
                print('Какая-то ошибка', e)


class AI(Player):
    def ask(self) -> Dot:  # логика компьютера
        last = self.rival.last_hit
        while True:
            if last:  # добивание раненого корабля
                if len(last) == 1:
                    near = ((0, 1), (0, -1), (1, 0), (-1, 0))
                else:
                    if last[0].x == last[-1].x:
                        near = ((0, 1), (0, -1))
                    else:
                        near = ((1, 0), (-1, 0))
                dx, dy = choice(near)
                d = choice((Dot(last[-1].x + dx, last[-1].y + dy), Dot(last[0].x + dx, last[0].y + dy)))
            else:
                d = Dot(randint(0, 5), randint(0, 5))
            if d not in self.rival.busy and not self.rival.out(d):
                break
        sleep(0.1 * randint(15, 50))  # имитация "мыслительной работы" компьютера
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class User(Player):
    def ask(self) -> Dot:
        while True:
            coords = input('Введите координаты выстрела:\t').split()
            if len(coords) != 2:
                print('Введите 2 координаты')
                continue
            x, y = coords
            if not all((x.isdigit(), y.isdigit())):
                print('Координаты должны быть числами')
                continue
            return Dot(int(x) - 1, int(y) - 1)


class Game():
    """
    Игра описывается параметрами:

    Игрок-пользователь, объект класса User.
    Доска пользователя user_board.
    Игрок-компьютер, объект класса AI.
    Доска компьютера ai_board.

    И имеет методы:

    random_board — метод генерирует случайную доску.
    Для этого мы просто пытаемся в случайные клетки изначально пустой доски расставлять корабли
    (в бесконечном цикле пытаемся поставить корабль в случайную доску, пока наша попытка не окажется успешной).
    Лучше расставлять сначала длинные корабли, а потом короткие. Если было сделано много (несколько тысяч)
    попыток установить корабль, но это не получилось, значит доска неудачная и на неё корабль уже не добавить.
    В таком случае нужно начать генерировать новую доску.

    greet — метод, который в консоли приветствует пользователя и рассказывает о формате ввода.

    loop — метод с самим игровым циклом. Там мы просто последовательно вызываем метод mode для игроков и делаем проверку,
    сколько живых кораблей осталось на досках, чтобы определить победу.

    start — запуск игры. Сначала вызываем greet, а потом loop.
    """

    def __init__(self, size=6):
        self.ships_len = (3, 2, 2, 1, 1, 1, 1)  # список кораблей
        self.size = size
        ai_board = self.random_board()
        user_board = self.random_board()
        ai_board.hid = True

        self.ai = AI(ai_board, user_board)
        self.pl = User(user_board, ai_board)

    def random_board(self):  # перебираем случайным образом доски
        board = None
        while board is None:
            board = self.generate_board()
        return board

    def generate_board(self):  # случайным образом вибираю доски с кораблями
        attempts = 0
        board = Board(size=self.size, hid=False)
        for l in self.ships_len:
            while True:
                attempts += 1
                if attempts > 256:
                    return None
                ship = Ship(Dot(randint(0, self.size), (randint(0, self.size))), l, bool(randint(0, 1)))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    @staticmethod
    def greet():
        print('-------------------')
        print('  Приветсвуем вас  ')
        print('      в игре       ')
        print('    морской бой    ')
        print('-------------------')
        print(' формат ввода: x y ')
        print(' x - номер строки  ')
        print(' y - номер столбца ')
        print('-------------------')

    def print_boards(self):  # вывод двух досок рядом по горизонтали
        print('-' * self.size * 10)
        print('Ваша доска:'.ljust((self.size + 1) * 4 - 1) + ' ' * self.size + 'Доска компьютера:')
        for s1, s2 in zip(self.pl.board.__str__().split('\n'), self.ai.board.__str__().split('\n')):
            print(s1 + ' ' * self.size + s2)

    def loop(self):
        step = 0
        while True:
            self.print_boards()
            if step % 2 == 0:
                print('Ваш ход!')
                repeat = self.pl.move()
            else:
                print('Ходит компьютер!')
                repeat = self.ai.move()
            if repeat:
                step -= 1

            if self.ai.board.defeat():
                self.print_boards()
                print('Вы выиграли!')
                break
            if self.pl.board.defeat():
                self.print_boards()
                print('Компьютер выиграл!')
                break
            step += 1

    def start(self):
        self.greet()
        self.loop()


# ---  создаю экземпляр класса --------


gamer = Game()
gamer.start()
