from math import ceil
import pygame
from ui import shapes
from game.tile import Tile
from input.one_press_input import OnePressInput
from config.constants import WINNING_COMBOS, BLACK_COLOR

class SubBoard():
    """Class that handles the sub-games of tic-tac-toe. These work as the 
    smaller games, the results of which form one big game of tic-tac-toe.
    """
    def __init__(self, turn_manager, location: tuple, tile_size: int):
        """The constructor for the SubBoard class. Creates an instance of 
        a SubBoard on specified location.

        Creates a list of 9 tiles to make up a 3*3 grid board.

        Args:
            player_turn (int):
                Keeps track of whose turn it is to play.
            current_move (int):
                Keeps track on which sub_board the current move was targeted on.
            location (tuple): 
                The location of the SubBoard.
            tile_size (int): 
                The shared tile size passed down from MainBoard.
        """
        self.turn_manager = turn_manager
        self.location = location
        self.result = None

        self.tile_size = tile_size
        self.border_size = ceil(tile_size / 10)
        self.board_rect = pygame.rect.Rect(
            location[0], location[1],
            tile_size * 3, tile_size * 3
        )
        self.border_rect = pygame.rect.Rect(
            location[0] - self.border_size,
            location[1] - self.border_size,
            tile_size * 3 + self.border_size * 2,
            tile_size * 3 + self.border_size * 2)

        self.tiles = []
        for i in range(3):
            for j in range(3):
                self.tiles.append(Tile(
                    ((self.location[0] + (j * tile_size)),
                     (self.location[1] + (i * tile_size))),
                    tile_size))

    def update(self):
        """Updates the SubBoard instance logic. Specifically checks if 
        mouse has been clicked over a tile and marks it for the current
        player. 
        """
        mouse_pos = pygame.mouse.get_pos()

        for i, tile in enumerate(self.tiles):
            if tile.tile_rect.collidepoint(mouse_pos):
                tile.is_hovering = True

                if OnePressInput.is_mouse_clicked(0) and not tile.flagged:
                    self.on_tile_click(tile, i)
            else:
                tile.is_hovering = False

    def on_tile_click(self, tile, tile_index):
        tile.flagged = True
        tile.tile_owner = self.turn_manager.get_turn()

        if self.check_win_sub(self.turn_manager.get_turn()):
            self.result = self.turn_manager.get_turn()

        self.turn_manager.update_turn(not self.turn_manager.get_turn())
        self.turn_manager.update_move(tile_index)

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

        for combination in WINNING_COMBOS:
            if all(replaced_board[i] == value for i, value in
                   enumerate(combination) if value == 1):
                return True
        return False

    def draw(self, canvas):
        """Draws the SubBoard which consists of the nine tiles created 
        in the constructor. If the SubBoard game has finished. Displays a
        cross or a circle over the whole SubBoard area depending on who won.

        Args:
            canvas (pygame.Surface): 
                The display canvas used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        if self.result is not None:
            pygame.draw.rect(canvas, (136, 96, 28, 255), self.border_rect)
            pygame.draw.rect(canvas, (0, 0, 0, 255), self.border_rect, self.border_size)

            if not self.result:
                shapes.cross(canvas,
                             pygame.color.Color(200, 0, 0, 255),
                             self.location,
                             self.tile_size * 3)
            elif self.result:
                shapes.circle(canvas,
                              pygame.color.Color(0, 0, 200, 255),
                              self.location,
                              self.tile_size * 3)
            return

        # Border for board
        pygame.draw.rect(canvas, BLACK_COLOR, self.border_rect, self.border_size)
        for tile in self.tiles:
            tile.draw(canvas)

    def draw_background(self, canvas: pygame.Surface, color: pygame.Color):
        """Draws a background of one color for the board.

        Args:
            canvas (pygame.Surface):
                The display canvas used for pygame. Necessary in order
                to use the draw function of pygame.
            color (pygame.Color):
                The color of the background.
        """
        pygame.draw.rect(canvas, color, self.board_rect)
