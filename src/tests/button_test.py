import unittest
import pygame
from ui.button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.button = Button((100,100), (100, 50), "Test")

    def test_correct_location(self):
        self.assertEqual(self.button.location, (100, 100))

    def test_correct_size(self):
        self.assertEqual(self.button.size, (100, 50))

    def test_correct_text(self):
        self.assertEqual(self.button.button_text, "Test")
