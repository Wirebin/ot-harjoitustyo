from math import ceil
import pygame

def cross(screen: pygame.Surface, color: pygame.color.Color, location: tuple, size: int):
    line_width = ceil(size / 10)
    pygame.draw.line(screen,
                     color,
                     (location[0] + (0.2 * size) - line_width / 2, location[1] + (0.2 * size) - line_width),
                     (location[0] + (0.8 * size) + line_width / 2, location[1] + (0.8 * size) + line_width / 2),
                      line_width)
    pygame.draw.line(screen,
                     color,
                     (location[0] + (0.8 * size) + line_width / 2, location[1] + (0.2 * size) - line_width),
                     (location[0] + (0.2 * size) - line_width / 2, location[1] + (0.8 * size) + line_width / 2),
                     ceil(size / 10))

def circle(screen: pygame.Surface, color: pygame.color.Color, location: tuple, size: int):
    pygame.draw.circle(screen,
                       color,
                       (location[0] + (size / 2), location[1] + (size / 2)),
                       size / 2.5,
                       ceil(size / 10))
