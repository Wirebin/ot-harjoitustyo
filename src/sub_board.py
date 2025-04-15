from math import ceil
import pygame
import shapes
from tile import Tile
from component import Component

class SubBoard(Component):
    def __init__(self, location: tuple, tile_size: int):
        self.location = location
        self.result = 0

        self.tile_size = tile_size
        self.border_size = ceil(tile_size / 10)
        self.border_rect = pygame.rect.Rect(
            location[0] - self.border_size,
            location[1] - self.border_size,
            tile_size * 3 + self.border_size * 2,
            tile_size * 3 + self.border_size * 2)

        self.tiles = []
        for i in range(3):
            for j in range(3):
                self.tiles.append(Tile(
                    ((self.location[0] + (i * tile_size)),
                     (self.location[1] + (j * tile_size))),
                    tile_size))


    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.border_rect, self.border_size)

        if self.result:
            if self.result == 1:
                shapes.cross(screen,
                             pygame.color.Color(200, 0, 0),
                             self.location,
                             self.tile_size * 3)
            elif self.result == 2:
                shapes.circle(screen,
                              pygame.color.Color(0, 0, 200),
                              self.location,
                              self.tile_size * 3)
            return

        for tile in self.tiles:
            tile.draw(screen)
