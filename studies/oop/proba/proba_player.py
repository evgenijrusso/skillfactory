from studies.oop.module_c2.c2_5.players import Player
from studies.oop.module_c2.c2_5.boards import Board

print('------------- Class Player ------------------')
ex_board_ru = Board(size=6, hid=False)
ex_board_ai = Board(size=6, hid=False)
ex_player = Player(board=ex_board_ru, rival=ex_board_ai)
print(ex_player.__dict__)
print('------------- def move ------------------')
# создаю экземпляр класса и тестю метод def move(self) через debug
ex_player.move() #  поставить bp