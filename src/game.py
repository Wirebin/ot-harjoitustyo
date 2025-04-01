from button import Button
import pygame
import sys

pygame.init()
fps = 30
fps_clock = pygame.time.Clock()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))

start_button = Button(((width/2)-(100/2), (height/2)-(50/2)), (100, 50), (200, 200, 200), (150,150,150), "Start")

while True:
    screen.fill((100,100,100))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    start_button.update(mouse_pos)
    start_button.draw(screen, mouse_pos)

    pygame.display.flip()
    fps_clock.tick()

