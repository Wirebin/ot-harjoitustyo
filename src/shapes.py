from math import ceil
import pygame

def cross(screen: pygame.Surface, color: pygame.color.Color, location: tuple, size: int):
    pygame.draw.line(screen,
                     color,
                     (location[0] + 4, location[1] + 4),                # Offset of 4
                     (location[0] + size - 5, location[1] + size - 5),  # Offset of 5
                     ceil(size / 10))
    pygame.draw.line(screen,
                     color,
                     (location[0] + size - 5, location[1] + 4),         # Offset 5 & 4
                     (location[0] + 4, location[1] + size - 5),
                     ceil(size / 10))

def circle(screen: pygame.Surface, color: pygame.color.Color, location: tuple, size: int):
    pygame.draw.circle(screen,
                       color,
                       (location[0] + (size / 2), location[1] + (size / 2)),
                       size / 2.5,
                       ceil(size / 10))
