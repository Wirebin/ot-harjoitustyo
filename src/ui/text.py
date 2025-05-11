import pygame

class Text():
    def __init__(self, location, font_size, color, text, align="topleft"):
        self.location = location
        self.font = pygame.font.Font(None, font_size)
        self.text_render = self.font.render(text, True, color)
        self.text_rect = self.text_render.get_rect()
        setattr(self.text_rect, align, location)

    def draw(self, canvas):
        canvas.blit(self.text_render, self.text_rect)
