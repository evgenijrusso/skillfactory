import unittest

from oop.module_c2.c2_5.ships import Dot

from studies.oop.module_c2.c2_5.boards import Board


class TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.board_1 = Board(hid=True, size=5)
        self.board_2 = Board(hid=False, size=0)
        print("\nRunning setUp method...")

    def tearDown(self):
        print("Running tearDown method...")

    def test_set_hid(self):
        print("Running test_set_hid method...")
        self.assertEqual(self.board_1.set_hid(), True)
        self.assertEqual(self.board_2.set_hid(), False)
        self.assertTrue(self.board_1.set_hid(), True)
        self.assertFalse(self.board_2.set_hid(), False)

    def test_out(self, d: Dot) -> bool:
        self.assertTrue(self.board_1.out(list(d.x, d.y)), True)


