from math import ceil
import pygame
from component import Component
from sub_board import SubBoard


class MainBoard(Component):
    def __init__(self, location: tuple, tile_size: int):
        self.location = location
        self.border_size = ceil(tile_size / 10)
        self.border_rect = pygame.rect.Rect(
            location[0] - self.border_size,
            location[1] - self.border_size,
            tile_size * 9 + self.border_size,
            tile_size * 9 + self.border_size)

        self.player_turn = 1
        self.winning_combos = (
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
        )

        self.sub_boards = []
        for i in range(3):
            for j in range(3):
                self.sub_boards.append(SubBoard(
                    (self.location[0] + i * (tile_size * 3 + self.border_size),
                     self.location[1] + j * (tile_size * 3 + self.border_size)),
                     tile_size))


    def check_win_conditions(self, board, player):
        replaced_board = [1 if tile.tile_owner == player else 0 for tile in board.tiles]

        for combination in self.winning_combos:
            if all(replaced_board[i] == combination[i] for i, 
                   value in enumerate(combination) if value == 1):
                return True
        return False


    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        # Main Board Logic
        for board in self.sub_boards:
            for tile in board.tiles:
                # Board game has already finished, skipping.
                if board.result:
                    continue

                # If left-clicked on top of tile.
                if tile.button_rect.collidepoint(mouse_pos) and \
                    pygame.mouse.get_pressed(num_buttons=3)[0] and not tile.flagged:
                    tile.flagged = True

                    if self.player_turn == 1:
                        tile.tile_owner = 1
                    elif self.player_turn == 2:
                        tile.tile_owner = 2

                    if self.check_win_conditions(board, self.player_turn):
                        board.result = self.player_turn
                    self.player_turn = 1 if self.player_turn == 2 else 2

        for sub_board in self.sub_boards:
            sub_board.update()


    def draw(self, screen):
        for sub_board in self.sub_boards:
            sub_board.draw(screen)
