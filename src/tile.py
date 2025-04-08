from component import Component
import pygame

class Tile(Component):
    def __init__(self, location: tuple, size: int):
        self.size = size
        self.location = location
        self.status = None

        self.button_rect = pygame.Rect(self.location[0], self.location[1], self.size, self.size)

    def update(self, mouse_pos):
        # If left-clicked on top of tile
        if self.button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.status = 1

    def draw(self, screen, mouse_pos):
        # If not hovering
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200,200,200), self.button_rect)

        # If hovering over button
        else:
            pygame.draw.rect(screen, (150,150,150), self.button_rect)

        pygame.draw.rect(screen, (0,0,0), self.button_rect, 1)