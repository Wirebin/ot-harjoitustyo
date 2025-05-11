import unittest
import pygame
from pygame import Rect
from game.sub_board import SubBoard
from game.turn_manager import TurnManager

class TestSubBoard(unittest.TestCase):
    def setUp(self):
        turn_manager = TurnManager(False)
        self.board = SubBoard(turn_manager, (200, 100), 50)

    def test_correct_location(self):
        self.assertEqual(self.board.location, (200, 100))

    def test_correct_tile_size(self):
        self.assertEqual(self.board.tile_size, 50)

    def test_correct_border_size(self):
        self.assertEqual(self.board.border_size, 5)

    def test_correct_border_rect(self):
        self.assertEqual(self.board._border_rect, Rect(200 - 5,
                                                      100 - 5,
                                                      50 * 3 + 5 * 2,
                                                      50 * 3 + 5 * 2))
    def test_on_tile_click(self):
        self.board._on_tile_click(self.board.tiles[0], 0)
        self.board._on_tile_click(self.board.tiles[3], 3)
        self.board._on_tile_click(self.board.tiles[1], 2)
        self.board._on_tile_click(self.board.tiles[5], 5)
        self.board._on_tile_click(self.board.tiles[2], 2)
        self.assertEqual(self.board.tiles[0].flagged, True)
        self.assertEqual(self.board.tiles[0].tile_owner, False)
        self.assertEqual(self.board.turn_manager.get_turn(), True)
        self.assertEqual(self.board.turn_manager.get_move(), 2)
        if self.board._check_win_sub(False):
            self.assertEqual(self.board.result, False)

    def test_win_check(self):
        self.assertEqual(self.board._check_win_sub(False), False)
        self.assertEqual(self.board._check_win_sub(True), False)
        for tile in self.board.tiles:
            tile.tile_owner = False
        self.assertEqual(self.board._check_win_sub(False), True)
        self.assertEqual(self.board._check_win_sub(True), False)
