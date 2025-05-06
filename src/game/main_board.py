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
        self.tile_size = tile_size
        self.location = location
        self.border_size = ceil(tile_size / 10)
        self.border_rect = pygame.rect.Rect(
            location[0] - self.border_size,
            location[1] - self.border_size,
            tile_size * 9 + self.border_size,
            tile_size * 9 + self.border_size)

        self.player_turn = 1
        self.current_move = None
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


    # def reset(self):
    #     """Resets the board back to the original state.
    #     """
    #     self.player_turn = 1
    #     self.sub_boards = []
    #     for i in range(3):
    #         for j in range(3):
    #             self.sub_boards.append(SubBoard(self,
    #                 (self.location[0] + i * (self.tile_size * 3 + self.border_size),
    #                  self.location[1] + j * (self.tile_size * 3 + self.border_size)),
    #                  self.tile_size))


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


    def update_current_move(self, num: int):
        self.current_move = num

    def update_player_turn(self, new_turn):
        self.player_turn = new_turn


    def update(self):
        """The MainBoard update logic. Goes through the update functions
        of all of the SubBoards and checks for wins.
        """
        for i in range(9):
            # Board game has already finished, skipping.
            if self.sub_boards[i].result:
                continue

            if self.current_move != None and self.current_move == i:
                self.sub_boards[i].update()

                if self.check_win_main(1) or self.check_win_main(2):
                    self.state_manager.go_to_state(GameStates.RESULT)
                return
            
            self.sub_boards[i].update()
            

    def draw(self, screen):
        """Draws the SubBoards on screen.

        Args:
            screen (pygame.Surface):
                The display screen used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        for sub_board in self.sub_boards:
            sub_board.draw(screen)
