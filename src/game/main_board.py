from math import ceil
import pygame
from game.sub_board import SubBoard
from game.states import GameStates

class MainBoard():
    """Class that handles the MainBoard.
    """
    def __init__(self, state_manager, location: tuple, tile_size: int):
        """The constructor for the MainBoard class. Creates a MainBoard
        instance at the specified location. 

        Args:
            state_manager (StateManager):
                A state manager instance used to switch game states.
            location (tuple):
                The location of the MainBoard instance.
            tile_size (int):
                The size of a singular tile used for the SubBoard games.
        """
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
        """Checks the winning conditions for the MainBoard.

        Compares the winning combinations with the results from the SubBoard
        games to determine whether a player has won the main game.

        Args:
            player (int):
                The player which the winning conditions will be checked for.

        Returns:
            bool:
                Returns True, if the player has won the SubBoard game.
                Otherwise returns False.
        """
        main_board = [board.result for board in self.sub_boards]
        replaced_board = [1 if tile == player else 0 for tile in main_board]

        for combination in self.winning_combos:
            if all(replaced_board[i] == value for i, value in
                   enumerate(combination) if value == 1):
                return True
        return False


    def update(self):
        """The MainBoard update logic. Goes through the update functions
        of all of the SubBoards and checks for wins.
        """
        for sub_board in self.sub_boards:
            # Board game has already finished, skipping.
            if sub_board.result:
                continue

            sub_board.update()

            if self.check_win_main(1) or self.check_win_main(2):
                self.state_manager.go_to_state(GameStates.RESULT)


    def draw(self, screen):
        """Draws the SubBoards on screen.

        Args:
            screen (pygame.Surface):
                The display screen used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        for sub_board in self.sub_boards:
            sub_board.draw(screen)
