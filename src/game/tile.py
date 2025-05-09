import pygame
from ui import shapes
from config.constants import RED_COLOR, BLUE_COLOR, BLACK_COLOR, TILE_COLOR_HOVER

class Tile():
    """Class for a game tile that allows you to place your game piece on it.
    """
    def __init__(self, location: tuple, size: int):
        """The constructor for the Tile class. Creates an instance 
        of a Tile on specified location with a specific square size. 
        
        Includes a flagged variable, that tells if the tile has already 
        been clicked and a tile_owner variable, that tells which player
        owns said Tile.

        Args:
            location (tuple): The location of the tile on screen.
            size (int): The size of the tile.
        """
        self.size = size
        self.location = location
        self.flagged = False
        self.is_hovering = False
        self.tile_owner = None     # False = Player 1, True = Player 2

        self.tile_rect = pygame.Rect(self.location[0], self.location[1], self.size, self.size)
        self.mouse_pos = None


    def draw(self, canvas):
        """Draws the tile on screen. If tile is flagged, draws either a cross
        or a circle, depending on the tile_owner. Otherwise draws an empty tile 
        with mouse hover over effect.

        Args:
            canvas (pygame.Surface): 
                The display canvas used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        if not self.flagged and self.is_hovering:
            pygame.draw.rect(canvas, TILE_COLOR_HOVER, self.tile_rect)

        if self.flagged and not self.tile_owner:
        # Draw a cross
            pygame.draw.rect(canvas, TILE_COLOR_HOVER, self.tile_rect)
            shapes.cross(canvas, pygame.color.Color(RED_COLOR), self.location, self.size)

        # Draw a circle
        elif self.flagged and self.tile_owner:
            pygame.draw.rect(canvas, TILE_COLOR_HOVER, self.tile_rect)
            shapes.circle(canvas, pygame.color.Color(BLUE_COLOR), self.location, self.size)

        # Draw border for tile
        pygame.draw.rect(canvas, BLACK_COLOR, self.tile_rect, 1)
