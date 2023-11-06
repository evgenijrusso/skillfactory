from oop.module_c2.c2_5.players import User, AI, Board


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


    def random_board(self): # перебираем случайным образом доски
        board = None
        while board is None:
            board = self.generate_board()
        return board


    def generate_board(self): # случайным образом вибираю доски с кораблями
        attempts = 0
        board = Board(size=self.size, hid=False)
        for l in self.ships_len:
            while True:
                attempts += 1
                if attempts > 2000:
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

