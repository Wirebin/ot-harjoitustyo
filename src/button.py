import pygame
from component import Component

class Button(Component):
    def __init__(self, location: tuple, size: tuple, color_normal: tuple, color_hover: tuple, button_text, on_click=None):
        self.location = location
        self.size = size
        self.color_normal = color_normal
        self.color_hover = color_hover
        
        self.button_surface = pygame.Surface((self.size[0], self.size[1]))
        self.button_rect = pygame.Rect(self.location[0], self.location[1], self.size[0], self.size[1])
        self.button_text = button_text

        self.on_click = on_click

    def update(self, mouse_pos):
        # If left-clicked on top of button
        if self.button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.on_click()

    def draw(self, screen, mouse_pos):
        self.button_surface.fill(self.color_normal)
        # If hovering over button
        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.color_hover)
        
        screen.blit(self.button_surface, self.button_rect)