import sys
import pygame
from ui.button import Button
from input.one_press_input import OnePressInput
from game.states import GameStates
from game.main_board import MainBoard
from game.state_manager import StateManager

pygame.init()
FPS = 30
FPS_CLOCK = pygame.time.Clock()

WIDTH = 600
HEIGHT = 500
TILE_SIZE = 30
BACKGROUND_COLOR = (214, 212, 185)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
state_manager = StateManager()

start_button = Button(((WIDTH/2)-(100/2), (HEIGHT/2)-(70/2)),
                      (100, 50),
                      "Start",
                      state_manager.next_state)
restart_button = Button(((WIDTH/2)-(100/2), (HEIGHT/2)-(70/2)),
                        (120, 50),
                        "Restart",
                        None)

# Place board on the center of the screen
board = MainBoard(state_manager, ((WIDTH/2)-(TILE_SIZE*9/2), (HEIGHT/2)-(TILE_SIZE*9/2)), TILE_SIZE)


def handle_game_state(state: GameStates):
    if state == GameStates.MENU:
        start_button.update()
        start_button.draw(screen)

    elif state == GameStates.GAME:
        pygame.draw.rect(screen, (200, 200, 165),
                        pygame.rect.Rect(
                            (WIDTH/2)-(TILE_SIZE*9/2), 
                            (HEIGHT/2)-(TILE_SIZE*9/2),
                            TILE_SIZE * 9 + TILE_SIZE / 10 + 20,
                            TILE_SIZE * 9 + TILE_SIZE / 10 + 20))
        
        board.update()
        board.draw(screen)

    elif state == GameStates.RESULT:
        restart_button.update()
        board.draw(screen)
        restart_button.draw(screen)


def run():
    while True:
        screen.fill(BACKGROUND_COLOR)
        OnePressInput.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        handle_game_state(state_manager.current_state)

        pygame.display.flip()
        FPS_CLOCK.tick()


if __name__ == "__main__":
    run()
