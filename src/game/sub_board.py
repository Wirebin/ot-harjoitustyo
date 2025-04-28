from math import ceil
import pygame
import ui.shapes as shapes
from game.tile import Tile

class SubBoard():
    def __init__(self, main_board, location: tuple, tile_size: int):
        self.main_board = main_board
        self.location = location
        self.result = 0

        self.tile_size = tile_size
        self.border_size = ceil(tile_size / 10)
        self.border_rect = pygame.rect.Rect(
            location[0] - self.border_size,
            location[1] - self.border_size,
            tile_size * 3 + self.border_size * 2,
            tile_size * 3 + self.border_size * 2)

        self.tiles = []
        for i in range(3):
            for j in range(3):
                self.tiles.append(Tile(
                    ((self.location[0] + (i * tile_size)),
                     (self.location[1] + (j * tile_size))),
                    tile_size))


    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        for tile in self.tiles:
            # Board game has already finished, skipping.
            if self.result:
                continue

            # If left-clicked on top of tile.
            if tile.button_rect.collidepoint(mouse_pos) and \
                pygame.mouse.get_pressed(num_buttons=3)[0] and not tile.flagged:
                tile.flagged = True

                if self.main_board.player_turn == 1:
                    tile.tile_owner = 1
                elif self.main_board.player_turn == 2:
                    tile.tile_owner = 2

                if self.main_board.check_win_conditions(self, self.main_board.player_turn):
                    self.result = self.main_board.player_turn
                self.main_board.player_turn = 1 if self.main_board.player_turn == 2 else 2


    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.border_rect, self.border_size)

        if self.result:
            if self.result == 1:
                shapes.cross(screen,
                             pygame.color.Color(200, 0, 0),
                             self.location,
                             self.tile_size * 3)
            elif self.result == 2:
                shapes.circle(screen,
                              pygame.color.Color(0, 0, 200),
                              self.location,
                              self.tile_size * 3)
            return

        for tile in self.tiles:
            tile.draw(screen)
