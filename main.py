import pygame
import math

from shapes import I, O, T, S, Z, J, L, shapes, shape_colors, CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, ORANGE

from pygame.locals import (
    QUIT,
    K_ESCAPE,
    K_DOWN,
    K_s,
    K_UP,
    K_w,
    K_LEFT,
    K_a,
    K_RIGHT,
    K_d
)


def draw_shape(shape, position, rotation):
    for i in range(4):
        for j in range(4):
            if shape[rotation][j][i] == '0':
                pygame.draw.rect(game, RED, grid_coordinates[j + position[1]][i + position[0]] + (BOX_SIZE, BOX_SIZE),
                                 0)


def is_position_valid(shape, position):
    for i in range(4):
        for j in range(4):
            if shape[rotation][j][i] == '0':
                if (position[0] + i) not in range(10) or (position[1] + j) not in range(20):
                    return False

    return True


BOX_SIZE = 30
LINE_WIDTH = 2
BOUNDARY_WIDTH = 4
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
GAME_HEIGHT = 19 * LINE_WIDTH + 20 * BOX_SIZE
GAME_WIDTH = 9 * LINE_WIDTH + 10 * BOX_SIZE
OFFSET_HEIGHT = math.floor(0.9 * (WINDOW_HEIGHT - GAME_HEIGHT))
OFFSET_WIDTH = math.floor((WINDOW_WIDTH - GAME_WIDTH) / 2)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)

grid = [[0 for x in range(10)] for y in range(20)]

grid_coordinates = []
for y in range(20):
    grid_coordinates.append([])
    for x in range(10):
        grid_coordinates[y].append((x * (BOX_SIZE + LINE_WIDTH), y * (BOX_SIZE + LINE_WIDTH)))

pygame.init()

position = [3, 0]
rotation = 0

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

fall_clock = pygame.time.Clock()

fall_time = 0
fall_speed = 500

running = True
screen.fill(BLACK)

# draw border
pygame.draw.rect(screen, WHITE, (
    OFFSET_WIDTH - BOUNDARY_WIDTH, OFFSET_HEIGHT - BOUNDARY_WIDTH, GAME_WIDTH + 2 * BOUNDARY_WIDTH,
    GAME_HEIGHT + 2 * BOUNDARY_WIDTH), BOUNDARY_WIDTH)

while running:
    game.fill(BLACK)

    # draw gridlines
    for x in range(9):
        pygame.draw.line(game, GREY, (30 + 32 * x, 0), (30 + 32 * x, GAME_HEIGHT), LINE_WIDTH)

    for y in range(19):
        pygame.draw.line(game, GREY, (0, 30 + 32 * y), (GAME_WIDTH, 30 + 32 * y), LINE_WIDTH)

    fall_time += fall_clock.get_rawtime()
    fall_clock.tick()

    if fall_time > fall_speed:
        fall_time = 0
        position[1] += 1
        if not is_position_valid(I, position):
            position[1] -= 1

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == (K_s or K_DOWN):
                position[1] += 1
                if not is_position_valid(I, position):
                    print("Not valid")
                    position[1] -= 1
            elif event.key == (K_d or K_RIGHT):
                position[0] += 1
                print("position = ", position)
                print(I[rotation])
                if not is_position_valid(I, position):
                    print("Not valid")
                    position[0] -= 1
            elif event.key == (K_a or K_LEFT):
                position[0] -= 1
                if not is_position_valid(I, position):
                    print("Not valid")
                    position[0] += 1
            # elif event.key == (K_w or K_UP):
            # rotate

    draw_shape(I, position, rotation)

    screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))

    pygame.display.update()
