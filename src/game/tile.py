import pygame
from ui import shapes

class Tile():
    """Class for a game tile that allows you to place your shape on it.
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
        self.tile_owner = 0     # 0 = None, 1 = X, 2 = O

        self.button_rect = pygame.Rect(self.location[0], self.location[1], self.size, self.size)
        self.mouse_pos = None


    def draw(self, screen):
        """Draws the tile on screen. If tile is flagged, draws either a cross
        or a circle, depending on the tile_owner. Otherwise draws an empty tile 
        with mouse hover over effect.

        Args:
            screen (pygame.Surface): 
                The display screen used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        if not self.flagged:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (136,96,28), self.button_rect)

            else:
                pygame.draw.rect(screen, (177,124,36), self.button_rect)

        else:
            # Draw a cross
            if self.tile_owner == 1:
                pygame.draw.rect(screen, (136,96,28), self.button_rect)
                shapes.cross(screen, pygame.color.Color(200, 0, 0), self.location, self.size)

            # Draw a circle
            elif self.tile_owner == 2:
                pygame.draw.rect(screen, (136,96,28), self.button_rect)
                shapes.circle(screen, pygame.color.Color(0, 0, 200), self.location, self.size)

        pygame.draw.rect(screen, (0,0,0), self.button_rect, 1)
