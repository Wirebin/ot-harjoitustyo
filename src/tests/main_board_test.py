import unittest
from game.main_board import MainBoard
from game.turn_manager import TurnManager
from config.constants import WINNING_COMBOS

class TestMainBoard(unittest.TestCase):
    def setUp(self):
        turn_manager = TurnManager(False)
        self.board = MainBoard(None, turn_manager, (200, 100), 50)

    def test_correct_location(self):
        self.assertEqual(self.board.location, (200, 100))

    def test_correct_border_size(self):
        self.assertEqual(self.board.border_size, 5)

    def test_sub_board_list_size(self):
        self.assertEqual(len(self.board.sub_boards), 9)

    def test_board_reset_correctly(self):
        self.board.reset_board()
        self.assertEqual(self.board.turn_manager.get_turn(), False)
        self.assertEqual(self.board.turn_manager.get_move(), None)
        self.assertEqual(len(self.board.sub_boards), 9)

    def test_win_check(self):
        self.assertEqual(self.board._check_win_main(False), False)
        self.assertEqual(self.board._check_win_main(True), False)
        for board in self.board.sub_boards:
            board.result = False
        self.assertEqual(self.board._check_win_main(False), True)
        self.assertEqual(self.board._check_win_main(True), False)
