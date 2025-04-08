from state_manager import State_Manager
from main_board import Main_Board
from states import Game_States
from button import Button
import pygame
import sys

pygame.init()
fps = 30
fps_clock = pygame.time.Clock()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
state_manager = State_Manager()

start_button = Button(((width/2)-(100/2), (height/2)-(70/2)), (100, 50), (200, 200, 200), (150,150,150), "Start", state_manager.next_state)
board = Main_Board(((width/2)-(220/2), (height/2)-(220/2)), 25)

while True:
    screen.fill((100,100,100))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    print(state_manager.current_state)
    if state_manager.current_state == Game_States.MENU:
        start_button.update(mouse_pos)
        start_button.draw(screen, mouse_pos)

    elif state_manager.current_state == Game_States.GAME:
        board.update(mouse_pos)
        board.draw(screen, mouse_pos)

    elif state_manager.current_state == Game_States.RESULT:
        pass

    else:
        raise state_manager(IndexError, "Invalid index for a game state.")

    pygame.display.flip()
    fps_clock.tick()

