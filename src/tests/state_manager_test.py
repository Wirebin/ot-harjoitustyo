import unittest
from state_manager import State_Manager
from states import Game_States

class TestStateManager(unittest.TestCase):
    def setUp(self):
        self.state_manager = State_Manager()

    def test_default_state_to_first(self):
        self.assertEqual(self.state_manager.current_state, Game_States.MENU)

    def test_state_amount(self):
        self.assertEqual(self.state_manager.state_amount, 3)

    def test_next_state(self):
        self.state_manager.next_state()
        self.assertEqual(self.state_manager.current_state, Game_States.GAME)
        