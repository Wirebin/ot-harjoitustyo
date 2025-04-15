import sys
import pygame
from button import Button
from states import GameStates
from main_board import MainBoard
from state_manager import StateManager

pygame.init()
FPS = 30
FPS_CLOCK = pygame.time.Clock()

WIDTH = 600
HEIGHT = 400
TILE_SIZE = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
state_manager = StateManager()

start_button = Button(((WIDTH/2)-(100/2), (HEIGHT/2)-(70/2)),
                       (100, 50),
                       "Start",
                       state_manager.next_state)

# Place board on the center of the screen
board = MainBoard(((WIDTH/2)-(TILE_SIZE*9/2), (HEIGHT/2)-(TILE_SIZE*9/2)), TILE_SIZE)

while True:
    screen.fill((100,100,100))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if state_manager.current_state == GameStates.MENU:
        start_button.update()
        start_button.draw(screen)

    elif state_manager.current_state == GameStates.GAME:
        board.update()
        board.draw(screen)

    elif state_manager.current_state == GameStates.RESULT:
        print("WINNER")

    pygame.display.flip()
    FPS_CLOCK.tick()
