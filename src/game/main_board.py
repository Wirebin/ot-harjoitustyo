from math import ceil
import pygame
from game.sub_board import SubBoard
from game.states import GameStates
from config.constants import WINNING_COMBOS, HIGHLIGHT_COLOR

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

        self.sub_boards = []
        for i in range(3):
            for j in range(3):
                self.sub_boards.append(SubBoard(self.player_turn, self.current_move,
                    (self.location[0] + j * (tile_size * 3 + self.border_size),
                     self.location[1] + i * (tile_size * 3 + self.border_size)),
                     tile_size))


    # def reset_board(self):
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

        for combination in WINNING_COMBOS:
            if all(replaced_board[i] == value for i, value in
                   enumerate(combination) if value == 1):
                return True
        return False


    def switch_player_turn(self, new_turn):
        self.player_turn = new_turn

    def update_current_move(self, num: int):
        self.current_move = num


    def update(self):
        """The MainBoard update logic. Goes through the update functions
        of all of the SubBoards and checks for wins.
        """
        for i, board in enumerate(self.sub_boards):
            # Board game has already finished, skipping.
            if board.result:
                continue

            if self.current_move is not None and self.current_move == i:
                board.update()

                if self.check_win_main(self.player_turn):
                    self.state_manager.go_to_state(GameStates.RESULT)
                return
            
            if self.current_move is None:
                board.update()

                if self.check_win_main(self.player_turn):
                    self.state_manager.go_to_state(GameStates.RESULT)
            

    def draw(self, canvas):
        """Draws the SubBoards on canvas.

        Args:
            canvas (pygame.Surface):
                The display canvas used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        for i, board in enumerate(self.sub_boards):
            if self.current_move == None or self.current_move == None and \
                self.current_move == i:
                board.draw_background(canvas, HIGHLIGHT_COLOR)
            else:
                board.draw_background(canvas, (171, 123, 42, 255))

            board.draw(canvas)

        # pygame.draw.rect(canvas,
        #     (200, 200, 165, 255),
        #     pygame.rect.Rect((WIDTH/2)-(TILE_SIZE*9/2),
        #                     (HEIGHT/2)-(TILE_SIZE*9/2),
        #                     TILE_SIZE * 9 + TILE_SIZE / 10 + 20,
        #                     TILE_SIZE * 9 + TILE_SIZE / 10 + 20))
