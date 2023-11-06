# Итоговое задание 2.5.1 (HW-02)
#from typing import List, Tuple

class BoardException(Exception):
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
    def __init__(self, dota: Dot, length:int, gorizon:bool):
        self.length = length
        self.dota = dota
        self.gorizon = gorizon
        self.lives = lives = 3
    @property
    def dots(self) -> list[int, int]: # возвращает список всех точек корабля
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