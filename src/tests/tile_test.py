import unittest
import pygame
from game.tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile((100,200), 10)

    def test_correct_location(self):
        self.assertEqual(self.tile._location, (100, 200))

    def test_correct_size(self):
        self.assertEqual(self.tile._size, 10)

    def test_flagged_starts_as_false(self):
        self.assertEqual(self.tile.flagged, False)

    def test_tile_owner_starts_as_none(self):
        self.assertEqual(self.tile.tile_owner, None)
