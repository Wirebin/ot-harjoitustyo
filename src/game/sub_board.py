from math import ceil
import pygame
from ui import shapes
from game.tile import Tile
from input.one_press_input import OnePressInput

class SubBoard():
    """Class that handles the sub-games of tic-tac-toe. These work as the 
    smaller games, the results of which form one big game of tic-tac-toe.
    """
    def __init__(self, main_board, location: tuple, tile_size: int):
        """The constructor for the SubBoard class. Creates an instance of 
        a SubBoard on specified location.

        Creates a list of 9 tiles to make up a 3*3 grid board.

        Args:
            main_board (MainBoard): 
                MainBoard instance to access player_turn variable.
            location (tuple): 
                The location of the SubBoard.
            tile_size (int): 
                The shared tile size passed down from MainBoard.
        """
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


    def check_win_sub(self, player):
        """Checks the winning conditions for SubBoards.

        Creates a temporary board that replaces all but the players values on the board
        with a zero (0) and the player values with a one (1). This is then compared with
        the winning combinations to see if the player has won.

        Args:
            player (int): 
                The player which the winning conditions will be checked for.

        Returns:
            bool: 
                Returns True, if the player has won the SubBoard game. 
                Otherwise returns False.
        """
        replaced_board = [1 if tile.tile_owner == player else 0 for tile in self.tiles]

        for combination in self.main_board.winning_combos:
            if all(replaced_board[i] == value for i, value in
                   enumerate(combination) if value == 1):
                return True
        return False


    def update(self):
        """Updates the SubBoard instance logic. Specifically checks if 
        mouse has been clicked over a tile and marks it for the current
        player. 
        """
        mouse_pos = pygame.mouse.get_pos()

        for tile in self.tiles:
            if tile.button_rect.collidepoint(mouse_pos) and \
                OnePressInput.is_mouse_clicked(0) and not tile.flagged:
                tile.flagged = True

                if self.main_board.player_turn == 1:
                    tile.tile_owner = 1
                elif self.main_board.player_turn == 2:
                    tile.tile_owner = 2

                if self.check_win_sub(self.main_board.player_turn):
                    self.result = self.main_board.player_turn
                self.main_board.player_turn = 1 if self.main_board.player_turn == 2 else 2


    def draw(self, screen):
        """Draws the SubBoard which consists of the nine tiles created 
        in the constructor. If the SubBoard game has finished. Displays a
        cross or a circle over the whole SubBoard area depending on who won.

        Args:
            screen (pygame.Surface): 
                The display screen used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        if self.result:
            pygame.draw.rect(screen, (136,96,28), self.border_rect)
            pygame.draw.rect(screen, (0,0,0), self.border_rect, self.border_size)

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

        pygame.draw.rect(screen, (0,0,0), self.border_rect, self.border_size)
        for tile in self.tiles:
            tile.draw(screen)
