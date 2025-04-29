import unittest
from game.main_board import MainBoard

class TestMainBoard(unittest.TestCase):
    def setUp(self):
        self.board = MainBoard(None, (200, 100), 50)

    def test_correct_location(self):
        self.assertEqual(self.board.location, (200, 100))

    def test_correct_border_size(self):
        self.assertEqual(self.board.border_size, 5)

    def test_sub_board_list_size(self):
        self.assertEqual(len(self.board.sub_boards), 9)

    def test_winning_combination_amount(self):
        self.assertEqual(len(self.board.winning_combos), 8)
