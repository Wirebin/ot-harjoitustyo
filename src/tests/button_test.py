import unittest
import pygame
from ui.button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        def click_return_true():
            return True
        self.button = Button((100,100), (100, 50), "Test", click_return_true)

    def tearDown(self):
        pygame.quit()

    def test_correct_location(self):
        self.assertEqual(self.button._location, (100, 100))

    def test_correct_size(self):
        self.assertEqual(self.button._size, (100, 50))

    def test_correct_text(self):
        self.assertEqual(self.button._text._text, "Test")

    def test_on_click_function_working(self):
        self.assertEqual(self.button._on_click(), True)
