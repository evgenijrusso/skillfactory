import unittest

from oop.module_c2.c2_5.ships import Dot


def dots(self) -> list:  # возвращает список всех точек корабля
    dots_ship = []
    for i in self.length:
        current_x = self.dota.x
        current_y = self.dota.y
        if self.gorizon:
            current_x += 1
        else:
            current_y += 1
        dots_ship.append(Dot(current_x, current_y))
    return dots_ship


class MyTestCase(unittest.TestCase):
    def test_dots(self):
        dots_ship_list = [(1, 1), (1, 2)]
        self.assertEqual(dots_ship_list, [(1, 1), (1, 2)])  # add assertion here


