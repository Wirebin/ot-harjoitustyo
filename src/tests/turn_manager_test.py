import unittest
from game.turn_manager import TurnManager

class TestTurnManager(unittest.TestCase):
    def setUp(self):
        self.turn_manager = TurnManager(False)

    def test_get_turn_method(self):
        self.assertEqual(self.turn_manager.get_turn(), False)

    def test_update_turn_method(self):
        self.turn_manager.update_turn(True)
        self.assertEqual(self.turn_manager.get_turn(), True)
        self.turn_manager.update_turn(False)
        self.assertEqual(self.turn_manager.get_turn(), False)

    def test_get_move_method(self):
        self.assertEqual(self.turn_manager.get_move(), None)

    def test_update_move_method(self):
        self.turn_manager.update_move(0)
        self.assertEqual(self.turn_manager.get_move(), 0)

    def test_is_winner_correct(self):
        self.assertEqual(self.turn_manager.get_winner(), None)
        self.turn_manager.set_winner(False)
        self.assertEqual(self.turn_manager.get_winner(), False)
        self.turn_manager.set_winner(True)
        self.assertEqual(self.turn_manager.get_winner(), True)
