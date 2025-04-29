from math import ceil
import pygame

def cross(screen: pygame.Surface, color: pygame.color.Color, location: tuple, size: int):
    """Draws a cross of a specific color and size onto the screen.

    Args:
        screen (pygame.Surface): 
            The display screen used for pygame. Necessary in order
            to use the draw function of pygame.
        color (pygame.color.Color): 
            The color of the cross.
        location (tuple): 
            The location of the cross starting from the top left corner.
        size (int): 
            The size of the cross.
    """
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
    """Draws a circle of a specific color and size onto the screen.

    Args:
        screen (pygame.Surface): 
            The display screen used for pygame. Necessary in order
            to use the draw function of pygame.
        color (pygame.color.Color): 
            The color of the circle.
        location (tuple): 
            The location of the circle.
        size (int): 
            The size of the circle
    """
    pygame.draw.circle(screen,
                       color,
                       (location[0] + (size / 2), location[1] + (size / 2)),
                       size / 2.5,
                       ceil(size / 10))
