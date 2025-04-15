import unittest
from sub_board import SubBoard
from pygame import Rect

class TestSubBoard(unittest.TestCase):
    def setUp(self):
        self.board = SubBoard((200, 100), 50)

    def test_correct_location(self):
        self.assertEqual(self.board.location, (200, 100))

    def test_correct_tile_size(self):
        self.assertEqual(self.board.tile_size, 50)

    def test_correct_border_size(self):
        self.assertEqual(self.board.border_size, 5)

    def test_correct_border_rect(self):
        self.assertEqual(self.board.border_rect, Rect(200 - 5,
                                                      100 - 5,
                                                      50 * 3 + 5 * 2,
                                                      50 * 3 + 5 * 2))
