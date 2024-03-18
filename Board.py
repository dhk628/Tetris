import pygame

from pygame.locals import (
    QUIT
)

pygame.init()

screen = pygame.display.set_mode((600, 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.display.flip()
