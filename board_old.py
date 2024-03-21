import pygame
import math

from pygame.locals import (
    QUIT
)

BOX_SIZE = 30
LINE_WIDTH = 2
BOUNDARY_WIDTH = 4
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
GAME_HEIGHT = 2*BOUNDARY_WIDTH + 19*LINE_WIDTH + 20*BOX_SIZE
GAME_WIDTH = 2*BOUNDARY_WIDTH + 9*LINE_WIDTH + 10*BOX_SIZE
OFFSET_HEIGHT = math.floor(0.9*(WINDOW_HEIGHT - GAME_HEIGHT))
OFFSET_WIDTH = math.floor((WINDOW_WIDTH - GAME_WIDTH) / 2)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)

grid = [[0 for x in range(10)] for y in range(20)]

grid_coordinates = []
for y in range(20):
    grid_coordinates.append([])
    for x in range(10):
        grid_coordinates[y].append((OFFSET_WIDTH + BOUNDARY_WIDTH + 1 + x*(BOX_SIZE + LINE_WIDTH), OFFSET_HEIGHT + BOUNDARY_WIDTH + 1 + y*(BOX_SIZE + LINE_WIDTH)))


pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (OFFSET_WIDTH, OFFSET_HEIGHT, GAME_WIDTH, GAME_HEIGHT), BOUNDARY_WIDTH)

    for x in range(1, 10):
        pygame.draw.rect(screen, BLACK, (grid_coordinates[0][x][0] - LINE_WIDTH, grid_coordinates[0][x][1] - 1, LINE_WIDTH, GAME_HEIGHT - 2*BOUNDARY_WIDTH), 0)
    for y in range(1,20):
        pygame.draw.rect(screen, BLACK, (grid_coordinates[y][0][0] - 1, grid_coordinates[y][0][1] - LINE_WIDTH, GAME_WIDTH - 2*BOUNDARY_WIDTH, LINE_WIDTH), 0)

    pygame.draw.rect(screen, RED, (OFFSET_WIDTH, OFFSET_HEIGHT, GAME_WIDTH, GAME_HEIGHT), 0)
    pygame.display.flip()
