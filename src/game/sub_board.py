from math import ceil
import pygame
from ui import shapes
from game.tile import Tile

class SubBoard():
    def __init__(self, main_board, location: tuple, tile_size: int):
        self.main_board = main_board
        self.location = location
        self.tile_owner = 0

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


    def check_win_sub(self, board, player):
        # Replace only the current player numbers with 1 and the rest with 0
        replaced_board = [1 if tile.tile_owner == player else 0 for tile in board.tiles]

        # Compare the created main board with the winning combinations and check for win
        for combination in self.main_board.winning_combos:
            if all(replaced_board[i] == value for i, value in
                   enumerate(combination) if value == 1):
                return True
        return False


    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        for tile in self.tiles:
            # If left-clicked on top of tile.
            if tile.button_rect.collidepoint(mouse_pos) and \
                pygame.mouse.get_pressed(num_buttons=3)[0] and not tile.flagged:
                tile.flagged = True

                if self.main_board.player_turn == 1:
                    tile.tile_owner = 1
                elif self.main_board.player_turn == 2:
                    tile.tile_owner = 2

                if self.check_win_sub(self, self.main_board.player_turn):
                    self.tile_owner = self.main_board.player_turn
                self.main_board.player_turn = 1 if self.main_board.player_turn == 2 else 2


    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.border_rect, self.border_size)

        if self.tile_owner:
            if self.tile_owner == 1:
                shapes.cross(screen,
                             pygame.color.Color(200, 0, 0),
                             self.location,
                             self.tile_size * 3)
            elif self.tile_owner == 2:
                shapes.circle(screen,
                              pygame.color.Color(0, 0, 200),
                              self.location,
                              self.tile_size * 3)
            return

        for tile in self.tiles:
            tile.draw(screen)
