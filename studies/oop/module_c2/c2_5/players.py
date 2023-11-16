from random import randint, choice

from studies.oop.module_c2.c2_5.boards import Board, Dot


class Player:
    """
    Внешняя логика: класс Player — класс игрока в игру (и AI, и пользователь).
    Этот класс будет родителем для классов с AI и с пользователем.
    Игрок описывается параметрами:
    Собственная доска (объект класса Board) - my_board.
    Доска врага -ai_board.
    """
    def __init__(self, board: Board, rival:Board):
        self.board = board
        self.rival = rival

    def ask(self):
        """
        метод, который «спрашивает» игрока, в какую клетку он делает выстрел.
        Пока мы делаем общий для AI и пользователя класс, этот метод мы описать не можем.
        Оставим этот метод пустым. Тем самым обозначим, что потомки должны реализовать этот метод.
        """
    pass

    def move(self)-> bool:
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
    def ask(self)->Dot:     #  логика компьютера
        last = self.rival.last_hit
        while True:
            if last:    # добивание раненого корабля
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
        sleep(0.1 * randint(15, 50))    # имитация "мыслительной работы" компьютера
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class User(Player):
    def ask(self)->Dot:
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

