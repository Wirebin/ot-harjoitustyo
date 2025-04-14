import pygame
from component import Component

class Button(Component):
    def __init__(self,
                 location: tuple,
                 size: tuple,
                 button_text: str,
                 on_click=None):

        self.location = location
        self.size = size

        self.button_rect = pygame.Rect(self.location[0],
                                       self.location[1],
                                       self.size[0],
                                       self.size[1])

        self.button_text = button_text
        font = pygame.font.Font(None, self.button_rect.height - 10)
        self.button_text_render = font.render(button_text, True, (0,0,0))
        self.button_text_rect = self.button_text_render.get_rect(center=self.button_rect.center)

        self.on_click = on_click

    def update(self):
        # If left-clicked on top of button
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) and \
            pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.on_click()

    def draw(self, screen):
        # If hovering over button
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (150, 150, 150), self.button_rect)
        # Not hovering over
        else:
            pygame.draw.rect(screen, (200, 200, 200), self.button_rect)

        # Draw text
        screen.blit(self.button_text_render, self.button_text_rect)
        