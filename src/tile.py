import pygame
import shapes
from component import Component

class Tile(Component):
    def __init__(self, location: tuple, size: int):
        self.size = size
        self.location = location
        self.flagged = False
        self.tile_owner = 0     # 0 = None, 1 = X, 2 = O

        self.button_rect = pygame.Rect(self.location[0], self.location[1], self.size, self.size)
        self.mouse_pos = None


    def draw(self, screen):
        # If tile has not been clicked
        if not self.flagged:
            # If not hovering
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (200,200,200), self.button_rect)

            # If hovering over button
            else:
                pygame.draw.rect(screen, (150,150,150), self.button_rect)

        else:
            # Draw a cross
            if self.tile_owner == 1:
                shapes.cross(screen, pygame.color.Color(200, 0, 0), self.location, self.size)

            # Draw a circle
            elif self.flagged and self.tile_owner == 2:
                shapes.circle(screen, pygame.color.Color(0, 0, 200), self.location, self.size)

        pygame.draw.rect(screen, (0,0,0), self.button_rect, 1)
