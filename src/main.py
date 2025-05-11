import sys
import pygame
from ui.button import Button
from input.one_press_input import OnePressInput
from game.states import GameStates
from game.main_board import MainBoard
from game.state_manager import StateManager
from game.turn_manager import TurnManager
from ui.shapes import cross, circle
from config.constants import WIDTH, HEIGHT, TILE_SIZE, BACKGROUND_COLOR, \
                             BLUE_COLOR, RED_COLOR

pygame.init()
fps = 60
fps_clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
canvas = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
state_manager = StateManager()
turn_manager = TurnManager(False)

# Place board on the center of the screen
board = MainBoard(state_manager, turn_manager, ((WIDTH/2)-(TILE_SIZE*9/2), (HEIGHT/2)-(TILE_SIZE*9/2)), TILE_SIZE)


def restart_game():
    board.reset_board()
    state_manager.go_to_state(GameStates.GAME)


start_button = Button(((WIDTH / 2) - (100 / 2), (HEIGHT / 2) - 60),
                      (120, 50),
                      "Start",
                      state_manager.next_state)

quit_button = Button(((WIDTH / 2) - (100 / 2), (HEIGHT / 2)),
                      (120, 50),
                      "Quit",
                      exit)

restart_button = Button(((WIDTH / 2) - (100 / 2), (HEIGHT) - (80)),
                        (120, 50),
                        "Restart",
                        restart_game)

def handle_game_state(state: GameStates):
    if state == GameStates.MENU:
        start_button.update()
        quit_button.update()
        start_button.draw(canvas)
        quit_button.draw(canvas)

    elif state == GameStates.GAME:
        if not turn_manager.player_turn:
            cross(canvas, RED_COLOR, (WIDTH / 2 - 100, 20), 60)
        else:
            circle(canvas, BLUE_COLOR, (WIDTH / 2 - 100, 20), 60)

        board.update()
        board.draw(canvas)

    elif state == GameStates.RESULT:
        restart_button.update()
        board.draw(canvas)
        restart_button.draw(canvas)


def run():
    while True:
        fps_clock.tick(fps)
        canvas.fill(BACKGROUND_COLOR)
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
