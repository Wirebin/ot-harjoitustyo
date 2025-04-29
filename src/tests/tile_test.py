import unittest
import pygame
from game.tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile((100,200), 10)

    def test_correct_location(self):
        self.assertEqual(self.tile.location, (100, 200))

    def test_correct_size(self):
        self.assertEqual(self.tile.size, 10)

    def test_flagged_starts_as_false(self):
        self.assertEqual(self.tile.flagged, False)

    def test_tile_owner_starts_at_zero(self):
        self.assertEqual(self.tile.tile_owner, 0)

    def test_tile_draw(self):
        self.tile.draw(pygame.Surface((0, 0)))
        self.tile.flagged = True
        self.tile.draw(pygame.Surface((0, 0)))
        self.tile.tile_owner = 1
        self.tile.draw(pygame.Surface((0, 0)))
        self.tile.tile_owner = 2
        self.tile.draw(pygame.Surface((0, 0)))
