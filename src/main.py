import sys
import pygame
from ui.button import Button
from input.one_press_input import OnePressInput
from game.states import GameStates
from game.main_board import MainBoard
from game.sub_board import SubBoard
from game.state_manager import StateManager
from config.constants import WIDTH, HEIGHT, TILE_SIZE, BACKGROUND_COLOR

pygame.init()
fps = 60
fps_clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
canvas = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
state_manager = StateManager()

start_button = Button(((WIDTH/2)-(100/2), (HEIGHT/2)-(70/2)),
                      (100, 50),
                      "Start",
                      state_manager.next_state)
restart_button = Button(((WIDTH/2)-(100/2), (HEIGHT)-(80)),
                        (120, 50),
                        "Restart",
                        None)

# Place board on the center of the screen
board = MainBoard(state_manager, ((WIDTH/2)-(TILE_SIZE*9/2), (HEIGHT/2)-(TILE_SIZE*9/2)), TILE_SIZE)
a = 1
b= None
test_board = SubBoard(a, b, (20,20), 30)

def restart_game(main_board: MainBoard):
    main_board.reset()
    state_manager.go_to_state(GameStates.GAME)


def handle_game_state(state: GameStates):
    if state == GameStates.MENU:
        start_button.update()
        start_button.draw(canvas)

    elif state == GameStates.GAME:
        test_board.update()
        test_board.draw(canvas)

        board.update()
        board.draw(canvas)

    elif state == GameStates.RESULT:
        restart_button.update()
        board.draw(canvas)
        restart_button.draw(canvas)


def run():
    while True:
        fps_clock.tick(fps)
        screen.fill(BACKGROUND_COLOR)
        OnePressInput.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        handle_game_state(state_manager.current_state)

        screen.blit(canvas, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    run()
