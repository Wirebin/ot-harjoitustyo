import unittest
from input.one_press_input import OnePressInput

class TestOnePressInput(unittest.TestCase):
    def setUp(self):
        OnePressInput._prev_mouse_state = (0, 0, 0)
        OnePressInput._current_mouse_state = (0, 0, 0)

    def test_is_mouse_clicked_on_button_index(self):
        OnePressInput._prev_mouse_state = (1, 0, 0)
        self.assertTrue(OnePressInput.is_mouse_clicked(0))

        OnePressInput._prev_mouse_state = (0, 1, 0)
        self.assertTrue(OnePressInput.is_mouse_clicked(1))

        OnePressInput._prev_mouse_state = (0, 0, 1)
        self.assertTrue(OnePressInput.is_mouse_clicked(2))

        self.assertFalse(OnePressInput.is_mouse_clicked(3))

    def test_input_update(self):
        OnePressInput._prev_mouse_state = (0, 0, 0)
        OnePressInput._current_mouse_state = (1, 0, 1)
        OnePressInput.update()
        self.assertEqual(OnePressInput._prev_mouse_state, (1, 0, 1))
        self.assertEqual(OnePressInput._current_mouse_state, (0, 0, 0))
