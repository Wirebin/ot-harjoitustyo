import unittest
from state_manager import StateManager
from states import GameStates

class TestStateManager(unittest.TestCase):
    def setUp(self):
        self.state_manager = StateManager()

    def test_default_state_to_first(self):
        self.assertEqual(self.state_manager.current_state, GameStates.MENU)

    def test_state_amount(self):
        self.assertEqual(self.state_manager.state_amount, 3)

    def test_next_state(self):
        self.state_manager.next_state()
        self.assertEqual(self.state_manager.current_state, GameStates.GAME)
