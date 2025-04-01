import unittest
import pygame
from button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        self.button = Button((100,100), (100, 50), (255,255,255), (0,0,0), "Test")

    def test_correct_location(self):
        self.assertEqual(self.button.location, (100, 100))

    def test_correct_size(self):
        self.assertEqual(self.button.size, (100, 50))

    def test_correct_text(self):
        self.assertEqual(self.button.button_text, "Test")

    def test_correct_normal_color(self):
        self.assertEqual(self.button.color_normal, (255,255,255))

    def test_correct_hover_color(self):
        self.assertEqual(self.button.color_hover, (0,0,0))