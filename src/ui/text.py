import pygame

class Text():
    def __init__(self, location, font_size, color, text, align="topleft"):
        self._text = text
        self._font = pygame.font.Font(None, font_size)
        self._text_render = self._font.render(self._text, True, color)
        self._text_rect = self._text_render.get_rect()
        setattr(self._text_rect, align, location)

    def draw(self, canvas):
        canvas.blit(self._text_render, self._text_rect)
