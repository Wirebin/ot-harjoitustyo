from component import Component
from sub_board import Sub_Board
import pygame

class Main_Board(Component):
    def __init__(self, location: tuple, tile_size: int):
        self.location = location
        self.size = tile_size
        self.main_board_rect = pygame.rect.Rect(location[0], location[1], tile_size*9, tile_size*9)

        self.sub_boards = []
        for i in range(3):
            for j in range(3):
                self.sub_boards.append(Sub_Board((self.location[0]+(i*tile_size*3), self.location[1]+(j*tile_size*3)), self.size))

    def update(self, mouse_pos):
        for sub_board in self.sub_boards:
            sub_board.update(mouse_pos)

    def draw(self, screen, mouse_pos):
        for sub_board in self.sub_boards:
            sub_board.draw(screen, mouse_pos)
            
        pygame.draw.rect(screen, (0,0,0), self.main_board_rect, 4)