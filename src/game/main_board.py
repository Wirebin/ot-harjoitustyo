from math import ceil
import pygame
from game.sub_board import SubBoard
from game.states import GameStates

class MainBoard():
    def __init__(self, state_manager, location: tuple, tile_size: int):
        self.state_manager = state_manager
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
            [0, 0, 1, 0, 1, 0, 1, 0, 0]
        )

        self.sub_boards = []
        for i in range(3):
            for j in range(3):
                self.sub_boards.append(SubBoard(self,
                    (self.location[0] + i * (tile_size * 3 + self.border_size),
                     self.location[1] + j * (tile_size * 3 + self.border_size)),
                     tile_size))


    def check_win_main(self, player):
        # Create main game from the sub_board results
        main_board = [board.tile_owner for board in self.sub_boards]
        # Replace only the current player numbers with 1 and the rest with 0
        replaced_board = [1 if tile == player else 0 for tile in main_board]

        # Compare the created main board with the winning combinations and check for win
        for combination in self.winning_combos:
            if all(replaced_board[i] == value for i, value in
                   enumerate(combination) if value == 1):
                return True
        return False


    def update(self):
        # Main Board Logic
        for sub_board in self.sub_boards:
            # Board game has already finished, skipping.
            if sub_board.tile_owner:
                continue

            # Update a board
            sub_board.update()

            if self.check_win_main(1) or self.check_win_main(2):
                self.state_manager.go_to_state(GameStates.RESULT)


    def draw(self, screen):
        for sub_board in self.sub_boards:
            sub_board.draw(screen)
