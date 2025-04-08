from component import Component
from tile import Tile
import pygame

class Sub_Board(Component):
    def __init__(self, location: tuple, tile_size: int):
        self.location = location

        self.tile_size = tile_size
        self.sub_board_rect = pygame.rect.Rect(location[0], location[1], tile_size*3, tile_size*3)
        self.tiles = []
        for i in range(3):
            for j in range(3):
                self.tiles.append(Tile((self.location[0]+(i*tile_size), self.location[1]+(j*tile_size)), tile_size))

    def update(self, mouse_pos):
        for tile in self.tiles:
            tile.update(mouse_pos)

    def draw(self, screen, mouse_pos):
        for tile in self.tiles:
            tile.draw(screen, mouse_pos)

        pygame.draw.rect(screen, (0,0,0), self.sub_board_rect, 2)
