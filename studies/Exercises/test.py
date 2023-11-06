table = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


# row, coll = map(int, input('Ввод через пробел n-строки и n-столбца: ').split())
# row, coll = input('row: '), input('coll: ')
# print('row, coll:', row, coll)

def win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][0] == player:
        return True

    if board[0][0] == player and board[1][1] == player and board[2][0] == player:
        return True


curr_player = 'x'

while False:
    print_board(table)
    print('Ход игрока', curr_player)
    row, coll = 1, 1

    if table[row][coll] != '-':
        print('Ячейка занята')
        continue

    table[row][coll] = curr_player

    if win(table, curr_player):
        print_board(table)
        print(f' Игрок {curr_player} выиграл')
        break

    if all([cell != '-' for row in table for cell in row]):
        print('Ничья')
        print_board()
        break

    curr_player = 'o' if curr_player == 'x' else 'x'
